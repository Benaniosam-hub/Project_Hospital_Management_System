# 🏥 Hospital Management System — High-Concurrency Edition (Updated)

> Enterprise-grade async Hospital Management API (FastAPI) focused on high concurrency, load testing with Locust, and clear, accurate API documentation.

This README has been updated to match the repository's implemented routes and instructions. Missing or planned endpoints are noted as TODOs.

---

## 🚀 What's New

- Fully asynchronous FastAPI application with async DB connection lifecycle.
- Locust load-testing scenarios included.
- RBAC example on patient registration endpoint.

---

## 🎯 Key Features (implemented)

- Async endpoints powered by FastAPI
- JWT-based authentication (routes present)
- Patient listing and patient registration (role-protected)
- Inpatient room management and patient admission
- Appointment booking and doctor schedule retrieval
- Locust scenarios for load testing

---

## 🧰 Tech Stack

- Language: Python 3.8+
- Framework: FastAPI (async)
- Server: Uvicorn (ASGI)
- DB driver: asyncpg (async)
- Validation: Pydantic
- Load testing: Locust

---

## 📁 Project structure (top-level)

```
Project_Hospital_Management_System/
├── hospitalapp.py           # FastAPI app (routers included with /api/v1)
├── config.py                # dotenv-based configuration
├── requirements.txt
├── locustfile.py            # Load testing scenarios
├── Dockerfile
├── docker-compose.yml
├── routes/                  # APIRouters (auth, patients, inpatient, appointments...)
├── controllers/             # Request handling / controllers
├── services/                # Business logic (async)
├── repositories/            # DB access (async)
├── schemas/                 # Pydantic models
└── database/                # connection/session/models (async DB pool)
```

---

## 🔌 Base URL

All routers are included with the prefix `/api/v1`.

Base URL (local):
```
http://localhost:8000/api/v1
```

---

## 🔗 Implemented API Endpoints (accurate to routes/*)

### Authentication (`/auth`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/auth/register` | Register new staff user |
| POST   | `/auth/login`    | Login & receive JWT token |

### Patients (`/patients`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/patients/`         | Get all patients (paginated) — requires JWT |
| POST   | `/patients/register` | Register a new patient — protected by roles (admin/doctor/receptionist) |

Note: The code currently exposes listing and a role-protected register endpoint. If you need per-patient CRUD (GET/PUT/DELETE `/patients/{id}`), add those routes in routes/patient_routes.py and controllers.

### Inpatient (`/inpatient`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/inpatient/rooms` | Add a new room |
| GET    | `/inpatient/rooms` | List inpatient rooms |
| POST   | `/inpatient/admit` | Admit a patient |

### Appointments (`/appointments`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/appointments/book`         | Book an appointment |
| GET    | `/appointments/doctor/{id}`  | Get a doctor's schedule by doctor_id |

---

## 🔐 Authentication usage

1. Register: POST `/api/v1/auth/register`
2. Login: POST `/api/v1/auth/login` -> receives JWT access token
3. Include token on protected requests:
```
Authorization: Bearer {access_token}
```

Protected routes: patient listing, patient registration (with role dependency), and other endpoints that use get_current_user dependency.

---

## 🚀 Run locally (development)

Create and activate a virtual environment, install requirements:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create the database (example):

```bash
createdb hospital_db
```

Create a `.env` file in project root with at least:

```env
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hospital_db
DB_USER=postgres
DB_PASSWORD=your_db_password
```

Start the app:

```bash
# development (reload)
python -m uvicorn hospitalapp:app --reload --port 8000
```

Docs will be available at `http://localhost:8000/docs` (Swagger UI).

---

## 📊 Locust load testing

Start Locust UI:

```bash
locust -f locustfile.py --host=http://localhost:8000
# Open http://localhost:8089
```

Run headless example:

```bash
locust -f locustfile.py --host=http://localhost:8000 --users 50 --spawn-rate 5 --run-time 5m --headless
```

---

## TODO / Notes

- README previously listed more patient CRUD endpoints and other routes. This file now reflects the routes currently implemented in `routes/`.
- If you prefer the README to document planned endpoints, mark them as TODO and keep them in a separate section.
- The repository currently includes Docker artifacts (Dockerfile, docker-compose.yml) — you can add containerized run instructions here if needed.

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit and open a PR

---

## 📄 License

MIT
