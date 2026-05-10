# notification_service placeholder
from sqlalchemy.orm import Session
from .. import models, schemas

class NotificationService:
    async def send_notification(self, db: Session, farmer_id: int, regulation_id: int, message: str):
        notification = models.Notification(
            farmer_id=farmer_id,
            regulation_id=regulation_id,
            message=message
        )
        db.add(notification)
        db.commit()
        db.refresh(notification)
        return notification

notification_service = NotificationService()
