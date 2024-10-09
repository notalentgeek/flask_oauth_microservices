import requests
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

company_a_bp = Blueprint('company_a', __name__)


@company_a_bp.route('/resource', methods=['GET'])
@jwt_required()
def access_resource():
    """
    Protected endpoint to access Company A's resources.

    This endpoint requires a valid JWT token to access. It returns
    a message indicating access to Company A's resource.
    """
    current_user = get_jwt_identity()

    return jsonify({'message': f'Accessed Company A resource for user: {current_user}'})


@company_a_bp.route('/call-company-b', methods=['GET'])
@jwt_required()
def call_company_b():
    """
    Protected endpoint to call an endpoint in Company B's service.

    This endpoint requires a valid JWT token to access. It retrieves the current JWT
    and makes a request to Company B's resource endpoint with that JWT.
    """
    # Get the Authorization header
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({"msg": "Missing Authorization Header"}), 401

    # The JWT Token Is Usually in the Format `Bearer <JWT>`
    try:
        # Split on whitespace and get the second part (JWT)
        jwt_token = auth_header.split()[1]
    except IndexError:
        return jsonify({"msg": "Invalid Authorization Header Format"}), 401

    # Directly Use the URL of Company B's Resource Endpoint
    # company_b_url = 'http://localhost:5002/resource'
    company_b_url = 'http://company-b-service:5000/resource'

    headers = {'Authorization': f'Bearer {jwt_token}'}

    print(headers)

    try:
        # Make an Authenticated Request to Company B
        response = requests.get(company_b_url, headers=headers)

        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({'error': 'Failed to Reach Company B', 'Details': str(e)}), 500
