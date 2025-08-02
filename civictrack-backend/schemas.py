from pydantic import BaseModel
from datetime import datetime

class IssueCreate(BaseModel):
    title: str
    description: str
    category: str
    latitude: float
    longitude: float
    anonymous: bool

class IssueResponse(IssueCreate):
    id: int
    status: str
    flagged: int
    created_at: datetime

    class Config:
        orm_mode = True