# Car Store

A simple web application built with **Flask** to manage a car store. This project includes user authentication, car listings, and form handling, and it was created for the **Web Programming** course.

## Features

- User registration and login (using Flask-Login)
- Form handling and validation (using Flask-WTF)
- PostgreSQL database integration (via Flask-SQLAlchemy and psycopg)
- Slug generation for car URLs (using python-slugify)
- Email validation for user registration
- Password hashing using Werkzeug

## Requirements

- Python 3.10+
- Flask
- Flask-WTF
- Flask-Login
- Flask-SQLAlchemy
- psycopg
- python-slugify
- email-validator
- python-dotenv

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/juancho391/car_store.git
   cd car_store

   ```

2. Install dependencies using uv or rye:
   uv add Flask Flask-WTF Flask-Login Flask-SQLAlchemy python-slugify email-validator python-dotenv psycopg

3. Create a .env file for environment variables:
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/car_store_db

4. Docker Setup (Optional)
   Use the included docker-compose.yml to run a PostgreSQL database:

   docker compose up -d

   Then update DATABASE_URL in .env to connect to the container.


5. ## Available Routes

| Route | Methods | Description | Login Required |
|-------|--------|-------------|----------------|
| `/` | GET | Home page. Shows all cars if authenticated, or welcome message if not. | No |
| `/login` | GET, POST | Login form and authentication. | No |
| `/signup` | GET, POST | Sign up form to create a new user. | No |
| `/logout` | GET | Logout the current user. | Yes |
| `/my_cars` | GET | Shows all cars owned by the logged-in user. | Yes |
| `/add_car` | GET, POST | Form to create a new car. | Yes |
| `/car/<slug>` | GET | Detail view of a specific car identified by its slug. | Yes |
| `/delete_car/<int:car_id>` | POST | Delete a car owned by the logged-in user. | Yes |
| `/update_car/<int:car_id>` | GET, POST | Form to update a car owned by the logged-in user. | Yes |
| `/profile` | GET, POST | User profile page with user's cars and option to add new cars. | Yes |

7. ##Project Folder Structure
## Project Folder Structure

**car_store/**  
├─ **src/**  
│  ├─ **run.py** – Entry point (Flask app, routes, login)  
│  ├─ **models.py** – SQLAlchemy models (`User`, `Car`) and query methods  
│  ├─ **forms.py** – WTForms (`LoginForm`, `SignupForm`, `CarForm`)  
│  ├─ **db.py** – Database initialization (`SQLAlchemy` instance)  
│  ├─ **templates/** – Jinja2 templates  
│  │  ├─ **base_template.html** – Base layout (head, nav, main, footer)  
│  │  ├─ **index.html**  
│  │  ├─ **profile_user.html**  
│  │  ├─ **update_car.html**  
│  │  └─ **car_detail.html**  
│  └─ **static/** – Static files (CSS, images, uploads)  
│     ├─ **base-css.css**  
│     ├─ **profile_user.css**  
│     ├─ **update_car.css** – (fix typo: was `upadte_car.css`)  
│     ├─ **car_detail.css**  
│     ├─ **index.css**  
│     └─ **images/**  
│        └─ `carro.png`  
├─ **migrations/** – Flask-Migrate migrations (if used)  
├─ **.env** – Environment variables (`DB`, `SECRET_KEY`)  
├─ **requirements.txt**  
└─ **README.md**

9. ## Database Models

### User (1) — (N) Car

**Table:** `ad_user`  

**Fields:**  
- `id`: Integer, **PK**  
- `name`: String(80), **NOT NULL**  
- `email`: String(256), **UNIQUE, NOT NULL**  
- `password`: String(256) (hashed)  

**Relationships:**  
- One-to-many with `Car` (`User.cars` → list of user's cars)  

**Typical Methods:**  
- `set_password(password)` → store password hash  
- `check_password(password)` → validate password  
- `save()` → commit changes to the DB  
- `get_by_email(email)`, `get_by_id(id)` → helper queries  

---

### Car

**Table:** `ad_car`  

**Fields:**  
- `id`: Integer, **PK**  
- `make`: String(80), **NOT NULL** (brand)  
- `model`: String(80), **NOT NULL**  
- `year`: Integer, **NOT NULL**  
- `price`: Float, **NOT NULL**  
- `slug`: String(150), **UNIQUE, NOT NULL** (friendly URL)  
- `image_filename`: String(225) (relative path in `static/`)  
- `user_id`: Integer, **FK → `ad_user.id`, NOT NULL**  

**Relationships:**  
- Belongs to `User` (`Car.user_id` → owner)  

**Typical Methods:**  
- `generate_slug()` → create unique slug using `slugify`  
- `save()` → insert/update record and handle `IntegrityError`  
- `get_by_slug(slug)`, `get_by_make(make, exclude_id=None, limit=5)`, `get_all()`, `get_by_id(id)`  


