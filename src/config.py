from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Application settings using Pydantic BaseSettings.
    
    Args:
        app_name: Name of the application
        debug_mode: Enable debug features
        max_concurrent_calls: Maximum number of simultaneous calls
    """
    app_name: str = "AI Phone Responder"
    debug_mode: bool = True
    max_concurrent_calls: int = 5
    
    # LLM Settings
    ollama_base_url: str = "http://localhost:11434"
    model_name: str = "mistral"
    
    # Audio Settings
    sample_rate: int = 16000
    channels: int = 1
    
    class Config:
        env_file = ".env"

settings = Settings()