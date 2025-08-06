from fastapi import FastAPI
from .config import settings

app = FastAPI(title=settings.app_name)

@app.get("/health")
async def health_check():
    """
    Basic health check endpoint.
    
    Returns:
        dict: Status message
    """
    return {"status": "healthy"}