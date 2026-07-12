# Hospital Management System API

A comprehensive RESTful API for managing hospital operations including patient management, inpatient services, appointments, and authentication.

---

## 🏥 Overview

The Hospital Management System API is built with **Flask** and provides a complete backend solution for hospital operations. It handles:

- **Patient Management**: Register, update, and manage patient information
- **Inpatient Services**: Manage hospital admissions and inpatient records
- **Appointments**: Schedule and manage medical appointments
- **Authentication**: Secure JWT-based authentication for users

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

- **Python 3.8+**
- **PostgreSQL 10+**
- **pip** (Python package manager)

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

# Flask Configuration
FLASK_DEBUG=True
```

---

## 📁 Project Structure

```
Project_Hospital_Management_System/
├── hospitalapp.py              # Application entry point
├── config.py                   # Configuration settings
├── requirements.txt            # Project dependencies
├── .env                        # Environment variables
│
├── controllers/                # Business logic layer
│   ├── patient_controller.py
│   ├── inpatient_controller.py
│   ├── appointment_controller.py
│   └── auth_controller.py
│
├── routes/                     # API endpoints
│   ├── patient_routes.py
│   ├── inpatient_routes.py
│   ├── appointment_routes.py
│   └── auth_routes.py
│
├── services/                   # Business operations
│   ├── patient_service.py
│   ├── inpatient_service.py
│   ├── appointment_service.py
│   └── auth_service.py
│
├── repositories/               # Data access layer
│   ├── patient_repository.py
│   ├── inpatient_repository.py
│   ├── appointment_repository.py
│   └── auth_repository.py
│
├── database/                   # Database configuration
│   ├── connection.py
│   └── models.py
│
└── utils/                      # Utilities
    ├── validators.py
    ├── decorators.py
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
http://localhost:5000/api/v1
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

```bash
# Make sure virtual environment is activated
python hospitalapp.py
```

The application will start on `http://localhost:5000`

### Access Points

| URL | Purpose |
|-----|---------|
| `http://localhost:5000/` | Health check |
| `http://localhost:5000/api/v1` | API Base URL |
| `http://localhost:5000/apidocs/` | Swagger UI documentation |

### Using Swagger UI

1. Start the application
2. Navigate to `http://localhost:5000/apidocs/`
3. Click "Authorize" button
4. Login to get token & paste it as `Bearer {token}`
5. Test endpoints directly from browser

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
Solution: python -c "from hospitalapp import create_app; app = create_app(); app.run(port=5001)"
```

### CORS Errors
- Verify frontend is using correct API base URL
- Check CORS configuration in Flask app

---

## 📖 Development Guidelines

### Architecture Layers

- **Controllers**: HTTP request/response logic
- **Services**: Business logic operations
- **Repositories**: Database CRUD operations
- **Routes**: Endpoint definitions
- **Utils**: Shared utilities & validators

### Adding New Endpoints

1. Create route in `routes/` directory
2. Implement controller in `controllers/`
3. Add service logic in `services/`
4. Add repository methods in `repositories/`
5. Register blueprint in `hospitalapp.py`

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
