# =====================================================================
# This file reads environment variables from the .env file and turns
# them into a Python object with automatic validation (using pydantic)
# instead of using os.getenv() everywhere in the project
# =====================================================================

# We import this library so it validates the incoming values for us instead of doing it manually
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str 
    APP_VERSION: str
    OPENAI_API_KEY: str
    
    MONGODB_URI: str
    MONGODB_NAME: str
    
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    
    model_config=SettingsConfigDict(env_file='.env')

def get_settings(): 
    return Settings()
