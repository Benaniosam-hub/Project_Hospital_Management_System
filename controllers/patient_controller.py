# controllers/patient_controller.py
from flask import request, jsonify
from services.patient_services import PatientService

patient_service = PatientService()

def register_patient_controller():
    """
    Register a New Patient
    ---
    tags:
      - Patients
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: PatientRegistration
          required:
            - first_name
            - last_name
            - gender
            - date_of_birth
            - phone
          properties:
            first_name:
              type: string
              example: Jane
            last_name:
              type: string
              example: Smith
            gender:
              type: string
              enum: ['Male', 'Female', 'Other']
              example: Female
            date_of_birth:
              type: string
              example: "24-05-2002"
            phone:
              type: string
              example: "9003572015"
            blood_group:
              type: string
              example: "O+"
            patient_type:
              type: string
              enum: ['Inpatient', 'Outpatient']
              example: Outpatient
    responses:
      201:
        description: Patient added successfully
      400:
        description: Invalid request payload
    """
    data = request.get_json()
    required = ['first_name', 'last_name', 'gender', 'date_of_birth', 'phone']
    if not data or not all(k in data for k in required):
        return jsonify({"error": "Missing essential personal details fields"}), 400
        
    result, status_code = patient_service.register_patient(data)
    return jsonify(result), status_code

def get_patients_controller():
    """
    Retrieve All Patient Directory Records
    ---
    tags:
      - Patients
    responses:
      200:
        description: Returns a list of all active patients
    """
    result, status_code = patient_service.list_patients()
    return jsonify(result), status_code