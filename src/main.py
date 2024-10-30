from fastapi import FastAPI
from src.routers import notification
from src.settings.settings import OPENAPI_URL, ROOT_PATH

app = FastAPI(
    openapi_url=OPENAPI_URL,
    root_path=ROOT_PATH,
)


# register routes
app.include_router(notification.router)
