from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, Alert
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uuid

router = APIRouter()

class AlertSchema(BaseModel):
    id: str
    stock_id: str
    alert_type: str
    price_target: float
    is_active: bool

class AlertCreateSchema(BaseModel):
    stock_id: str
    alert_type: str
    price_target: float

# Mock uyarılar
MOCK_ALERTS = [
    {
        "id": "a1",
        "stock_id": "1",
        "alert_type": "price_above",
        "price_target": 115.00,
        "is_active": True
    },
    {
        "id": "a2",
        "stock_id": "2",
        "alert_type": "price_below",
        "price_target": 110.00,
        "is_active": True
    },
    {
        "id": "a3",
        "stock_id": "3",
        "alert_type": "volume_spike",
        "price_target": 0.0,
        "is_active": True
    },
]

@router.get("/", response_model=List[AlertSchema])
async def get_alerts(db: Session = Depends(get_db), active_only: bool = True):
    """Uyarıları getir"""
    if active_only:
        return [a for a in MOCK_ALERTS if a["is_active"]]
    return MOCK_ALERTS

@router.post("/", response_model=AlertSchema)
async def create_alert(alert: AlertCreateSchema, db: Session = Depends(get_db)):
    """Yeni uyarı oluştur"""
    new_alert = {
        "id": str(uuid.uuid4()),
        "is_active": True,
        **alert.dict()
    }
    MOCK_ALERTS.append(new_alert)
    return new_alert

@router.delete("/{alert_id}")
async def delete_alert(alert_id: str, db: Session = Depends(get_db)):
    """Uyarıyı sil"""
    global MOCK_ALERTS
    MOCK_ALERTS = [a for a in MOCK_ALERTS if a["id"] != alert_id]
    return {"status": "✅ Uyarı silindi", "alert_id": alert_id}

@router.put("/{alert_id}")
async def update_alert(alert_id: str, alert: AlertCreateSchema, db: Session = Depends(get_db)):
    """Uyarıyı güncelle"""
    for a in MOCK_ALERTS:
        if a["id"] == alert_id:
            a.update(alert.dict())
            return a
    return {"error": "Uyarı bulunamadı"}

@router.post("/{alert_id}/disable")
async def disable_alert(alert_id: str, db: Session = Depends(get_db)):
    """Uyarıyı devre dışı bırak"""
    for a in MOCK_ALERTS:
        if a["id"] == alert_id:
            a["is_active"] = False
            return a
    return {"error": "Uyarı bulunamadı"}
