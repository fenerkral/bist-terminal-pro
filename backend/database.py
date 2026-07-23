from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./bist_terminal.db")

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(String, primary_key=True)
    code = Column(String, unique=True, index=True)
    name = Column(String)
    price = Column(Float)
    change = Column(Float)
    change_percent = Column(Float)
    volume = Column(Integer)
    rsi = Column(Float)
    score = Column(Integer)
    updated_at = Column(DateTime, default=datetime.utcnow)

class ScanResult(Base):
    __tablename__ = "scan_results"
    id = Column(String, primary_key=True)
    stock_id = Column(String, index=True)
    scanner_type = Column(String)
    score = Column(Integer)
    reason = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(String, primary_key=True)
    stock_id = Column(String, index=True)
    alert_type = Column(String)
    price_target = Column(Float)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

async def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
