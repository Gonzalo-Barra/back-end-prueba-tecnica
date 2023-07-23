from dotenv import load_dotenv
import os

load_dotenv()

class DATABASE:
    db_server_name: str = os.getenv('DB_SERVER_NAME')
    db_user: str = os.getenv('DB_USER')
    db_password: str = os.getenv('DB_PASSWORD')
    db_ip: str = os.getenv('DB_IP')


class CORS:
    ip_1: str = os.getenv('CORS_IP_1')
    ip_2: str = os.getenv('CORS_IP_2')