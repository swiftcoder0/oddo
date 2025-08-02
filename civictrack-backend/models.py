from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from .database import Base

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    category = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    status = Column(String, default="Reported")
    flagged = Column(Integer, default=0)
    anonymous = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)