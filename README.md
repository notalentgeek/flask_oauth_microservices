# Flask OAuth Microservices

This project is a Python-based Flask microservice architecture for handling OAuth authentication and user management. It enables user registration, login, and secure access to protected resources using JSON Web Tokens (JWT). The project adheres to clean architecture principles with distinct layers for controllers, models, and repositories, ensuring maintainability and scalability.

## Features

- **User Registration** : Secure user registration with password hashing.
- **User Authentication** : Login via JWT-based authentication.
- **JWT Support** : Token-based authentication for protected routes.
- **Clean Architecture** : Separation of concerns with controllers, models, and repositories.
- **PostgreSQL Integration** : Uses PostgreSQL as the primary database.
- **Docker Support** : Fully Dockerized for easy deployment and development.
- **Unit Testing** : Includes sample unit tests for key components.

## Prerequisites

- **Python 3.x** : Ensure you have Python 3.x installed
- **PostgreSQL** : Requires a running PostgreSQL instance
- **Docker** : (Optional but recommended) for containerized deployment and development

## Setup

Skip to no. 4 if you have Docker installed.

1. **Clone the Repository** :

   ```bash
   git clone https://github.com/yourusername/flask-oauth-microservices.git
   cd flask-oauth-microservices
   ```

2. **Environment Setup**:
   - Install the required Python dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Configure the environment variables in a `.env` file for database and JWT settings.

3. **Database Setup**:
   - Ensure that PostgreSQL is running and properly configured.
   - Run database migrations:

     ```bash
     flask db migrate
     flask db upgrade
     ```

4. **Running the Application**:
   - Without Docker:

     ```bash
     python app.py
     ```

   - With Docker (Recommended):

     ```bash
     docker-compose up -d --build
     ```

## Postman Collection

To interact with the API using Postman, follow these steps to import the provided Postman collection:

1. **Download Postman**: [https://www.postman.com/](https://www.postman.com/)
2. **Import the Collection**:
   - Open Postman and click **Import**.
   - Choose **Import File** and select the `postman_collection.json` file from this repository.
   - Alternatively, if the collection is hosted online, select **Link** and paste the URL to the collection.
3. **Access API Endpoints**: After importing, the collection will be available under the **Collections** tab in Postman, ready for use.

The Postman collection file is located in this repository at `./postman_collection.json`.

## Commands

### Fresh Start (OAuth Provider Service)

For development purposes, you can reset and rebuild the OAuth provider service using the following:

```bash
cd ./oauth_provider_service
docker-compose down
Remove-Item -Path .\oauth_provider_service\postgres -Force -Recurse
docker-compose up -d --build
Start-Sleep -Seconds 30
flask db migrate
flask db upgrade
python app.py
```

### Running Unit Tests

Install the requirements_test.txt first.

```bash
pip install -r requirements_test.txt
```

To run the unit tests:

```bash
cd ./oauth_provider_service
python -m unittest controllers.auth_controller_test
```
