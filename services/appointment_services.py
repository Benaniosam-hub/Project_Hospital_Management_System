from repositories.appointment_repository import AppointmentRepository

class AppointmentService:
    def __init__(self):
        self.appointment_repo = AppointmentRepository()

    def create_appointment(self, data):
        """Dispatches appointment scheduling payloads directly to the database layer."""
        new_appointment = self.appointment_repo.schedule_appointment(data)
        return {"status": "success", "message": "Appointment scheduled successfully", "data": new_appointment}, 201

    def list_doctor_schedule(self, doctor_id):
        """Fetches the structured upcoming line-up list for a doctor."""
        schedule = self.appointment_repo.get_doctor_appointments(doctor_id)
        return {"status": "success", "doctor_id": doctor_id, "data": schedule}, 200