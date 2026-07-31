# 🏥 Hospital Management System API

<p align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![AsyncIO](https://img.shields.io/badge/Async-High%20Concurrency-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Authentication-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge)
![Swagger](https://img.shields.io/badge/Swagger-OpenAPI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)

</p>

<p align="center">
Production-oriented Hospital Management System REST API built with <b>FastAPI</b>, <b>PostgreSQL</b>, and <b>Async Python</b>.
</p>

---

# 📖 Overview

This project demonstrates modern backend development practices using FastAPI and PostgreSQL. It follows a layered architecture with clear separation of responsibilities, secure authentication, asynchronous request handling, and modular code organization.

## Highlights

* Async FastAPI REST API
* JWT Authentication
* Role-Based Access Control (RBAC)
* BCrypt Password Hashing
* Pydantic Request Validation
* PostgreSQL Database
* Async Database Connection Pooling
* Docker Support
* Swagger API Documentation

---

# ✨ Features

### Authentication

* JWT Authentication
* BCrypt Password Hashing
* Protected API Endpoints

### User Roles

* Admin
* Doctor
* Nurse
* Receptionist
* Pharmacist

### Patient Management

* Register Patients
* Update Patient Details
* View Patient Records

### Appointment Management

* Schedule Appointments
* Manage Appointment Status
* Assign Doctors

### Admission Management

* Admit Patients
* Allocate Rooms
* Discharge Patients

### Medical Records

* Store Medical History
* View Patient Records

---

# 🏗 Architecture

```
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Controllers
   │
   ▼
Services
   │
   ▼
Repositories
   │
   ▼
PostgreSQL
```

The project follows a layered architecture where each layer has a single responsibility, making the codebase easier to maintain and extend.

---

# 📂 Project Structure

```text
Hospital_Management_System/
│
├── controllers/
├── routes/
├── services/
├── repositories/
├── schemas/
├── middleware/
├── database/
├── core/
├── hospitalapp.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

# ⚙ Technology Stack

| Category         | Technology  |
| ---------------- | ----------- |
| Language         | Python 3.11 |
| Framework        | FastAPI     |
| Database         | PostgreSQL  |
| Database Driver  | asyncpg     |
| Validation       | Pydantic    |
| Authentication   | JWT         |
| Password Hashing | BCrypt      |
| Containerization | Docker      |

---

# 🔐 Security

* JWT Authentication
* BCrypt Password Hashing
* Role-Based Authorization
* Environment Variable Configuration
* Pydantic Input Validation
* Parameterized Database Queries

---

# ⚡ Asynchronous Performance

The application uses asynchronous programming to improve responsiveness and efficiently handle concurrent requests.

Features include:

* Async FastAPI Endpoints
* Async PostgreSQL Driver (`asyncpg`)
* Database Connection Pooling
* Non-blocking Database Operations

---

# 🧪 Load Testing

The application was tested using **Locust** to evaluate API performance under concurrent workloads.

The load test measures:

* Concurrent Users
* Requests Per Second (RPS)
* Response Time
* Failure Rate
* Overall API Throughput

---

# 🗄 Database

The project uses PostgreSQL with a normalized relational schema.

Main entities include:

* Staff
* Patients
* Appointments
* Rooms
* Admissions
* Medical Records

Database design includes:

* Foreign Key Constraints
* Indexed Relationships
* Data Integrity

---

# 📸 Project Screenshots

## ⚡ Locust Load Testing

<p align="center">
<img src="https://github.com/user-attachments/assets/42678087-9604-42de-880a-6882f2933ed8" width="900">
</p>

Locust was used to simulate concurrent users and monitor application performance under load.

---

## 📊 Performance Statistics

<p align="center">
<img src="https://github.com/user-attachments/assets/a7e68e8d-5f43-4a46-aad2-17194751856a" width="900">
</p>

Performance statistics include request throughput, response times, concurrent users, and failure rates.

---

## 🗄 Database Schema

<p align="center">
<img src="https://github.com/user-attachments/assets/7bb37eac-c37d-42da-8070-26b2ca7c96e8" width="650">
</p>

Relational database schema showing the relationships between hospital entities.

---

## 📖 Swagger API Documentation

<p align="center">
<img src="https://github.com/user-attachments/assets/f8d5cfb6-7623-4b65-92f7-178f768c003c" width="900">
</p>

Interactive API documentation generated automatically by FastAPI.

---

## 🐳 Docker Compose - Running Containers

<p align="center">
<img width="1456" height="998" alt="Screenshot 2026-07-31 at 10 54 46 AM" src="https://github.com/user-attachments/assets/369e9a4f-2ad9-4801-8bf8-d62641e2a26d" />
</p>

**FastAPI** and **PostgreSQL** containers managed by Docker Compose.

---

## 📋 Docker Container Logs

<p align="center">
<img width="1456" height="998" alt="Screenshot 2026-07-31 at 10 54 39 AM" src="https://github.com/user-attachments/assets/da2d1e82-6af9-47bd-8ef0-945b3b4f8b22" />
</p>

Container logs confirmation.

---

## 💻 Docker Compose Terminal Logs

<p align="center">
<img width="662" height="448" alt="Screenshot 2026-07-31 at 10 38 23 AM" src="https://github.com/user-attachments/assets/8b84f6f8-8080-4604-aad3-fa693761875f" />
</p>

`docker compose logs` showing successful service startup.

# 🚀 Running the Project

Clone the repository

```bash
git clone https://github.com/Benaniosam-hub/Project_Hospital_Management_System.git
```

Move into the project

```bash
cd Project_Hospital_Management_System
```

Run with Docker

```bash
docker compose up --build
```

Application

```
http://localhost:8000
```

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# ⚙ Environment Variables

Create a `.env` file.

```env
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

JWT_SECRET_KEY=
```

---

# 📚 What I Learned

* FastAPI Development
* REST API Design
* Async Programming
* PostgreSQL
* JWT Authentication
* RBAC
* Repository Pattern
* Docker
* Pydantic Validation
* Load Testing with Locust

---

# 👨‍💻 Author

**Benaniosam S**

Backend Developer

GitHub: https://github.com/Benaniosam-hub

---

⭐ If you found this project useful, consider giving it a **Star**.
