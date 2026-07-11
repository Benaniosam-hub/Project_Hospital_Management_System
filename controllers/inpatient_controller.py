from flask import request, jsonify
from services.inpatient_services import InpatientService

inpatient_service = InpatientService()

def add_room_controller():
    """
    Add a New Hospital Room
    ---
    tags:
      - Inpatient Facility
    parameters:
      - name: body
        in: body
        required: true
        schema:
          required:
            - room_number
            - type
            - total_beds
            - price_per_day
          properties:
            room_number:
              type: string
              example: "101-A"
            type:
              type: string
              enum: ['General', 'Semi-Private', 'Private', 'ICU']
              example: "General"
            total_beds:
              type: integer
              example: 4
            price_per_day:
              type: number
              example: 150.00
    responses:
      201:
        description: Room provisioned successfully
    """
    data = request.get_json()
    required = ['room_number', 'type', 'total_beds', 'price_per_day']
    if not data or not all(k in data for k in required):
        return jsonify({"error": "Missing essential room structural keys"}), 400
        
    result, status_code = inpatient_service.add_room(data)
    return jsonify(result), status_code

def get_rooms_controller():
    """
    Get All Rooms Directory Status
    ---
    tags:
      - Inpatient Facility
    responses:
      200:
        description: Returns status overview list of all rooms
    """
    result, status_code = inpatient_service.list_rooms()
    return jsonify(result), status_code

def admit_patient_controller():
    """
    Admit a Patient to a Room
    ---
    tags:
      - Inpatient Facility
    parameters:
      - name: body
        in: body
        required: true
        schema:
          required:
            - patient_id
            - room_id
            - reason
          properties:
            patient_id:
              type: integer
              example: 1
            room_id:
              type: integer
              example: 1
            reason:
              type: string
              example: "Recovering from appendectomy surgery observations"
    responses:
      201:
        description: Patient checked in and bed allocated successfully
      400:
        description: Selected room is full or inputs invalid
    """
    data = request.get_json()
    required = ['patient_id', 'room_id', 'reason']
    if not data or not all(k in data for k in required):
        return jsonify({"error": "Missing essential admission details"}), 400
        
    result, status_code = inpatient_service.admit_patient(data)
    return jsonify(result), status_code