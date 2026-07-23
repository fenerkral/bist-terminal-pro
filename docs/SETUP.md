# BIST Terminal Pro - Kurulum Rehberi

## Hızlı Başlangıç

### Docker ile (Önerilen)

```bash
# Repository'yi klonla
git clone https://github.com/fenerkral/bist-terminal-pro.git
cd bist-terminal-pro

# Tüm servisleri başlat
docker-compose up --build
```

**Erişim:**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Manuel Kurulum

#### Backend

```bash
cd backend

# Virtual environment oluştur
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\\Scripts\\activate  # Windows

# Bağımlılıkları yükle
pip install -r requirements.txt

# Sunucuyu başlat
python main.py
```

#### Frontend

```bash
cd frontend

# Bağımlılıkları yükle
npm install

# Geliştirme sunucusunu başlat
npm run dev
```

## Kullanım

### API Test Etme

```bash
# Hisseleri getir
curl http://localhost:8000/api/stocks/

# Tarama çalıştır
curl -X POST http://localhost:8000/api/scanners/run \
  -H "Content-Type: application/json" \
  -d '{"scanner_type": "harmonik"}'

# Uyarı oluştur
curl -X POST http://localhost:8000/api/alerts/ \
  -H "Content-Type: application/json" \
  -d '{"stock_id": "1", "alert_type": "price_above", "price_target": 115.0}'
```

## Mimarı

```
bist-terminal-pro/
├── frontend/              # Next.js React uygulaması
│   ├── pages/            # Sayfa bileşenleri
│   ├── components/       # Yeniden kullanılabilir bileşenler
│   ├── styles/           # Global CSS
│   └── package.json
├── backend/              # FastAPI sunucusu
│   ├── routes/           # API rotaları
│   ├── main.py           # Ana uygulama
│   ├── database.py       # Veritabanı modeli
│   └── requirements.txt
├── docs/                 # Dokümantasyon
└── docker-compose.yml    # Docker konfigürasyonu
```

## Teknoloji Stack

- **Frontend:** Next.js 14, React 18, TypeScript, Tailwind CSS
- **Backend:** FastAPI, Python 3.11, SQLAlchemy
- **Database:** PostgreSQL / SQLite
- **Deployment:** Docker, Docker Compose

## Özellikleri

✅ Gerçek zamanlı BIST 100/30/50 verisi
✅ 8+ Teknik Analiz Taraması
✅ Hisse detay sayfaları
✅ Favoriler ve Uyarı sistemi
✅ Grafik ve indikatörler
✅ Responsive tasarım

## Katkı

Katkılarınızı kabul ediyoruz! Lütfen:
1. Fork edin
2. Feature branch oluşturun
3. Commit edin
4. Pull request gönderin

## Lisans

MIT

## Destek

Sorular veya sorunlar için GitHub Issues'i açın.
