# Hospital Management System API

A comprehensive RESTful API for managing hospital operations including patient management, inpatient services, appointments, and authentication.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Running the Application](#running-the-application)
- [Swagger UI](#swagger-ui)
- [Contributing](#contributing)

---

## 🏥 Overview

The Hospital Management System API is built with **Flask** and provides a complete backend solution for hospital operations. It handles:

- **Patient Management**: Register, update, and manage patient information
- **Inpatient Services**: Manage hospital admissions and inpatient records
- **Appointments**: Schedule and manage medical appointments
- **Authentication**: Secure JWT-based authentication for users

---

## ✨ Features

- ✅ RESTful API architecture
- ✅ JWT-based authentication & authorization
- ✅ PostgreSQL database integration
- ✅ Automatic Swagger/OpenAPI documentation
- ✅ Error handling and validation
- ✅ Environment-based configuration
- ✅ Database connection pooling

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Flask 2.x |
| **API Documentation** | Flasgger (Swagger/OpenAPI) |
| **Database** | PostgreSQL |
| **Authentication** | JWT (JSON Web Tokens) |
| **Language** | Python 3.x |
| **Environment Management** | python-dotenv |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **PostgreSQL 10+**
- **pip** (Python package manager)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Benaniosam-hub/Project_Hospital_Management_System.git
cd Project_Hospital_Management_System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create PostgreSQL Database

```bash
createdb hospital_db
```

Or using PostgreSQL CLI:

```sql
CREATE DATABASE hospital_db;
```

---

## ⚙️ Configuration

### 1. Environment Variables (.env file)

Create a `.env` file in the root directory with the following variables:

```env
# Secret Keys
SECRET_KEY=your_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_key_here

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hospital_db
DB_USER=postgres
DB_PASSWORD=your_db_password

# Flask Configuration
FLASK_DEBUG=True
```

### 2. Configuration File (config.py)

The configuration is automatically loaded from environment variables:

```python
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','')
    DEBUG = os.environ.get('FLASK_DEBUG', True)
    
    # Database
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_NAME = os.environ.get('DB_NAME','hospital_db')
    DB_USER = os.environ.get('DB_USER','postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_PORT = os.environ.get('DB_PORT','5432')
    
    # JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY','')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
```

---

## 📁 Project Structure

```
Project_Hospital_Management_System/
├── hospitalapp.py              # Application entry point
├── config.py                   # Configuration settings
├── requirements.txt            # Project dependencies
├── .env                       # Environment variables
├── .gitignore                 # Git ignore rules
│
├── controllers/               # Business logic layer
│   ├── patient_controller.py
│   ├── inpatient_controller.py
│   ├── appointment_controller.py
│   └── auth_controller.py
│
├── routes/                    # API routes/endpoints
│   ├── patient_routes.py
│   ├── inpatient_routes.py
│   ├── appointment_routes.py
│   └── auth_routes.py
│
├── services/                  # Service layer for business operations
│   ├── patient_service.py
│   ├── inpatient_service.py
│   ├── appointment_service.py
│   └── auth_service.py
│
├── repositories/              # Data access layer
│   ├── patient_repository.py
│   ├── inpatient_repository.py
│   ├── appointment_repository.py
│   └── auth_repository.py
│
├── database/                  # Database configuration
│   ├── connection.py         # Database connection management
│   └── models.py             # Database models/schemas
│
└── utils/                     # Utility functions
    ├── validators.py         # Input validation
    ├── decorators.py         # Custom decorators
    └── helpers.py            # Helper functions
```

---

## 📊 Database Schema

### Tables Overview

#### 1. **Users Table**
Stores user account information for authentication.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,  -- 'admin', 'doctor', 'nurse', 'receptionist'
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 2. **Patients Table**
Stores patient information and medical history.

```sql
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE,
    phone VARCHAR(20),
    date_of_birth DATE,
    gender VARCHAR(10),  -- 'M', 'F', 'Other'
    address TEXT,
    blood_group VARCHAR(5),  -- 'A+', 'O-', etc.
    medical_history TEXT,
    allergies TEXT,
    emergency_contact VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    insurance_number VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 3. **Appointments Table**
Manages patient appointments with doctors.

```sql
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    doctor_id INTEGER NOT NULL REFERENCES users(id),
    appointment_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER DEFAULT 30,
    reason_for_visit TEXT,
    status VARCHAR(50) DEFAULT 'scheduled',  -- 'scheduled', 'completed', 'cancelled', 'no_show'
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (patient_id, appointment_date)
);
```

#### 4. **Inpatients Table**
Manages hospital admissions and inpatient records.

```sql
CREATE TABLE inpatients (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    admission_date TIMESTAMP NOT NULL,
    discharge_date TIMESTAMP,
    room_number VARCHAR(50),
    bed_number VARCHAR(50),
    ward_name VARCHAR(100),  -- 'ICU', 'General', 'Pediatrics', etc.
    admission_reason TEXT NOT NULL,
    attending_doctor_id INTEGER NOT NULL REFERENCES users(id),
    diagnosis TEXT,
    treatment_plan TEXT,
    status VARCHAR(50) DEFAULT 'admitted',  -- 'admitted', 'discharged', 'transferred'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 5. **Medical Records Table**
Stores detailed medical records for patients.

```sql
CREATE TABLE medical_records (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    inpatient_id INTEGER REFERENCES inpatients(id),
    record_type VARCHAR(50),  -- 'lab_result', 'prescription', 'diagnosis', 'test'
    record_date TIMESTAMP NOT NULL,
    description TEXT,
    doctor_id INTEGER NOT NULL REFERENCES users(id),
    attachments TEXT,  -- JSON array of file paths
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Relationships Diagram

```
Users (1) -----> (Many) Appointments
  |
  ├---------> (Many) Inpatients
  └---------> (Many) Medical Records

Patients (1) ------> (Many) Appointments
   |
   ├-----------> (Many) Inpatients
   └-----------> (Many) Medical Records
```

---

## 📡 API Documentation

### Base URL

```
http://localhost:5000/api/v1
```

### Response Format

All API responses follow a consistent JSON format:

**Success Response (2xx):**
```json
{
    "status": "success",
    "message": "Operation completed successfully",
    "data": {
        "id": 1,
        "name": "John Doe",
        ...
    }
}
```

**Error Response (4xx, 5xx):**
```json
{
    "status": "error",
    "message": "Error description",
    "error_code": "INVALID_REQUEST",
    "details": {}
}
```

---

## 🔌 API Endpoints

### 1. Authentication Endpoints (`/api/v1/auth`)

#### Register User
```http
POST /api/v1/auth/register
Content-Type: application/json

{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "SecurePassword123!",
    "role": "doctor"
}
```

**Response (201):**
```json
{
    "status": "success",
    "message": "User registered successfully",
    "data": {
        "id": 1,
        "username": "johndoe",
        "email": "john@example.com",
        "role": "doctor"
    }
}
```

#### Login
```http
POST /api/v1/auth/login
Content-Type: application/json

{
    "email": "john@example.com",
    "password": "SecurePassword123!"
}
```

**Response (200):**
```json
{
    "status": "success",
    "message": "Login successful",
    "data": {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "token_type": "Bearer",
        "expires_in": 3600,
        "user": {
            "id": 1,
            "username": "johndoe",
            "role": "doctor"
        }
    }
}
```

#### Logout
```http
POST /api/v1/auth/logout
Authorization: Bearer {token}
```

**Response (200):**
```json
{
    "status": "success",
    "message": "Logout successful"
}
```

---

### 2. Patient Endpoints (`/api/v1/patients`)

#### Create Patient
```http
POST /api/v1/patients
Authorization: Bearer {token}
Content-Type: application/json

{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone": "+1-555-0123",
    "date_of_birth": "1990-05-15",
    "gender": "M",
    "address": "123 Main St, City, State 12345",
    "blood_group": "O+",
    "medical_history": "Hypertension, Diabetes Type 2",
    "allergies": "Penicillin, Shellfish",
    "emergency_contact": "Jane Doe",
    "emergency_contact_phone": "+1-555-0124",
    "insurance_number": "INS123456789"
}
```

**Response (201):**
```json
{
    "status": "success",
    "message": "Patient created successfully",
    "data": {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1-555-0123",
        "date_of_birth": "1990-05-15",
        "gender": "M",
        "blood_group": "O+",
        "is_active": true
    }
}
```

#### Get All Patients
```http
GET /api/v1/patients
Authorization: Bearer {token}
```

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Results per page (default: 10)
- `search`: Search by name or email

**Response (200):**
```json
{
    "status": "success",
    "message": "Patients retrieved successfully",
    "data": [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1-555-0123",
            "blood_group": "O+"
        }
    ],
    "pagination": {
        "page": 1,
        "limit": 10,
        "total": 1
    }
}
```

#### Get Patient by ID
```http
GET /api/v1/patients/{patient_id}
Authorization: Bearer {token}
```

**Response (200):**
```json
{
    "status": "success",
    "message": "Patient retrieved successfully",
    "data": {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1-555-0123",
        "date_of_birth": "1990-05-15",
        "gender": "M",
        "address": "123 Main St, City, State 12345",
        "blood_group": "O+",
        "medical_history": "Hypertension, Diabetes Type 2",
        "allergies": "Penicillin, Shellfish",
        "insurance_number": "INS123456789"
    }
}
```

#### Update Patient
```http
PUT /api/v1/patients/{patient_id}
Authorization: Bearer {token}
Content-Type: application/json

{
    "phone": "+1-555-9999",
    "medical_history": "Hypertension, Diabetes Type 2, Asthma"
}
```

**Response (200):**
```json
{
    "status": "success",
    "message": "Patient updated successfully",
    "data": { ... }
}
```

#### Delete Patient
```http
DELETE /api/v1/patients/{patient_id}
Authorization: Bearer {token}
```

**Response (200):**
```json
{
    "status": "success",
    "message": "Patient deleted successfully"
}
```

---

### 3. Inpatient Endpoints (`/api/v1/inpatient`)

#### Create Inpatient Record
```http
POST /api/v1/inpatient
Authorization: Bearer {token}
Content-Type: application/json

{
    "patient_id": 1,
    "admission_date": "2024-01-15T10:00:00Z",
    "room_number": "101",
    "bed_number": "A",
    "ward_name": "ICU",
    "admission_reason": "Acute myocardial infarction",
    "attending_doctor_id": 2,
    "diagnosis": "Heart Attack",
    "treatment_plan": "Immediate intervention required"
}
```

**Response (201):**
```json
{
    "status": "success",
    "message": "Inpatient record created successfully",
    "data": {
        "id": 1,
        "patient_id": 1,
        "admission_date": "2024-01-15T10:00:00Z",
        "room_number": "101",
        "bed_number": "A",
        "ward_name": "ICU",
        "status": "admitted"
    }
}
```

#### Get All Inpatients
```http
GET /api/v1/inpatient
Authorization: Bearer {token}
```

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Results per page (default: 10)
- `status`: Filter by status (admitted, discharged, transferred)
- `ward_name`: Filter by ward

**Response (200):**
```json
{
    "status": "success",
    "message": "Inpatients retrieved successfully",
    "data": [ ... ],
    "pagination": { ... }
}
```

#### Get Inpatient by ID
```http
GET /api/v1/inpatient/{inpatient_id}
Authorization: Bearer {token}
```

#### Update Inpatient
```http
PUT /api/v1/inpatient/{inpatient_id}
Authorization: Bearer {token}
Content-Type: application/json

{
    "diagnosis": "Updated diagnosis",
    "treatment_plan": "Updated treatment plan"
}
```

#### Discharge Patient
```http
POST /api/v1/inpatient/{inpatient_id}/discharge
Authorization: Bearer {token}
Content-Type: application/json

{
    "discharge_date": "2024-01-20T14:00:00Z",
    "discharge_summary": "Patient recovered well"
}
```

**Response (200):**
```json
{
    "status": "success",
    "message": "Patient discharged successfully",
    "data": {
        "id": 1,
        "status": "discharged",
        "discharge_date": "2024-01-20T14:00:00Z"
    }
}
```

---

### 4. Appointment Endpoints (`/api/v1/appointments`)

#### Schedule Appointment
```http
POST /api/v1/appointments
Authorization: Bearer {token}
Content-Type: application/json

{
    "patient_id": 1,
    "doctor_id": 2,
    "appointment_date": "2024-02-01T14:00:00Z",
    "duration_minutes": 30,
    "reason_for_visit": "Routine checkup"
}
```

**Response (201):**
```json
{
    "status": "success",
    "message": "Appointment scheduled successfully",
    "data": {
        "id": 1,
        "patient_id": 1,
        "doctor_id": 2,
        "appointment_date": "2024-02-01T14:00:00Z",
        "duration_minutes": 30,
        "reason_for_visit": "Routine checkup",
        "status": "scheduled"
    }
}
```

#### Get All Appointments
```http
GET /api/v1/appointments
Authorization: Bearer {token}
```

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Results per page (default: 10)
- `status`: Filter by status
- `doctor_id`: Filter by doctor
- `patient_id`: Filter by patient

#### Get Appointments for a Patient
```http
GET /api/v1/appointments?patient_id=1
Authorization: Bearer {token}
```

#### Get Appointment by ID
```http
GET /api/v1/appointments/{appointment_id}
Authorization: Bearer {token}
```

#### Update Appointment
```http
PUT /api/v1/appointments/{appointment_id}
Authorization: Bearer {token}
Content-Type: application/json

{
    "appointment_date": "2024-02-02T15:00:00Z",
    "reason_for_visit": "Follow-up consultation"
}
```

#### Cancel Appointment
```http
POST /api/v1/appointments/{appointment_id}/cancel
Authorization: Bearer {token}
Content-Type: application/json

{
    "reason": "Patient requested cancellation"
}
```

**Response (200):**
```json
{
    "status": "success",
    "message": "Appointment cancelled successfully",
    "data": {
        "id": 1,
        "status": "cancelled"
    }
}
```

#### Complete Appointment
```http
POST /api/v1/appointments/{appointment_id}/complete
Authorization: Bearer {token}
Content-Type: application/json

{
    "notes": "Patient showed good progress"
}
```

---

## 🔐 Authentication

The API uses **JWT (JSON Web Tokens)** for authentication and authorization.

### How It Works

1. **User Registration**: Create an account with username, email, and password
2. **Login**: Send credentials to receive an access token
3. **Authorization**: Include token in the `Authorization` header for protected routes
4. **Token Format**: `Authorization: Bearer {access_token}`

### JWT Token Structure

```
Header:
{
    "alg": "HS256",
    "typ": "JWT"
}

Payload:
{
    "user_id": 1,
    "username": "johndoe",
    "role": "doctor",
    "exp": 1704067200,
    "iat": 1704063600
}

Signature:
HMACSHA256(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    secret_key
)
```

### Token Expiration

- **Access Token Expires**: 3600 seconds (1 hour)
- **Token Type**: Bearer

### Protected Routes

All endpoints except `/auth/register` and `/auth/login` require valid JWT token in the `Authorization` header.

**Error Response (401 Unauthorized):**
```json
{
    "status": "error",
    "message": "Authorization required",
    "error_code": "UNAUTHORIZED"
}
```

---

## 🚀 Running the Application

### 1. Start the Development Server

```bash
# Make sure virtual environment is activated
python hospitalapp.py
```

The application will start on `http://localhost:5000`

### 2. Access the API

```
Base URL: http://localhost:5000/api/v1
Health Check: http://localhost:5000/
```

### 3. View Swagger Documentation

```
http://localhost:5000/apidocs/
```

---

## 📚 Swagger UI

The application includes **Flasgger** integration for automatic API documentation generation.

### Features

- ✅ Interactive API testing interface
- ✅ Automatic endpoint documentation
- ✅ Try-it-out functionality
- ✅ Response examples and schemas
- ✅ Authentication token support

### Accessing Swagger UI

1. Start the application
2. Navigate to: `http://localhost:5000/apidocs/`
3. Authorize with JWT token (obtained from login endpoint)
4. Test endpoints directly from the browser

### Example: Testing in Swagger UI

1. **Login**: POST `/api/v1/auth/login` with credentials
2. **Copy** the `access_token` from response
3. **Click** "Authorize" button
4. **Paste** token in format: `Bearer {token}`
5. **Test** other endpoints as authenticated user

---

## 🔧 Common Issues & Troubleshooting

### Issue: Database Connection Failed

**Error Message:** `FATAL: database "hospital_db" does not exist`

**Solution:**
```bash
# Create the database
createdb hospital_db

# Or using PostgreSQL CLI
psql -U postgres
CREATE DATABASE hospital_db;
```

### Issue: Secret Key Missing

**Error Message:** `KeyError: 'SECRET_KEY'`

**Solution:**
- Ensure `.env` file exists in project root
- Add `SECRET_KEY` and `JWT_SECRET_KEY` to `.env`

### Issue: Port Already in Use

**Error Message:** `Address already in use`

**Solution:**
```bash
# Run on different port
python -c "
from hospitalapp import create_app
app = create_app()
app.run(debug=True, port=5001)
"
```

### Issue: CORS Errors

**Solution:**
- Ensure frontend is making requests to correct base URL
- Check CORS configuration in Flask app

---

## 📖 Development Guidelines

### Code Structure

- **Controllers**: Handle HTTP request/response logic
- **Services**: Contain business logic
- **Repositories**: Handle database operations
- **Routes**: Define API endpoints and HTTP methods
- **Utils**: Shared utility functions

### Adding New Endpoints

1. Create route in `routes/` directory
2. Implement controller in `controllers/`
3. Add service logic in `services/`
4. Add repository methods in `repositories/`
5. Register blueprint in `hospitalapp.py`

### Example: Creating New Patient Endpoint

**routes/patient_routes.py:**
```python
@patient_bp.route('/<int:patient_id>/records', methods=['GET'])
def get_patient_records(patient_id):
    """Get patient medical records"""
    # Implementation
    pass
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 📞 Support & Contact

For questions or issues:

- **GitHub Issues**: [Report an issue](https://github.com/Benaniosam-hub/Project_Hospital_Management_System/issues)
- **Email**: Contact the project maintainer

---

## 🎯 Roadmap

- [ ] Advanced patient analytics
- [ ] Prescription management
- [ ] Billing and insurance integration
- [ ] Mobile app support
- [ ] Telemedicine features
- [ ] Advanced reporting
- [ ] Multi-language support

---

## 📝 Version History

### v1.0.0 (Current)
- Initial release
- Core CRUD operations for all modules
- JWT authentication
- Swagger documentation
- PostgreSQL integration

---

**Last Updated**: January 2024  
**Maintainer**: [Benaniosam-hub](https://github.com/Benaniosam-hub)
