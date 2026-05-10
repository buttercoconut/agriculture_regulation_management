from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from datetime import datetime
from ..models import Regulation, RegulationCategory, Farmer, Notification
from ..schemas import RegulationCreate, Regulation, FarmerCreate, Farmer, NotificationCreate, Notification

class RegulationService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def search(self, keyword: str | None = None, category_id: int | None = None):
        stmt = select(Regulation).join(RegulationCategory)
        if keyword:
            stmt = stmt.where(or_(Regulation.title.ilike(f"%{keyword}%"), Regulation.content.ilike(f"%{keyword}%")))
        if category_id:
            stmt = stmt.where(Regulation.category_id == category_id)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get(self, regulation_id: int):
        stmt = select(Regulation).where(Regulation.id == regulation_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, regulation_in: RegulationCreate):
        regulation = Regulation(**regulation_in.dict(), created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        self.db.add(regulation)
        await self.db.commit()
        await self.db.refresh(regulation)
        return regulation

class NotificationService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def send_notification(self, farmer_id: int, regulation_id: int, message: str):
        notification = Notification(farmer_id=farmer_id, regulation_id=regulation_id, message=message, sent_at=datetime.utcnow())
        self.db.add(notification)
        await self.db.commit()
        await self.db.refresh(notification)
        return notification
