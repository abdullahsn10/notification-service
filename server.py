from uvicorn import run
from src.main import app
from src.consumer.rabbitmq import RabbitMQConsumer
from src.settings.settings import RABBITMQ_HOST, ORDER_NOTIFICATION_QUEUE
import threading


def start_consumer():
    """
    Start the RabbitMQ consumer in a separate thread
    """
    consumer = RabbitMQConsumer(host=RABBITMQ_HOST, queue_name=ORDER_NOTIFICATION_QUEUE)
    consumer_thread = threading.Thread(target=consumer.start_consuming)
    consumer_thread.start()


if __name__ == "__main__":
    start_consumer()
    run(app, host="0.0.0.0", port=8855)
