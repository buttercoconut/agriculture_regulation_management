from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import Base

class RegulationCategory(Base):
    __tablename__ = "regulation_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    regulations = relationship("Regulation", back_populates="category")

class Regulation(Base):
    __tablename__ = "regulations"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey("regulation_categories.id"))
    category = relationship("RegulationCategory", back_populates="regulations")
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class Farmer(Base):
    __tablename__ = "farmers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    phone = Column(String(20))
    notifications = relationship("Notification", back_populates="farmer")

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"))
    regulation_id = Column(Integer, ForeignKey("regulations.id"))
    message = Column(Text, nullable=False)
    sent_at = Column(DateTime)
    farmer = relationship("Farmer", back_populates="notifications")
    regulation = relationship("Regulation")
