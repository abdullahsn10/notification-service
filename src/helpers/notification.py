from src import models, schemas
from sqlalchemy.orm import Session


def _find_all_notifications(
    db: Session,
    size: int,
    page: int,
    sort: str = None,
    coffee_shop_id: int = None,
) -> tuple[list[models.Notification], int]:
    """
    This helper function used to find all notifications for a specific coffee shop, apply pagination
    and return the total count of notifications
    *Args:
        db (Session): a database session
        coffee_shop_id (int): id of the coffee shop to find the notifications for
        size (int): the maximum limit of notifications to return in the page
        page (int): the page number, needed to calculate the offset to skip
        sort (str): the sort order of the notifications
    *Returns:
        tuple of list of Notification instances and the total count of notifications
    """

    query = db.query(models.Notification)

    if coffee_shop_id:
        query = query.filter(models.Notification.coffee_shop_id == coffee_shop_id)
    if sort == "latest":
        query = query.order_by(models.Notification.created_at.desc())
    elif sort == "oldest":
        query = query.order_by(models.Notification.created_at.asc())

    # total count of notifications
    total_count: int = query.count()

    # apply pagination
    offset = (page - 1) * size
    notifications = query.offset(offset).limit(size).all()

    return notifications, total_count


def get_all_notifications(
    db: Session, coffee_shop_id: int, page: int, size: int, sort: str
) -> schemas.PaginatedNotificationResponse:
    """
    This helper function used to get all notifications for a specific coffee shop
    *Args:
        db (Session): a database session
        coffee_shop_id (int): id of the coffee shop to find the notifications for
        size (int): the maximum limit of notifications to return in the page
        page (int): the page number, needed to calculate the offset to skip
        sort (str): the sort order of the notifications
    *Returns:
        PaginatedNotificationResponse instance
    """

    notifications, total_count = _find_all_notifications(
        db=db, coffee_shop_id=coffee_shop_id, size=size, page=page, sort=sort
    )

    return schemas.PaginatedNotificationResponse(
        total_count=total_count,
        page=page,
        page_size=size,
        notifications=notifications,
    )
