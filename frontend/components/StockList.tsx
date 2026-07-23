import React from 'react';

interface Stock {
  id: string;
  code: string;
  name: string;
  price: number;
  change: number;
  changePercent: number;
  volume: number;
  rsi: number;
  score: number;
  reason: string;
}

interface StockListProps {
  stocks: Stock[];
  loading: boolean;
}

const StockList: React.FC<StockListProps> = ({ stocks, loading }) => {
  if (loading) {
    return <div className="text-center text-gray-400">Veriler yükleniyor...</div>;
  }

  return (
    <div className="space-y-3">
      <h2 className="text-primary font-bold mb-4">🎯 TAVAN POTANSİYELİ</h2>
      {stocks.map((stock) => (
        <div
          key={stock.id}
          className="bg-dark-light border border-dark-lighter rounded-lg p-4 hover:border-primary transition cursor-pointer"
        >
          <div className="flex justify-between items-start">
            <div className="flex-1">
              <h3 className="font-bold text-lg text-white">{stock.code}</h3>
              <p className="text-gray-400 text-sm">{stock.name}</p>
              <p className="text-gray-500 text-sm mt-2">🔍 {stock.reason}</p>
            </div>
            <div className="text-right">
              <div className="text-2xl font-bold text-primary">{stock.score}</div>
              <div className="text-sm text-gray-400">SKOR</div>
            </div>
          </div>
          <div className="mt-3 grid grid-cols-4 gap-2 text-xs">
            <div className="bg-dark-lighter p-2 rounded">
              <p className="text-gray-400">Fiyat</p>
              <p className="font-bold text-primary">{stock.price.toFixed(2)} ₺</p>
            </div>
            <div className="bg-dark-lighter p-2 rounded">
              <p className="text-gray-400">Değişim</p>
              <p className={`font-bold ${stock.change >= 0 ? 'text-primary' : 'text-danger'}`}>
                {stock.change >= 0 ? '+' : ''}{stock.changePercent.toFixed(2)}%
              </p>
            </div>
            <div className="bg-dark-lighter p-2 rounded">
              <p className="text-gray-400">RSI</p>
              <p className="font-bold text-info">{stock.rsi}</p>
            </div>
            <div className="bg-dark-lighter p-2 rounded">
              <p className="text-gray-400">Hacim</p>
              <p className="font-bold text-warning">{(stock.volume / 1000000).toFixed(1)}M</p>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default StockList;
