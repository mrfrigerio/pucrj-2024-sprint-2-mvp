from pydantic import BaseModel

# Schema de exemplo
class CaptureSchema(BaseModel):
    trainer_name: str = "Treinador Pokemon"
    capture_date: str = "2024-06-22"
    pokemon_name: str = "pikachu"


class DeleteCaptureSchema(BaseModel):
   capture_id: int = 1
