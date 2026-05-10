from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"))
    farmer = relationship("Farmer", back_populates="notifications")
    regulation_id = Column(Integer, ForeignKey("regulations.id"))
    regulation = relationship("Regulation")
    message = Column(Text)
    sent_at = Column(DateTime, server_default="now()")
    read = Column(Integer, default=0)
