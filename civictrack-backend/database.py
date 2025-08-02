from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Local SQLite database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./civictrack.db"

# Engine talks to DB
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Creates sessions (connections) to DB
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for all models
Base = declarative_base()