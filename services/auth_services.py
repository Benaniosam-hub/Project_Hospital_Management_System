# services/auth_services.py
import os
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from repositories.staff_repository import StaffRepository

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-default-secret-key')

class AuthService:
    def __init__(self):
        self.staff_repo = StaffRepository()

    async def register_user(self, data):
        """Validates duplication rules, hashes passwords, and creates a user record."""
        # Check if username already exists
        existing_user = await self.staff_repo.find_by_username(data['username'])
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

        new_user = await self.staff_repo.create_staff(staff_payload)
        return {"status": "success", "message": "Staff registered successfully", "data": new_user}, 201

    async def login_user(self, username, password):
        """Verifies credentials and issues a secure JWT access token."""
        user = await self.staff_repo.find_by_username(username)
        if not user or not check_password_hash(user['password'], password):
            return {"error": "Invalid username or password credentials"}, 401

        # Generate JWT Token valid for the timeframe specified in config
        token_payload = {
            "staff_id": user['staff_id'],
            "role": user['role'],
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)
        }
        
        token = jwt.encode(token_payload, JWT_SECRET_KEY, algorithm="HS256")
        
        return {
            "status": "success",
            "token": token,
            "user": {
                "staff_id": user['staff_id'],
                "username": user['username'],
                "role": user['role']
            }
        }, 200