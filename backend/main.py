from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
from database import init_db

# Mock routes
from routes import stocks, scanners, alerts

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("✅ BIST Terminal Pro başlatılıyor...")
    await init_db()
    print("✅ Veritabanı hazır")
    yield
    # Shutdown
    print("❌ Uygulama kapanıyor")

app = FastAPI(
    title="BIST Terminal Pro API",
    description="Gerçek zamanlı Borsa İstanbul hisse analiz API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(stocks.router, prefix="/api/stocks", tags=["Hisseler"])
app.include_router(scanners.router, prefix="/api/scanners", tags=["Taramalar"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["Uyarılar"])

@app.get("/")
async def root():
    return {
        "message": "BIST Terminal Pro API",
        "version": "1.0.0",
        "status": "🟢 Çalışıyor",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    return {"status": "✅ Sağlıklı"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
