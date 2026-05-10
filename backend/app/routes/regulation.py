from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, services
from ..database import get_db

router = APIRouter(prefix="/regulations", tags=["regulations"])

@router.get("/search", response_model=List[schemas.Regulation])
async def search_regulations(keyword: str, db: Session = Depends(get_db)):
    return await services.regulation_service.search_regulations(db, keyword)

@router.get("/{regulation_id}", response_model=schemas.Regulation)
async def get_regulation(regulation_id: int, db: Session = Depends(get_db)):
    regulation = await services.regulation_service.get_regulation(db, regulation_id)
    if not regulation:
        raise HTTPException(status_code=404, detail="Regulation not found")
    return regulation

# Additional CRUD endpoints can be added here
