from src.settings.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False, index=True)
    issuer_id = Column(Integer, nullable=False, index=True)
    customer_id = Column(Integer, nullable=False, index=True)
    coffee_shop_id = Column(Integer, nullable=False, index=True)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
