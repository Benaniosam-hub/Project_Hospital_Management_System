from flask import Blueprint
from controllers.inpatient_controller import add_room_controller, get_rooms_controller, admit_patient_controller

inpatient_bp = Blueprint('inpatient_bp', __name__)

inpatient_bp.route('/rooms', methods=['POST'])(add_room_controller)
inpatient_bp.route('/rooms', methods=['GET'])(get_rooms_controller)
inpatient_bp.route('/admit', methods=['POST'])(admit_patient_controller)
