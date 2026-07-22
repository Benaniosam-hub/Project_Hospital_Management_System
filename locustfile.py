import random
from locust import HttpUser, task, between

class HospitalUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(3)
    def get_patients(self):
        self.client.get("/api/v1/patients/")

    @task(2)
    def get_inpatient_rooms(self):
        self.client.get("/api/v1/inpatient/rooms")

    @task(2)
    def get_doctor_schedule(self):
        # Pick a random doctor ID strictly from your actual doctor dataset (IDs 1 to 20)
        doctor_id = random.randint(1, 20)
        
        # Group metrics together cleanly under one endpoint name in the Locust UI
        self.client.get(
            f"/api/v1/appointments/doctor/{doctor_id}", 
            name="/api/v1/appointments/doctor/[id]"
        )

    @task(1)
    def get_health(self):
        self.client.get("/")