from flask import Flask, render_template, request, redirect, url_for, abort
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
    login_required,
)
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import urlparse
from dotenv import load_dotenv
from forms import LoginForm, SignupForm, CarForm
from db import db
import os

load_dotenv()
DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
from models import User, Car

login_manager = LoginManager(app)
login_manager.login_view = "login"


@app.route("/")
def index():
    if current_user.is_authenticated:
        cars = Car.get_cars_except_user_cars(current_user.id)
    else:
        cars = None
    return render_template("index.html", cars=cars)


@app.route("/my_cars")
@login_required
def my_cars():
    cars = Car.get_user_cars(current_user.id)
    return render_template("my_cars.html", cars=cars)


@app.route("/add_car", methods=["GET", "POST"])
@login_required
def add_car():
    form = CarForm()
    if form.validate_on_submit():
        make = form.make.data
        model = form.model.data
        year = int(form.year.data)
        price = float(form.price.data)
        car = Car(
            make=make,
            model=model,
            year=year,
            price=price,
            user_id=current_user.id,
        )
        car.generate_slug()
        car.save()
        return redirect(url_for("my_cars"))
    return render_template("car_form.html", form=form)


@app.route("/delete_car/<int:car_id>", methods=["POST"])
@login_required
def delete_car(car_id):
    car = Car.get_by_id(car_id)
    if car.user_id != current_user.id:
        abort(403)
    Car.delte_by_id(car_id)
    return redirect(url_for("my_cars"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get("next")
            if not next_page or urlparse(next_page).netloc != "":
                next_page = url_for("index")
            return redirect(next_page)
    return render_template("login_form.html", form=form)


@app.route("/car/<slug>")
@login_required
def car_detail(slug):
    car = Car.get_by_slug(slug)
    return render_template("car_detail.html", car=car)


@app.route("/signup", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User.get_by_email(email)
        if user is not None:
            error = f"El email {email} ya está registrado"
        else:
            user = User(name=name, email=email)
            user.set_password(password)
            user.save()
            login_user(user, remember=True)
            next_page = request.args.get("next", None)
            if not next_page or urlparse(next_page).netloc != "":
                next_page = url_for("index")
            return redirect(next_page)
    return render_template("/signup_form.html", form=form, error=error)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print(db.engine.table_names())
    app.run(debug=True)
