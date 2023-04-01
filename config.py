import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    DB_USER = os.getenv('DB_USER')
    DB_USER_PASSWORD = os.getenv('DB_USER_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_PORT = os.getenv('DB_PORT')
    DB_URL = f'postgresql+psycopg2://{DB_USER}:{DB_USER_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


config = Config
