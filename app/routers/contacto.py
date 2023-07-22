from fastapi import APIRouter
from app.schemas.ContactoSchema import ContactoData
from app.database import SessionLocal, Contacto
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post('/contacto/crear', tags=["contacto"])
async def crear_contacto(contacto: ContactoData):
  try:
    db = SessionLocal()
    new_contact = Contacto(nombre=contacto.nombre, apellido=contacto.apellido, email=contacto.email, telefono=contacto.telefono, ruc=contacto.ruc)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact
  except IntegrityError as e:
    db.rollback()
    return{"error": "El contacto con ese nombre ya existe."}
