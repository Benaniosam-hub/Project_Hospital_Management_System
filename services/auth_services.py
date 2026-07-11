# services/auth_services.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
import jwt
import datetime
from repositories.staff_repository import StaffRepository

class AuthService:
    def __init__(self):
        self.staff_repo = StaffRepository()

    def register_user(self, data):
        """Validates duplication rules, hashes passwords, and creates a user record."""
        # Check if username already exists
        existing_user = self.staff_repo.find_by_username(data['username'])
        if existing_user:
            return {"error": "Username is already registered"}, 400

        # Securely hash password
        hashed_password = generate_password_hash(data['password'])
        
        staff_payload = {
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "username": data['username'],
            "password": hashed_password,
            "email": data['email'],
            "role": data['role'],
            "specialization": data.get('specialization')
        }

        new_user = self.staff_repo.create_staff(staff_payload)
        return {"status": "success", "message": "Staff registered successfully", "data": new_user}, 201

    def login_user(self, username, password):
        """Verifies credentials and issues a secure JWT access token."""
        user = self.staff_repo.find_by_username(username)
        if not user or not check_password_hash(user['password'], password):
            return {"error": "Invalid username or password credentials"}, 401

        # Generate JWT Token valid for the timeframe specified in config
        token_payload = {
            "staff_id": user['staff_id'],
            "role": user['role'],
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=int(current_app.config['JWT_ACCESS_TOKEN_EXPIRES']))
        }
        
        token = jwt.encode(token_payload, current_app.config['JWT_SECRET_KEY'], algorithm="HS256")
        
        return {
            "status": "success",
            "token": token,
            "user": {
                "staff_id": user['staff_id'],
                "username": user['username'],
                "role": user['role']
            }
        }, 200