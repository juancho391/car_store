from flask import url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from slugify import slugify
from sqlalchemy.exc import IntegrityError
from db import db


class User(db.Model, UserMixin):
    __tablename__ = "ad_user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)


class Car(db.Model):
    __tablename__ = "ad_car"

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False)
    # image_filename = db.Column(db.LargeBinary, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("ad_user.id"), nullable=False)

    def __repr__(self):
        return f"<Car {self.make} {self.model} ({self.year})>"

    def generate_slug(self):
        base_slug = slugify(f"{self.make}-{self.model}-{self.year}")
        slug = base_slug
        counter = 1
        while Car.query.filter_by(slug=slug).first():
            slug = f"{base_slug}-{counter}"
            counter += 1
        self.slug = slug

    def save(self):
        if not self.id:
            self.generate_slug()
            db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("A car with this slug already exists.")

    @staticmethod
    def get_by_slug(slug):
        return Car.query.filter_by(slug=slug).first()

    @staticmethod
    def get_all():
        return Car.query.all()

    @staticmethod
    def get_cars_except_user_cars(user_id):
        return Car.query.filter(Car.user_id != user_id).all()

    @staticmethod
    def get_user_cars(user_id):
        return Car.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_id(car_id):
        return Car.query.get(car_id)

    @staticmethod
    def delte_by_id(car_id):
        car = Car.get_by_id(car_id)
        if car:
            db.session.delete(car)
            db.session.commit()
