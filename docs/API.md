# BIST Terminal Pro API Dokümantasyonu

## Base URL
```
http://localhost:8000
```

## Hisseler Endpoints

### GET /api/stocks/
Tüm hisseleri getir

**Query Parameters:**
- `limit` (int): Sonuç sayısı (default: 50)

**Response:**
```json
[
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
  }
]
```

### GET /api/stocks/{code}
Belirli hisseyi getir

### POST /api/stocks/
Yeni hisse ekle

### GET /api/stocks/top/gainers
En çok kazananları getir

### GET /api/stocks/top/losers
En çok kaybedenleri getir

## Taramalar Endpoints

### GET /api/scanners/
Tüm tarama sonuçlarını getir

### GET /api/scanners/{scanner_type}
Belirli scanner sonuçlarını getir

**Scanner Types:**
- `harmonik` - Harmonik Kalıpları
- `fvg` - Fair Value Gap
- `kiran` - Kıran Taraması
- `ortak-al` - Ortak AL
- `everest` - Everest Formasyonu
- `vcp` - Volatility Contraction Pattern
- `tavan` - Tavan Potansiyeli
- `mum` - Mum Formasyonu

### POST /api/scanners/run
Tarama çalıştır

```json
{
  "scanner_type": "harmonik"
}
```

## Uyarılar Endpoints

### GET /api/alerts/
Uyarıları getir

**Query Parameters:**
- `active_only` (bool): Sadece aktif uyarılar (default: true)

### POST /api/alerts/
Yeni uyarı oluştur

```json
{
  "stock_id": "1",
  "alert_type": "price_above",
  "price_target": 115.00
}
```

### DELETE /api/alerts/{alert_id}
Uyarıyı sil

### POST /api/alerts/{alert_id}/disable
Uyarıyı devre dışı bırak

## Canlı API Test

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
