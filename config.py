from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    db_server_name: str = os.getenv('DB_SERVER_NAME')
    db_user: str = os.getenv('DB_USER')
    db_password: str = os.getenv('DB_PASSWORD')
    db_ip: str = os.getenv('DB_IP')

    class Config:
        env_file=".env"
