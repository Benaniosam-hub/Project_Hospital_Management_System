# repositories/appointment_repository.py
from repositories.base_repository import BaseRepository

class AppointmentRepository(BaseRepository):

    async def schedule_appointment(self, appt_data):
        """Creates an appointment slot by letting PostgreSQL automatically parse the datetime strings."""
        query = """
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status, reason)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING appointment_id, patient_id, doctor_id, appointment_date;
        """
        params = (
            appt_data['patient_id'],
            appt_data['doctor_id'],
            appt_data['appointment_date'],
            appt_data['appointment_time'],
            appt_data.get('status', 'Scheduled'),
            appt_data.get('reason')
        )
        return await self.fetch_one(query, params)

    async def get_doctor_appointments(self, doctor_id):
        """Retrieves appointments by matching doctor_id and joining staff/patients tables."""
        query = """
            SELECT a.appointment_id,
                   a.appointment_date::text,
                   a.appointment_time::text,
                   a.status,
                   a.reason,
                   s.first_name as doctor_first,
                   s.last_name as doctor_last,
                   p.first_name as patient_first,
                   p.last_name as patient_last
            FROM appointments a
            JOIN staff s ON a.doctor_id = s.staff_id
            JOIN patients p ON a.patient_id = p.patient_id
            WHERE a.doctor_id = $1
            ORDER BY a.appointment_date ASC, a.appointment_time ASC;
        """
        return await self.fetch_all(query, (doctor_id,))