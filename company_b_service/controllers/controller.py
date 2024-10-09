from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

company_b_bp = Blueprint('company_b', __name__)


@company_b_bp.route('/resource', methods=['GET'])
@jwt_required()
def access_resource():
    """
    Protected endpoint to access Company B's resources.

    This endpoint requires a valid JWT token to access. It returns
    a message indicating access to Company B's resource.
    """
    current_user = get_jwt_identity()

    return jsonify({'message': f'Accessed Company B resource for user: {current_user}'})
