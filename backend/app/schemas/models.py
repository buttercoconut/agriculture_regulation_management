from pydantic import BaseModel, Field
from typing import List, Optional

class RegulationCategoryBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: Optional[str] = None

class RegulationCategoryCreate(RegulationCategoryBase):
    pass

class RegulationCategory(RegulationCategoryBase):
    id: int
    class Config:
        orm_mode = True

class RegulationBase(BaseModel):
    title: str = Field(..., max_length=255)
    content: str
    category_id: int

class RegulationCreate(RegulationBase):
    pass

class Regulation(RegulationBase):
    id: int
    created_at: str
    updated_at: str
    category: RegulationCategory
    class Config:
        orm_mode = True

class RegulationHistoryBase(BaseModel):
    change_description: str

class RegulationHistoryCreate(RegulationHistoryBase):
    regulation_id: int

class RegulationHistory(RegulationHistoryBase):
    id: int
    changed_at: str
    regulation: Regulation
    class Config:
        orm_mode = True

class FarmerBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None

class FarmerCreate(FarmerBase):
    pass

class Farmer(FarmerBase):
    id: int
    class Config:
        orm_mode = True

class NotificationBase(BaseModel):
    message: str
    regulation_id: int

class NotificationCreate(NotificationBase):
    farmer_id: int

class Notification(NotificationBase):
    id: int
    sent_at: str
    farmer: Farmer
    class Config:
        orm_mode = True
