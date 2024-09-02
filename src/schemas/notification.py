from datetime import datetime
from pydantic import BaseModel


class NotificationResponse(BaseModel):
    """
    Notification Pydantic model
    """

    order_id: int
    issuer_id: int
    customer_id: int
    message: str
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True


class PaginatedNotificationResponse(BaseModel):
    """
    Paginated Notification Pydantic model
    """

    total_count: int
    page: int
    page_size: int
    notifications: list[NotificationResponse]
