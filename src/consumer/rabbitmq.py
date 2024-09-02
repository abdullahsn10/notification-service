import pika
import json
from src.models.notification import Notification
from src.settings.database import db


class RabbitMQConsumer:
    def __init__(
        self,
        host: str = "localhost",
        queue_name: str = "order_notification",
    ):
        self.host = host
        self.queue_name = queue_name
        self.connection = None
        self.channel = None
        self.db = db

    def _connect(self):
        if self.connection is None or self.connection.is_closed:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(self.host)
            )
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.queue_name, durable=True)

    def _consume_callback(self, ch, method, properties, body):
        message = json.loads(body)
        self._store_notification(message)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def _store_notification(self, message):
        try:
            notification = Notification(
                order_id=message["order_id"],
                issuer_id=message["issuer_id"],
                customer_id=message["customer_id"],
                message=message["message"],
                created_at=message["created_at"],
            )
            self.db.add(notification)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def start_consuming(self):
        self._connect()
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self._consume_callback
        )
        print(f"[*] Waiting for messages in {self.queue_name}. To exit press CTRL+C")
        self.channel.start_consuming()

    def close(self):
        if self.connection is not None and not self.connection.is_closed:
            self.connection.close()
