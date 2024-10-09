from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

user_bp = Blueprint('user', __name__)


@user_bp.route('/info', methods=['GET'])
@jwt_required()
def info():
    """
    Protected endpoint to retrieve the current user's information.

    This endpoint requires a valid JWT token to access. It returns
    the username of the currently authenticated user.
    """
    current_user = get_jwt_identity()
    return jsonify({'user': current_user})
