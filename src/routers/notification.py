from fastapi import APIRouter, Query, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.settings.database import get_db
from src.security.roles import UserRole
from src.security.oauth2 import require_role
from src.utils.control_access import check_if_user_can_access_shop
from src.exceptions.exception import NotificationServiceException
from src.helpers import notification
from src import schemas

router = APIRouter(
    tags=["Notifications"],
    prefix="/notifications",
)


@router.get(
    "/coffee-shops/{coffee_shop_id}/",
    response_model=schemas.PaginatedNotificationResponse,
)
def get_all_notifications_endpoint(
    coffee_shop_id: int,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1),
    sort: str = Query(None, regex="^(latest|oldest)$"),
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(
        require_role([UserRole.ADMIN, UserRole.CASHIER])
    ),
):
    """
    GET endpoint to get all notifications for a specific coffee shop.
    """
    try:
        check_if_user_can_access_shop(
            user_coffee_shop_id=current_user.coffee_shop_id,
            target_coffee_shop_id=coffee_shop_id,
        )
        return notification.get_all_notifications(
            db=db,
            coffee_shop_id=coffee_shop_id,
            sort=sort,
            page=page,
            size=size,
        )
    except NotificationServiceException as se:
        raise HTTPException(status_code=se.status_code, detail=se.message)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
