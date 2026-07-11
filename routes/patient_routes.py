from flask import Blueprint
from controllers.patient_controller import register_patient_controller, get_patients_controller

patient_bp = Blueprint('patient_bp',__name__)

patient_bp.route('/register', methods=['POST'])(register_patient_controller)
patient_bp.route('/',methods= ['GET'])(get_patients_controller)