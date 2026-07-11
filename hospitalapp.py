from flask import Flask
from config import Config
from database.connection import close_db_connection
from routes.auth_routes import auth_bp
from flasgger import Swagger
from routes.patient_routes import patient_bp
from routes.inpatient_routes import inpatient_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config['SWAGGER'] = {
        'title': 'Hospital Management System API',
        'uiversion': 3
    }
    Swagger(app)

    app.teardown_appcontext(close_db_connection)

    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')

    app.register_blueprint(patient_bp, url_prefix='/api/v1/patients')

    app.register_blueprint(inpatient_bp, url_prefix='/api/v1/inpatient')

    app.route('/')
    def index():
        return{"status": "success", "message": "HMS API Live. Go to /apidocs/ for Swagger documentation."}, 200
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000) 