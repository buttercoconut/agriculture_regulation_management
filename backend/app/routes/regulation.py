from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..services import RegulationService
from ..schemas import Regulation, RegulationCreate
from ..models import Regulation as RegulationModel
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=list[Regulation])
async def search_regulations(keyword: str | None = None, category_id: int | None = None, db: AsyncSession = Depends(get_db)):
    service = RegulationService(db)
    regulations = await service.search(keyword, category_id)
    return regulations

@router.get("/{regulation_id}", response_model=Regulation)
async def get_regulation(regulation_id: int, db: AsyncSession = Depends(get_db)):
    service = RegulationService(db)
    regulation = await service.get(regulation_id)
    if not regulation:
        raise HTTPException(status_code=404, detail="Regulation not found")
    return regulation

@router.post("/", response_model=Regulation, status_code=status.HTTP_201_CREATED)
async def create_regulation(regulation_in: RegulationCreate, db: AsyncSession = Depends(get_db)):
    service = RegulationService(db)
    regulation = await service.create(regulation_in)
    return regulation
