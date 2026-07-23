from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, Stock
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uuid

router = APIRouter()

class StockSchema(BaseModel):
    id: str
    code: str
    name: str
    price: float
    change: float
    change_percent: float
    volume: int
    rsi: float
    score: int

class StockCreateSchema(BaseModel):
    code: str
    name: str
    price: float
    change: float
    change_percent: float
    volume: int
    rsi: float
    score: int

# Mock veri
MOCK_STOCKS = [
    {
        "id": "1",
        "code": "GARAN",
        "name": "Garanti BBVA",
        "price": 111.30,
        "change": 3.0,
        "change_percent": 2.94,
        "volume": 100000000,
        "rsi": 59,
        "score": 89
    },
    {
        "id": "2",
        "code": "ASELS",
        "name": "Aselsan",
        "price": 116.00,
        "change": -3.0,
        "change_percent": -2.52,
        "volume": 50000000,
        "rsi": 71,
        "score": 95
    },
    {
        "id": "3",
        "code": "KRDMD",
        "name": "Kredim",
        "price": 40.98,
        "change": 1.0,
        "change_percent": 2.50,
        "volume": 30000000,
        "rsi": 65,
        "score": 87
    },
    {
        "id": "4",
        "code": "ISBANK",
        "name": "İşbank",
        "price": 88.50,
        "change": 2.5,
        "change_percent": 2.90,
        "volume": 75000000,
        "rsi": 62,
        "score": 92
    },
    {
        "id": "5",
        "code": "AKBNK",
        "name": "Akbank",
        "price": 95.20,
        "change": -1.5,
        "change_percent": -1.55,
        "volume": 60000000,
        "rsi": 58,
        "score": 85
    },
]

@router.get("/", response_model=List[StockSchema])
async def get_stocks(limit: int = 50, db: Session = Depends(get_db)):
    """Tüm hisseleri getir"""
    return MOCK_STOCKS[:limit]

@router.get("/{code}", response_model=StockSchema)
async def get_stock(code: str, db: Session = Depends(get_db)):
    """Belirli bir hisseyi getir"""
    for stock in MOCK_STOCKS:
        if stock["code"] == code:
            return stock
    return {"error": "Hisse bulunamadı"}

@router.post("/", response_model=StockSchema)
async def create_stock(stock: StockCreateSchema, db: Session = Depends(get_db)):
    """Yeni hisse ekle"""
    new_stock = {
        "id": str(uuid.uuid4()),
        **stock.dict()
    }
    MOCK_STOCKS.append(new_stock)
    return new_stock

@router.get("/top/gainers")
async def get_top_gainers():
    """En çok kazananları getir"""
    sorted_stocks = sorted(MOCK_STOCKS, key=lambda x: x["change_percent"], reverse=True)
    return sorted_stocks[:10]

@router.get("/top/losers")
async def get_top_losers():
    """En çok kaybedenleri getir"""
    sorted_stocks = sorted(MOCK_STOCKS, key=lambda x: x["change_percent"])
    return sorted_stocks[:10]
