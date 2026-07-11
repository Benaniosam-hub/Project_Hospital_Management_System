# controllers/auth_controller.py
from flask import request, jsonify
from services.auth_services import AuthService

auth_service = AuthService()

def register_controller():
    """
    Staff Registration Endpoint
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: StaffRegistration
          required:
            - first_name
            - last_name
            - username
            - password
            - email
            - role
          properties:
            first_name:
              type: string
              example: John
            last_name:
              type: string
              example: Doe
            username:
              type: string
              example: johndoe
            password:
              type: string
              example: Password123!
            email:
              type: string
              example: john@hospital.com
            role:
              type: string
              enum: ['admin', 'doctor', 'nurse', 'receptionist', 'pharmacist']
              example: admin
            specialization:
              type: string
              example: Cardiology
    responses:
      201:
        description: Staff registered successfully
      400:
        description: Missing essential fields or username taken
    """
    data = request.get_json()
    required_fields = ['first_name', 'last_name', 'username', 'password', 'email', 'role']
    if not data or not all(k in data for k in required_fields):
        return jsonify({"error": "Missing essential payload fields"}), 400
        
    result, status_code = auth_service.register_user(data)
    return jsonify(result), status_code


def login_controller():
    """
    Staff Login Endpoint
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: StaffLogin
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: johndoe
            password:
              type: string
              example: Password123!
    responses:
      200:
        description: Login successful, JWT token returned
      401:
        description: Invalid credentials
    """
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password fields"}), 400
        
    result, status_code = auth_service.login_user(data['username'], data['password'])
    return jsonify(result), status_code