import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseSettings, Field

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    #db_url: str = Field(..., env='DATABASE_URL')
    PROJECT_TITLE:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"
    
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5433) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","my_db")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()