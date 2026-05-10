from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base

class RegulationCategory(Base):
    __tablename__ = "regulation_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    regulations = relationship("Regulation", back_populates="category")

class Regulation(Base):
    __tablename__ = "regulations"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey("regulation_categories.id"))
    category = relationship("RegulationCategory", back_populates="regulations")
    created_at = Column(DateTime, server_default="now()")
    updated_at = Column(DateTime, server_default="now()", onupdate="now()")
    histories = relationship("RegulationHistory", back_populates="regulation")

class RegulationHistory(Base):
    __tablename__ = "regulation_histories"
    id = Column(Integer, primary_key=True, index=True)
    regulation_id = Column(Integer, ForeignKey("regulations.id"))
    regulation = relationship("Regulation", back_populates="histories")
    changed_at = Column(DateTime, server_default="now()")
    change_description = Column(Text)
