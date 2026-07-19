from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.connection import close_db_connection
from routes.auth_routes import auth_bp
from routes.patient_routes import patient_bp
from routes.inpatient_routes import inpatient_bp
from routes.appointment_routes import appointment_bp

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    close_db_connection

app = FastAPI(
    title= "Hospital Management System API",
    version="1.0.0"
) 

app.include_router(auth_bp, prefix='/api/v1/auth')
app.include_router(patient_bp, prefix='/api/v1/patients')
app.include_router(inpatient_bp, prefix='/api/v1/inpatient')
app.include_router(appointment_bp, prefix='/api/v1/appointments')

@app.get("/")
async def index():
    return{"status": "success",
           "message": "HMS API Live. Go to /docs for Swagger documentation."
           }, 200

