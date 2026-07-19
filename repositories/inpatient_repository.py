# repositories/inpatient_repository.py
from repositories.base_repository import BaseRepository

class InpatientRepository(BaseRepository):

    async def create_room(self, room_data):
        """Adds a new physical hospital room into the inventory system."""
        query = """
            INSERT INTO rooms (room_number, type, total_beds, available_beds, price_per_day)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING room_id, room_number, available_beds;
        """
        params = (
            room_data['room_number'],
            room_data['type'],
            room_data['total_beds'],
            room_data['total_beds'],  # Initially available_beds equals total_beds
            room_data['price_per_day']
        )
        return await self.fetch_one(query, params)

    async def get_all_rooms(self):
        """Fetches status of all hospital rooms."""
        query = "SELECT * FROM rooms ORDER BY room_number ASC;"
        return await self.fetch_all(query)

    async def check_room_availability(self, room_id):
        """Verifies if a specific room has free beds available."""
        query = "SELECT available_beds FROM rooms WHERE room_id = %s;"
        result = await self.fetch_one(query, (room_id,))
        return result['available_beds'] if result else 0

    async def create_admission(self, admission_data):
        """Inserts a new patient admission record and decreases available beds."""
        # 1. Insert the admission entry
        query_admission = """
            INSERT INTO admissions (patient_id, room_id, admission_date, reason)
            VALUES (%s, %s, %s, %s)
            RETURNING admission_id, patient_id, room_id, status;
        """
        params_admission = (
            admission_data['patient_id'],
            admission_data['room_id'],
            admission_data['admission_date'],
            admission_data['reason']
        )
        new_admission = await self.fetch_one(query_admission, params_admission)

        # 2. Update room availability: decrease available_beds by 1
        query_room_update = """
            UPDATE rooms
            SET available_beds = available_beds - 1
            WHERE room_id = %s
            RETURNING available_beds;
        """
        await self.fetch_one(query_room_update, (admission_data['room_id'],))

        return new_admission