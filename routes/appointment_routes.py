# routes/appointment_routes.py
from flask import Blueprint
from controllers.appointment_controller import book_appointment_controller, get_doctor_schedule_controller

appointment_bp = Blueprint('appointment_bp', __name__)

appointment_bp.route('/book', methods=['POST'])(book_appointment_controller)
appointment_bp.route('/doctor/<int:doctor_id>', methods=['GET'])(get_doctor_schedule_controller)