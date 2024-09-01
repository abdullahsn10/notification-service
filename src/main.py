from fastapi import FastAPI
from src.routers import notification

app = FastAPI()

# register routes
app.include_router(notification.router)
