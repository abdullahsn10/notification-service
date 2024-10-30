import os
from dotenv import load_dotenv


# load environment variables
load_dotenv()

# load database settings
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_SERVICE = os.getenv("DB_SERVICE")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# database url
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_SERVICE}/{POSTGRES_DB}"
)

# database settings
DATABASE_SETTINGS = {
    "URL": SQLALCHEMY_DATABASE_URL,
}

# security settings
PUBLIC_KEY = os.getenv("PUBLIC_KEY")


JWT_TOKEN_SETTINGS = {
    "PUBLIC_KEY": PUBLIC_KEY,
    "ALGORITHM": os.getenv("ALGORITHM"),
    "ACCESS_TOKEN_EXPIRE_MINUTES": os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"),
}


# RabbitMQ and Order-Notification settings
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
ORDER_NOTIFICATION_QUEUE = os.getenv("ORDER_NOTIFICATION_QUEUE")
