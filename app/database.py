from fastapi import FastAPI
from sqlalchemy import create_engine, Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship   
from config import Settings

settings = Settings()

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.db_user}:{settings.db_password}@{settings.db_ip}/{settings.db_server_name}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Contacto(Base):
    __tablename__ = "contactos_data"
    nombre = Column(String, index=True, primary_key=True)
    apellido = Column(String, nullable=False)
    email = Column(String())
    telefono = Column(BigInteger())
    ruc = Column(BigInteger())

Base.metadata.create_all(bind=engine)
