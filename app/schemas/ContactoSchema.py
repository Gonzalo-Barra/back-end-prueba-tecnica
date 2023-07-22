from pydantic import BaseModel

class ContactoData(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: int
    ruc: int
