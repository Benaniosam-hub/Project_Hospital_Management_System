from repositories.patient_repository import PatientRepository

class PatientService:
    def __init__(self):
        self.patient_repo = PatientRepository()

    async def register_patient(self,data):
        """Processs logic for directly recording incoming patient registrations"""
        new_patient = await self.patient_repo.create_patient(data)
        return {"status": "success","message": "patient recorded successfully", "data": new_patient}, 201
    
    async def list_patients(self):
        """Fetches the directory list of all records."""
        patients = await self.patient_repo.get_all_patients()
        return {"status": "success", "count": len(patients), "data": patients}, 200
    