from repositories.inpatient_repository import InpatientRepository
from datetime import datetime

class InpatientService:
    def __init__(self):
        self.inpatient_repo = InpatientRepository()

    def add_room(self, data):
        """Directly forwards room setup details to the repository layer."""
        new_room = self.inpatient_repo.create_room(data)
        return {"status": "success", "message": "Room added successfully", "data": new_room}, 201

    def list_rooms(self):
        """Retrieves a directory of all rooms."""
        rooms = self.inpatient_repo.get_all_rooms()
        return {"status": "success", "data": rooms}, 200

    def admit_patient(self, data):
        """Checks structural occupancy and registers a patient admission stay."""
        room_id = data.get('room_id')
        
        # Guard clause: Check if room has open capacity
        available_beds = self.inpatient_repo.check_room_availability(room_id)
        if available_beds <= 0:
            return {"error": "Cannot admit patient. Selected room is completely full."}, 400

        # Set default admission date to now if not provided
        if not data.get('admission_date'):
            data['admission_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_admission = self.inpatient_repo.create_admission(data)
        return {"status": "success", "message": "Patient admitted successfully", "data": new_admission}, 201