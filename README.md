# 🏥 Hospital Management System with Swagger UI

> **High-Performance Hospital Management API** - Built with FastAPI for concurrent request handling and interactive API visualization with Swagger UI

A comprehensive RESTful API for managing hospital operations including patient management, inpatient services, appointments, and authentication. Now upgraded with **FastAPI** for superior performance and **high concurrency** support.

---

## 🏥 Overview

The **Hospital Management System with Swagger UI** is a modern healthcare backend built with **FastAPI**, delivering high-performance concurrent request handling for hospital operations. Features include:

- **Patient Management**: Register, update, and manage patient information
- **Inpatient Services**: Manage hospital admissions and inpatient records
- **Appointments**: Schedule and manage medical appointments
- **Authentication**: Secure JWT-based authentication for users
- **Interactive API Documentation**: Built-in Swagger UI for API exploration and testing

## ✨ Key Features

- ⚡ **FastAPI Framework** - Modern, fast Python web framework (3x faster than Flask)
- 🔄 **High Concurrency** - Async/await support for handling multiple concurrent requests
- 📊 **Interactive Swagger UI** - Beautiful, real-time API documentation and testing interface
- ✅ JWT-based authentication & authorization
- ✅ PostgreSQL database integration
- ✅ Automatic OpenAPI/Swagger documentation
- ✅ Advanced error handling and validation
- ✅ Environment-based configuration
- ✅ Database connection pooling
- ✅ Request/Response validation with Pydantic models

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | FastAPI 0.95+ |
| **API Documentation** | Swagger UI / OpenAPI 3.0 |
| **Async Server** | Uvicorn (ASGI) |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Authentication** | JWT (JSON Web Tokens) |
| **Language** | Python 3.8+ |
| **Validation** | Pydantic |
| **Environment Management** | python-dotenv |

---

## 📦 Prerequisites

- **Python 3.8+**
- **PostgreSQL 10+**
- **pip** (Python package manager)
- **Uvicorn** (ASGI server for async execution)

---

## 🚀 Installation & Configuration

### 1. Clone & Setup

```bash
git clone https://github.com/Benaniosam-hub/Project_Hospital_Management_System.git
cd Project_Hospital_Management_System

# Create virtual environment
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Create Database

```bash
createdb hospital_db
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

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

# FastAPI Configuration
DEBUG=True
HOST=127.0.0.1
PORT=8000
WORKERS=4
```

---

## 📁 Project Structure

```
Project_Hospital_Management_System/
├── main.py                      # FastAPI application entry point
├── config.py                    # Configuration settings
├── requirements.txt             # Project dependencies
├── .env                         # Environment variables
│
├── api/                         # API routes layer
│   └── v1/
│       ├── __init__.py
│       ├── patients.py          # Patient endpoints
│       ├── inpatients.py        # Inpatient endpoints
│       ├── appointments.py      # Appointment endpoints
│       └── auth.py              # Authentication endpoints
│
├── controllers/                 # Business logic layer
│   ├── patient_controller.py
│   ├── inpatient_controller.py
│   ├── appointment_controller.py
│   └── auth_controller.py
│
├── services/                    # Business operations
│   ├── patient_service.py
│   ├── inpatient_service.py
│   ├── appointment_service.py
│   └── auth_service.py
│
├── repositories/                # Data access layer
│   ├── patient_repository.py
│   ├── inpatient_repository.py
│   ├── appointment_repository.py
│   └── auth_repository.py
│
├── schemas/                     # Pydantic models for validation
│   ├── patient_schema.py
│   ├── inpatient_schema.py
│   ├── appointment_schema.py
│   └── auth_schema.py
│
├── database/                    # Database configuration
│   ├── connection.py
│   ├── models.py
│   └── session.py
│
└── utils/                       # Utilities
    ├── validators.py
    ├── decorators.py
    ├── security.py
    └── helpers.py
```

---

## 📊 Database Schema

### Core Tables

**Users Table** - Authentication & role management
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

**Patients Table** - Patient information & medical history
```sql
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE,
    phone VARCHAR(20),
    date_of_birth DATE,
    gender VARCHAR(10),
    address TEXT,
    blood_group VARCHAR(5),
    medical_history TEXT,
    allergies TEXT,
    emergency_contact VARCHAR(100),
    insurance_number VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Appointments Table** - Appointment scheduling
```sql
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    doctor_id INTEGER NOT NULL REFERENCES users(id),
    appointment_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER DEFAULT 30,
    reason_for_visit TEXT,
    status VARCHAR(50) DEFAULT 'scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (patient_id, appointment_date)
);
```

**Inpatients Table** - Hospital admissions
```sql
CREATE TABLE inpatients (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    admission_date TIMESTAMP NOT NULL,
    discharge_date TIMESTAMP,
    room_number VARCHAR(50),
    bed_number VARCHAR(50),
    ward_name VARCHAR(100),
    admission_reason TEXT NOT NULL,
    attending_doctor_id INTEGER NOT NULL REFERENCES users(id),
    diagnosis TEXT,
    treatment_plan TEXT,
    status VARCHAR(50) DEFAULT 'admitted',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Medical Records Table** - Detailed medical documentation
```sql
CREATE TABLE medical_records (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id) ON DELETE CASCADE,
    inpatient_id INTEGER REFERENCES inpatients(id),
    record_type VARCHAR(50),
    record_date TIMESTAMP NOT NULL,
    description TEXT,
    doctor_id INTEGER NOT NULL REFERENCES users(id),
    attachments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Entity Relationships

```
Users (1) -----> (Many) Appointments, Inpatients, Medical Records
Patients (1) ----> (Many) Appointments, Inpatients, Medical Records
```

---

## 🔌 API Endpoints

### Base URL
```
http://localhost:8000/api/v1
```

### Response Format

**Success (2xx):**
```json
{
    "status": "success",
    "message": "Operation completed successfully",
    "data": { /* response data */ }
}
```

**Error (4xx, 5xx):**
```json
{
    "status": "error",
    "message": "Error description",
    "error_code": "ERROR_CODE",
    "details": {}
}
```

### Authentication Endpoints (`/auth`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login & get JWT token |
| POST | `/auth/logout` | Logout |

**Login Request:**
```http
POST /api/v1/auth/login
{
    "email": "john@example.com",
    "password": "SecurePassword123!"
}
```

**Login Response:**
```json
{
    "status": "success",
    "data": {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "token_type": "Bearer",
        "expires_in": 3600,
        "user": { "id": 1, "username": "johndoe", "role": "doctor" }
    }
}
```

### Patient Endpoints (`/patients`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/patients` | Create patient |
| GET | `/patients` | Get all patients (paginated) |
| GET | `/patients/{id}` | Get patient by ID |
| PUT | `/patients/{id}` | Update patient |
| DELETE | `/patients/{id}` | Delete patient |

**Query Parameters:** `page`, `limit`, `search`

### Inpatient Endpoints (`/inpatient`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/inpatient` | Create inpatient record |
| GET | `/inpatient` | Get all inpatients (paginated) |
| GET | `/inpatient/{id}` | Get inpatient by ID |
| PUT | `/inpatient/{id}` | Update inpatient |
| POST | `/inpatient/{id}/discharge` | Discharge patient |

**Query Parameters:** `page`, `limit`, `status`, `ward_name`

### Appointment Endpoints (`/appointments`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/appointments` | Schedule appointment |
| GET | `/appointments` | Get all appointments (paginated) |
| GET | `/appointments/{id}` | Get appointment by ID |
| PUT | `/appointments/{id}` | Update appointment |
| POST | `/appointments/{id}/cancel` | Cancel appointment |
| POST | `/appointments/{id}/complete` | Mark as completed |

**Query Parameters:** `page`, `limit`, `status`, `doctor_id`, `patient_id`

---

## 🔐 Authentication

The API uses **JWT (JSON Web Tokens)** for secure authentication.

### Token Structure

```
Header:     {"alg": "HS256", "typ": "JWT"}
Payload:    {"user_id": 1, "username": "johndoe", "role": "doctor", "exp": ..., "iat": ...}
Signature:  HMACSHA256(base64(header) + "." + base64(payload), secret_key)
```

### How to Use

1. **Register** at `/auth/register`
2. **Login** at `/auth/login` to get access token
3. **Include token** in all requests: `Authorization: Bearer {access_token}`
4. **Token expires** in 3600 seconds (1 hour)

### Protected Routes

All endpoints except `/auth/register` and `/auth/login` require a valid JWT token.

---

## 🚀 Running the Application

### Standard Execution

```bash
# Make sure virtual environment is activated
python main.py
```

The application will start on `http://localhost:8000`

### Production Deployment with Uvicorn

```bash
# Run with multiple workers for high concurrency
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# Run with auto-reload for development
uvicorn main:app --reload --port 8000
```

### Access Points

| URL | Purpose |
|-----|---------|
| `http://localhost:8000/` | Health check / API status |
| `http://localhost:8000/api/v1` | API Base URL |
| `http://localhost:8000/docs` | **Swagger UI Documentation** 📊 |
| `http://localhost:8000/redoc` | ReDoc Alternative Documentation |
| `http://localhost:8000/openapi.json` | OpenAPI Schema (JSON) |

---

## 📊 Swagger UI Visualization

The application features a **modern, interactive Swagger UI** that provides a beautiful interface for exploring and testing the API in real-time.

### Accessing Swagger UI

1. Start the application:
   ```bash
   python main.py
   # or for production
   uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8000/docs
   ```

3. You'll see the complete API documentation with:
   - 📋 All available endpoints organized by tags
   - 📝 Request/response schemas with examples
   - 🔑 Security/Authorization section for JWT tokens
   - 🧪 **Try it out** feature to test endpoints interactively
   - ⚡ Real-time request/response visualization

### Using Swagger UI for Testing

1. **Authenticate First:**
   - Locate the `/auth/login` endpoint
   - Click "Try it out" button
   - Enter your credentials (email & password)
   - Click "Execute" to get your JWT token
   - Copy the `access_token` from the response

2. **Authorize Your Session:**
   - Click the green "Authorize" button at the top
   - Paste your token as: `Bearer {your_token_here}`
   - Click "Authorize" to proceed with authenticated requests

3. **Test Any Endpoint:**
   - Expand any endpoint section
   - Click "Try it out" button
   - Fill in required parameters and request body
   - Click "Execute" to see live responses
   - View response status, headers, and body

4. **Explore Schemas:**
   - Scroll to the bottom to see model definitions
   - Understand the structure of request/response data
   - Reference data types and required fields

### Swagger UI Features

- ⚡ **Lightning Fast** - Built-in with FastAPI (no external dependencies)
- ✨ **Interactive Testing** - Execute real API calls from the browser
- 📦 **Schema Validation** - Automatic request validation with clear errors
- 🎯 **Smart Navigation** - Filter and search endpoints quickly
- 📱 **Responsive Design** - Works perfectly on all devices
- 🔒 **Security Integration** - Built-in JWT token management
- 📄 **Complete Documentation** - Parameters, models, and examples included
- 🚀 **Real-time Updates** - Documentation auto-syncs with code

---

## ⚡ Performance & Concurrency

### FastAPI Advantages

FastAPI is **3x faster than Flask** and built for async/concurrent operations:

- **Async Support**: Handle thousands of concurrent requests efficiently
- **Automatic Validation**: Pydantic models validate data before processing
- **Optimal Performance**: Built on Starlette and Uvicorn (production-grade ASGI)
- **Reduced Latency**: Non-blocking I/O for database and external API calls

### Running with High Concurrency

```bash
# Production setup with 4 worker processes
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# For high-traffic scenarios
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 8 --loop uvloop

# Development with auto-reload
uvicorn main:app --reload --port 8000
```

---

## 🔧 Troubleshooting

### Database Connection Failed
```
Error: FATAL: database "hospital_db" does not exist
Solution: createdb hospital_db
```

### Secret Key Missing
```
Error: KeyError: 'SECRET_KEY'
Solution: Ensure .env file exists with SECRET_KEY & JWT_SECRET_KEY
```

### Port Already in Use
```
Error: Address already in use
Solution: uvicorn main:app --port 8001
```

### Swagger UI Not Loading
```
Error: 404 when accessing /docs
Solution: Ensure FastAPI is properly initialized in main.py
         Verify the application is running on the correct port
         Check that FastAPI dependencies are installed (uvicorn, starlette)
```

### High CPU Usage with Multiple Workers
```
Solution: Adjust worker count based on CPU cores (--workers should <= 2 * CPU cores + 1)
         Monitor with: htop or Task Manager
         Consider load balancing with Nginx
```

---

## 📖 Development Guidelines

### Architecture Layers

- **API Routes**: Endpoint definitions with FastAPI decorators
- **Controllers**: HTTP request/response logic
- **Services**: Business logic operations (async-ready)
- **Repositories**: Database CRUD operations
- **Schemas**: Pydantic models for request/response validation
- **Utils**: Shared utilities & validators

### Adding New Async Endpoints

```python
# Example: api/v1/patients.py
from fastapi import APIRouter, Depends
from schemas import PatientSchema

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/")
async def get_patients(page: int = 1, limit: int = 10):
    # Async operation
    return await patient_service.get_all(page, limit)

@router.post("/")
async def create_patient(patient: PatientSchema):
    # Automatic validation with Pydantic
    return await patient_service.create(patient)
```

### Leveraging Async/Await

```python
# Concurrent database operations
async def get_patient_with_records(patient_id: int):
    patient, records, appointments = await asyncio.gather(
        patient_repo.get_by_id(patient_id),
        medical_record_repo.get_by_patient(patient_id),
        appointment_repo.get_by_patient(patient_id)
    )
    return {patient, records, appointments}
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

For questions or issues: [Report an issue](https://github.com/Benaniosam-hub/Project_Hospital_Management_System/issues)

---

## 🎉 Migration from Flask to FastAPI

This project has been completely upgraded from Flask to FastAPI to provide:
- **3x Performance Improvement** - Faster request processing
- **High Concurrency Support** - Handle many concurrent requests simultaneously
- **Better Type Safety** - Pydantic models with automatic validation
- **Built-in API Documentation** - Swagger UI and ReDoc included by default
- **Production Ready** - Optimized for deployment with Uvicorn
