from pydantic import BaseModel, Field
from datetime import datetime

class RegulationCategoryBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: str | None = None

class RegulationCategoryCreate(RegulationCategoryBase):
    pass

class RegulationCategory(RegulationCategoryBase):
    id: int
    class Config:
        orm_mode = True

class RegulationBase(BaseModel):
    title: str
    content: str
    category_id: int

class RegulationCreate(RegulationBase):
    pass

class Regulation(RegulationBase):
    id: int
    created_at: datetime
    updated_at: datetime
    category: RegulationCategory
    class Config:
        orm_mode = True

class FarmerBase(BaseModel):
    name: str
    email: str
    phone: str | None = None

class FarmerCreate(FarmerBase):
    pass

class Farmer(FarmerBase):
    id: int
    class Config:
        orm_mode = True

class NotificationBase(BaseModel):
    farmer_id: int
    regulation_id: int
    message: str

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int
    sent_at: datetime | None = None
    class Config:
        orm_mode = True
