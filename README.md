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

5. List routes
| **Ruta**                   | **Método(s)** | **Descripción**                                                                                                                 |
| -------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `/`                        | `GET`         | Página principal. Muestra todos los autos si el usuario no ha iniciado sesión, o todos excepto los suyos si ha iniciado sesión. |
| `/login`                   | `GET`, `POST` | Muestra el formulario de inicio de sesión y autentica al usuario.                                                               |
| `/signup`                  | `GET`, `POST` | Muestra el formulario de registro y crea un nuevo usuario.                                                                      |
| `/logout`                  | `GET`         | Cierra la sesión actual y redirige al inicio.                                                                                   |
| `/profile`                 | `GET`, `POST` | Página del perfil del usuario. Permite ver y añadir autos propios.                                                              |
| `/my_cars`                 | `GET`         | Muestra los autos agregados por el usuario autenticado.                                                                         |
| `/add_car`                 | `GET`, `POST` | Permite añadir un nuevo auto al perfil del usuario.                                                                             |
| `/car/<slug>`              | `GET`         | Muestra el detalle de un auto específico. También sugiere autos similares por marca.                                            |
| `/update_car/<int:car_id>` | `GET`, `POST` | Permite actualizar la información de un auto existente. Solo el propietario puede hacerlo.                                      |
| `/delete_car/<int:car_id>` | `POST`        | Elimina un auto existente. Solo el propietario puede eliminarlo.                                                                |

