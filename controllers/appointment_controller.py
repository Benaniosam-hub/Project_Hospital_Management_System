# controllers/appointment_controller.py
from flask import request, jsonify
from services.appointment_services import AppointmentService

appointment_service = AppointmentService()

def book_appointment_controller():
    """
    Schedule a New Patient Appointment
    ---
    tags:
      - Appointments & Schedules
    parameters:
      - name: body
        in: body
        required: true
        schema:
          required:
            - patient_id
            - doctor_id
            - appointment_date
          properties:
            patient_id:
              type: integer
              example: 1
            doctor_id:
              type: integer
              example: 1
            appointment_date:
              type: string
              example: "2026-08-15 10:30:00"
            reason:
              type: string
              example: "Routine cardiac checkup evaluation follow-up"
    responses:
      201:
        description: Appointment logged successfully
    """
    data = request.get_json()
    required = ['patient_id', 'doctor_id', 'appointment_date']
    if not data or not all(k in data for k in required):
        return jsonify({"error": "Missing essential calendar tokens"}), 400
        
    result, status_code = appointment_service.create_appointment(data)
    return jsonify(result), status_code

def get_doctor_schedule_controller(doctor_id):
    """
    Get Upcoming Schedule Matrix For A Doctor
    ---
    tags:
      - Appointments & Schedules
    parameters:
      - name: doctor_id
        in: path
        type: integer
        required: true
        description: The unique ID number of the specific physician
    responses:
      200:
        description: Returns a list of appointments for the doctor
    """
    result, status_code = appointment_service.list_doctor_schedule(doctor_id)
    return jsonify(result), status_code