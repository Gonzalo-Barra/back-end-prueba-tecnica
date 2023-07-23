from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import contacto
from config import CORS


app = FastAPI()

origins = [
    CORS.ip_1,
    CORS.ip_2
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacto.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
