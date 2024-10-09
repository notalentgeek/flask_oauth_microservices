from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

user_bp = Blueprint('user', __name__)

# Protected user info endpoint


@user_bp.route('/info', methods=['GET'])
@jwt_required()
def userinfo():
    current_user = get_jwt_identity()
    return jsonify({'user': current_user})
