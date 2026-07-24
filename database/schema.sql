-- STAFF table (handles Admins, Doctors, Nurses, etc.)
CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'doctor', 'nurse', 'receptionist', 'pharmacist')),
    specialization VARCHAR(100) DEFAULT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Patient table
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL CHECK (gender IN ('Male', 'Female', 'Other')),
    date_of_birth DATE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    blood_group VARCHAR(5) DEFAULT NULL,
    patient_type VARCHAR(20) DEFAULT 'Outpatient' CHECK (patient_type IN ('Inpatient', 'Outpatient')),
    is_active BOOLEAN DEFAULT TRUE
);

-- Patient Indexes
CREATE INDEX IF NOT EXISTS idx_patients_phone ON patients (phone);
CREATE INDEX IF NOT EXISTS idx_patients_name ON patients (LOWER(last_name), LOWER(first_name));


-- Appointment table
CREATE TABLE appointments (
    appointment_id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'Scheduled' CHECK (status IN ('Scheduled', 'Completed', 'Cancelled')),
    reason TEXT DEFAULT NULL,
    CONSTRAINT fk_appointment_patient FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    CONSTRAINT fk_appointment_doctor FOREIGN KEY (doctor_id) REFERENCES staff(staff_id) ON DELETE CASCADE
);

-- Appointment Indexes
CREATE INDEX IF NOT EXISTS idx_appointments_patient_id ON appointments (patient_id);
CREATE INDEX IF NOT EXISTS idx_appointments_doctor_id ON appointments (doctor_id);
CREATE INDEX IF NOT EXISTS idx_appointments_doctor_date ON appointments (doctor_id, appointment_date);


-- Room Table
CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    room_number VARCHAR(10) UNIQUE NOT NULL,
    room_type VARCHAR(20) NOT NULL CHECK (room_type IN ('General Ward', 'Semi-Private', 'Private', 'ICU')),
    price_per_day NUMERIC(10, 2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE
);

-- Room Index
CREATE INDEX IF NOT EXISTS idx_rooms_number ON rooms (room_number);


-- Admission Table
CREATE TABLE admissions (
    admission_id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    room_id INT NOT NULL,
    doctor_id INT NOT NULL,
    admission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    discharge_date TIMESTAMP DEFAULT NULL,
    reason_for_admission TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'Admitted' CHECK (status IN ('Admitted', 'Discharged')),
    CONSTRAINT fk_admission_patient FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    CONSTRAINT fk_admission_room FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE SET NULL,
    CONSTRAINT fk_admission_doctor FOREIGN KEY (doctor_id) REFERENCES staff(staff_id) ON DELETE SET NULL
); 

-- Admission Indexes
CREATE INDEX IF NOT EXISTS idx_admissions_patient_id ON admissions (patient_id);
CREATE INDEX IF NOT EXISTS idx_admissions_room_id ON admissions (room_id);


-- Medical Records
CREATE TABLE medical_records (
    record_id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    diagnosis TEXT NOT NULL,
    prescription TEXT DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_record_patient FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    CONSTRAINT fk_record_doctor FOREIGN KEY (doctor_id) REFERENCES staff(staff_id) ON DELETE CASCADE
);

-- Medical Records Index
CREATE INDEX IF NOT EXISTS idx_medical_records_patient ON medical_records (patient_id);