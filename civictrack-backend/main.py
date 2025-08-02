from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from .database import SessionLocal, engine
import math
from fastapi.middleware.cors import CORSMiddleware

# Create tables if not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# DB Session Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Distance Filter (Haversine)
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in KM
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = (math.sin(d_lat/2)**2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(d_lon/2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# POST /issues → create new issue
@app.post("/issues", response_model=schemas.IssueResponse)
def create_issue(issue: schemas.IssueCreate, db: Session = Depends(get_db)):
    db_issue = models.Issue(**issue.dict())
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue

# GET /issues → nearby filtering
@app.get("/issues", response_model=list[schemas.IssueResponse])
def get_issues(lat: float, lng: float, radius: int = 3, db: Session = Depends(get_db)):
    all_issues = db.query(models.Issue).all()
    nearby = []
    for issue in all_issues:
        distance = calculate_distance(lat, lng, issue.latitude, issue.longitude)
        if distance <= radius:
            # Add distance to the response
            issue_dict = issue.__dict__
            issue_dict["distance"] = distance
            nearby.append(issue_dict)
    return nearby

# PUT /issues/{id}/status → update status
@app.put("/issues/{issue_id}/status")
def update_status(issue_id: int, status_data: dict, db: Session = Depends(get_db)):
    issue = db.query(models.Issue).filter(models.Issue.id == issue_id).first()
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    issue.status = status_data.get("status", "Reported")
    db.commit()
    return {"message": "Status updated"}

# POST /issues/{id}/flag → increase spam counter
@app.post("/issues/{issue_id}/flag")
def flag_issue(issue_id: int, db: Session = Depends(get_db)):
    issue = db.query(models.Issue).filter(models.Issue.id == issue_id).first()
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    issue.flagged += 1
    db.commit()
    return {"message": "Issue flagged"}

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "CivicTrack API is running"}