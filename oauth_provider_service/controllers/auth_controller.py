from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.user_model import UserModel
from repositories.user_repository import UserRepository
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user.

    Expects JSON data with 'username' and 'password'.
    If the username already exists, returns a 400 error.
    Saves the new user and returns a success message.
    """
    data = request.json

    if UserRepository.find_by_username(data['username']):
        return jsonify({'message': 'User Already Exists'}), 400

    hashed_password = generate_password_hash(data['password'])
    user = UserModel(username=data['username'], password=hashed_password)
    UserRepository.save(user)

    return jsonify({'message': 'User Registered Successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Log in a user and create an access token.

    Expects JSON data with 'username' and 'password'.
    If the credentials are valid, returns a JWT access token.
    If invalid, returns a 401 error with a message.
    """
    data = request.json
    user = UserRepository.find_by_username(data['username'])

    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token)

    return jsonify({'message': 'Invalid Credentials'}), 401
