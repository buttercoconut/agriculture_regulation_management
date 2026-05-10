from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..services import NotificationService
from ..schemas import NotificationCreate, Notification
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=Notification, status_code=status.HTTP_201_CREATED)
async def send_notification(notification_in: NotificationCreate, db: AsyncSession = Depends(get_db)):
    service = NotificationService(db)
    notification = await service.send_notification(notification_in.farmer_id, notification_in.regulation_id, notification_in.message)
    return notification
