from repositories.appointment_repository import AppointmentRepository
from repositories.staff_repository import StaffRepository

class AppointmentService:
    def __init__(self):
        self.appointment_repo = AppointmentRepository()
        self.staff_repo = StaffRepository()

    async def create_appointment(self, data):
        """Dispatches appointment scheduling payloads after validating the physician's role."""
        doctor_id = data.get('doctor_id')
        
        # 1. Fetch the staff record to verify who this ID belongs to
        staff_member = await self.staff_repo.find_by_id(doctor_id)
        
        # 2. If the staff ID does not exist at all, reject the booking with a 404
        if not staff_member:
            return {
                "status": "error",
                "message": f"Cannot book appointment. No staff record found with ID {doctor_id}."
            }, 404
            
        # 3. If they exist but are NOT a doctor, reject the booking with a 400 Bad Request!
        if staff_member.get('role') != 'doctor':
            return {
                "status": "error",
                "message": f"Booking Denied. Staff ID {doctor_id} belongs to a {staff_member.get('role')} ({staff_member.get('first_name')}), not a physician."
            }, 400

        # 4. If all validations clear, dispatch to database
        new_appointment = await self.appointment_repo.schedule_appointment(data)
        return {
            "status": "success", 
            "message": "Appointment scheduled successfully", 
            "data": new_appointment
        }, 201

    async def list_doctor_schedule(self, doctor_id):
        """Fetches the structured upcoming line-up list for a doctor after validation."""
        # 1. Fetch the staff record using the staff repo you just initialized on line 7
        staff_member = await self.staff_repo.find_by_id(doctor_id)
        
        # 2. If no record exists at all in the staff table, return a 404 error
        if not staff_member:
            return {
                "status": "error",
                "message": f"No staff record found with ID {doctor_id}."
            }, 404
            
        # 3. If the user exists but isn't a doctor, explicitly throw a 400 error message
        if staff_member.get('role') != 'doctor':
            return {
                "status": "error",
                "message": f"Access Denied. Staff member '{staff_member.get('first_name')}' is registered as a {staff_member.get('role')}, not a doctor."
            }, 400

        # 4. If they pass the check, fetch and return the schedule matrix normally
        schedule = await self.appointment_repo.get_doctor_appointments(doctor_id)
        return {
            "status": "success", 
            "doctor_id": doctor_id, 
            "data": schedule
        }, 200