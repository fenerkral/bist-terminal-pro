from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, ScanResult
from pydantic import BaseModel
from typing import List
from datetime import datetime
import uuid

router = APIRouter()

class ScanResultSchema(BaseModel):
    id: str
    stock_id: str
    scanner_type: str
    score: int
    reason: str

class ScanRunSchema(BaseModel):
    scanner_type: str

# Mock tarama sonuçları
MOCK_SCAN_RESULTS = [
    {
        "id": "s1",
        "stock_id": "1",
        "scanner_type": "harmonik",
        "score": 89,
        "reason": "Harmonik kalıp (Gartley) tespit edildi. Düşen tepeyi kırmaya hazır"
    },
    {
        "id": "s2",
        "stock_id": "2",
        "scanner_type": "fvg",
        "score": 95,
        "reason": "FVG kırılımı tamamlandı. Gaplar test edildi, momentum yükselişte"
    },
    {
        "id": "s3",
        "stock_id": "3",
        "scanner_type": "vcp",
        "score": 87,
        "reason": "VCP formasyonu sona yaklaşıyor. Hacim artışı gözlendi"
    },
    {
        "id": "s4",
        "stock_id": "1",
        "scanner_type": "ortak-al",
        "score": 88,
        "reason": "Ortak AL sinyali oluştu. RSI 59 seviyesinde, Hacim +9.7"
    },
    {
        "id": "s5",
        "stock_id": "4",
        "scanner_type": "everest",
        "score": 92,
        "reason": "Everest formasyonu aktif. Trend filtresi boğa + kısa-orta-uzun taramaları yükselişte"
    },
]

@router.get("/", response_model=List[ScanResultSchema])
async def get_all_scans(db: Session = Depends(get_db)):
    """Tüm tarama sonuçlarını getir"""
    return MOCK_SCAN_RESULTS

@router.get("/{scanner_type}", response_model=List[ScanResultSchema])
async def get_scan_results(scanner_type: str, db: Session = Depends(get_db)):
    """Belirli scanner taramasının sonuçlarını getir"""
    results = [s for s in MOCK_SCAN_RESULTS if s["scanner_type"] == scanner_type]
    return results

@router.post("/run")
async def run_scan(scan: ScanRunSchema, db: Session = Depends(get_db)):
    """Tarama çalıştır"""
    results = [s for s in MOCK_SCAN_RESULTS if s["scanner_type"] == scan.scanner_type]
    return {
        "status": "✅ Tarama başarıyla tamamlandı",
        "scanner": scan.scanner_type,
        "stocks_found": len(results),
        "results": results
    }

@router.get("/top/harmonic")
async def get_harmonic_scans():
    """Harmonik taramalarını getir"""
    return [s for s in MOCK_SCAN_RESULTS if s["scanner_type"] == "harmonik"]

@router.get("/top/fvg")
async def get_fvg_scans():
    """FVG taramalarını getir"""
    return [s for s in MOCK_SCAN_RESULTS if s["scanner_type"] == "fvg"]

@router.get("/top/vcp")
async def get_vcp_scans():
    """VCP taramalarını getir"""
    return [s for s in MOCK_SCAN_RESULTS if s["scanner_type"] == "vcp"]
