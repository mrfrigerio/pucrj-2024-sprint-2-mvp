from pydantic import BaseModel


# Schema de exemplo
class AddParameterSchema(BaseModel):
    patient_name: str = "João da Silva"
    pregnancies: float = 0
    glucose: float = 137
    blood_pressure: float = 40
    skin_thickness: float = 35
    insulin: float = 168
    bmi: float = 43.1
    diabetes_pedigree_function: float = 2.288
    age: float = 33


class DeleteParameterSchema(BaseModel):
    parameter_id: int = 1
