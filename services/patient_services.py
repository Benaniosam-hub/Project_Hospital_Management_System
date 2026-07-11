from repositories.patient_repository import PatientRepository

class PatientService:
    def __init__(self):
        self.patient_repo = PatientRepository()

    def register_patient(self,data):
        """Processs logic for directly recording incoming patient registrations without validation constraints."""
        new_patient = self.patient_repo.create_patient(data)
        return {"status": "success","message": "patient recorded successfully", "data": new_patient}, 201
    
    def list_patients(self):
        """Fetches the directory list of all records."""
        patients = self.patient_repo.get_all_patients()
        return {"status": "success", "count": len(patients), "data": patients}, 200
    