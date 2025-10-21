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
car_store/
├── src/
│   ├── run.py                  # Punto de entrada (Flask app, routes, login)
│   ├── models.py               # Modelos SQLAlchemy (User, Car) y métodos de consulta
│   ├── forms.py                # WTForms (LoginForm, SignupForm, CarForm)
│   ├── db.py                   # Inicialización de db (SQLAlchemy instance)
│   ├── templates/              # Plantillas Jinja2
│   │   ├── base_template.html  # Layout base (head, nav, main, footer)
│   │   ├── index.html
│   │   ├── profile_user.html
│   │   ├── update_car.html
│   │   └── car_detail.html
│   └── static/                 # Archivos estáticos CSS / imágenes / uploads
│       ├── base-css.css
│       ├── profile_user.css
│       ├── upadte_car.css      # (revisar posible typo: update_car.css)
│       ├── car_detail.css
│       ├── index.css
│       └── images/
│           └── carro.png
├── migrations/                 # (si usas Flask-Migrate)
├── .env                        # Variables de entorno (DB, SECRET_KEY)
├── requirements.txt
└── README.md
