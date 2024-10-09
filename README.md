# Flask OAuth Microservices

This project is a Python Flask-based microservice that handles OAuth authentication and user management. The service allows users to register, log in, and access protected resources using JWT (JSON Web Tokens). The project follows a clean architecture with separate modules for controllers, models, and repositories.

As of 15:00, this repository is still under development.

# Features

* User registration
* User login with password hashing (using bcrypt)
* JWT-based authentication
* Separate layers for controllers, models, and repositories
* Uses PostgreSQL as the database
* Dockerized for easy deployment

# Basic Setup

* Python 3.x is required.
* PostgreSQL for the database
* Docker is optional but recommended for containerization.

# Commands

## Clean-Up and Setup

```console
docker-compose down; Remove-Item -Path .\postgres -Force -Recurse; docker compose up -d --build; Start-Sleep -Seconds 30; flask db migrate; flask db upgrade; python app.py
```
