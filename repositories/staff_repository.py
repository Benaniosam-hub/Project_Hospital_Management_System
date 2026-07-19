# repositories/staff_repository.py
from repositories.base_repository import BaseRepository

class StaffRepository(BaseRepository):

    async def create_staff(self, staff_data):
        """Inserts a new staff member into the database asynchronously."""
        query = """
            INSERT INTO staff (first_name, last_name, username, password, email, role, specialization)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING staff_id, username, email, role;
        """
        params = (
            staff_data['first_name'],
            staff_data['last_name'],
            staff_data['username'],
            staff_data['password'],  # Securely hashed by the service layer
            staff_data['email'],
            staff_data['role'],
            staff_data.get('specialization')
        )
        return await self.fetch_one(query, params)

    async def find_by_username(self, username):
        """Finds an active staff member by their unique username for login validation."""
        query = "SELECT * FROM staff WHERE username = %s AND is_active = TRUE;"
        return await self.fetch_one(query, (username,))

    async def find_by_id(self, staff_id):
        """Finds a staff profile by ID to verify their active role status."""
        query = "SELECT staff_id, first_name, last_name, role FROM staff WHERE staff_id = %s"
        return await self.fetch_one(query, (staff_id,))