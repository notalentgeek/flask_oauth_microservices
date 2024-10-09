import unittest

from app import db
from controllers.auth_controller import auth_bp
from flask import Flask
from flask_jwt_extended import JWTManager


class AuthTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        # Use an In-Memory Database For Tests
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['JWT_SECRET_KEY'] = 'your_secret_key'

        self.jwt = JWTManager(self.app)
        self.app.register_blueprint(auth_bp)

        self.client = self.app.test_client()

        # Initialize the Database And Create Tables For Testing
        with self.app.app_context():
            db.init_app(self.app)  # Initialize `db` With the App
            db.create_all()  # Create Tables In the In-Memory Database

    def test_register_user_success(self):
        # Send a POST Request to Register a New User
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Verify the Registration Response
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'User Registered Successfully', response.data)

    def test_register_user_already_exists(self):
        # Register a User For the First Time
        self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Attempt to Register the Same User Again, Expecting a Failure
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'User Already Exists', response.data)

    def test_login_success(self):
        # Register a User First to Set Up For Login
        self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Send a POST Request to Login With Valid Credentials
        response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Verify the Login Response Contains an Access Token
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'access_token', response.data)

    def test_login_invalid_credentials(self):
        # Attempt to Login Without Registering Any User
        response = self.client.post('/login', json={
            'username': 'nonexistentuser',
            'password': 'wrongpassword'
        })

        # Verify the Login Response Indicates Invalid Credentials
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid Credentials', response.data)


if __name__ == '__main__':
    unittest.main()
