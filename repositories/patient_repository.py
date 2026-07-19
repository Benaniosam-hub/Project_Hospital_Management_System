# repositories/patient_repository.py
from repositories.base_repository import BaseRepository

class PatientRepository(BaseRepository):

    async def create_patient(self, patient_data):
        """Inserts a clean patient registration into the database."""
        query = """
            INSERT INTO patients (first_name, last_name, gender, date_of_birth, phone, blood_group, patient_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING patient_id, first_name, last_name, patient_type;
        """
        params = (
            patient_data['first_name'],
            patient_data['last_name'],
            patient_data['gender'],
            patient_data['date_of_birth'],
            patient_data['phone'],
            patient_data.get('blood_group'),
            patient_data.get('patient_type', 'Outpatient')  # Default to Outpatient
        )
        return await self.fetch_one(query, params)

    async def get_all_patients(self):
        """Retrieves all active patient records from the hospital database."""
        query = "SELECT * FROM patients WHERE is_active = TRUE ORDER BY patient_id DESC;"
        return await self.fetch_all(query)