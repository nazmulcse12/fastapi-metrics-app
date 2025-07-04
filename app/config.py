from pydantic import BaseSettings

class Settings(BaseSettings):
    metrics_collection_interval: int = 5
    app_name: str = "FastAPI Metrics App"
    
    class Config:
        env_file = ".env"

settings = Settings()