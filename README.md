# Flask OAuth Microservices

This project is a Python Flask-based microservices that handle OAuth authentication and user management. The services allows users to register, log in, and access protected resources using JWT (JSON Web Tokens). The project follows a clean architecture with separate modules for controllers, models, and repositories.

# Features

* User registration
* User login with password hashing
* JWT-based authentication
* Separate layers for controllers, models, and repositories
* Uses PostgreSQL as the database
* Dockerized for easy deployment
* Sample unit tests

# Basic Setup

* Python 3.x is required.
* PostgreSQL for the database
* Docker is optional but recommended for containerization.

# Commands

## Running

```console
docker-compose up -d --build
```

## Fresh Start OAuth Provider Service

```console
cd ./oauth_provider_service
docker-compose down; Remove-Item -Path .\oauth_provider_service\postgres -Force -Recurse; docker compose up -d --build; Start-Sleep -Seconds 30; flask db migrate; flask db upgrade; python app.py
```

## Running Unit Test

```console
cd ./oauth_provider_service
python -m unittest controllers.auth_controller_test
```
