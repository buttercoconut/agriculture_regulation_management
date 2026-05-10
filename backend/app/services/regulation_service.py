from sqlalchemy.orm import Session
from .. import models, schemas
from sqlalchemy import or_

class RegulationService:
    async def search_regulations(self, db: Session, keyword: str):
        return db.query(models.Regulation).filter(
            or_(models.Regulation.title.ilike(f"%{keyword}%"), models.Regulation.content.ilike(f"%{keyword}%"))
        ).all()

    async def get_regulation(self, db: Session, regulation_id: int):
        return db.query(models.Regulation).filter(models.Regulation.id == regulation_id).first()

regulation_service = RegulationService()
