import React from 'react';

const MarketSummary: React.FC = () => {
  const indices = [
    { name: 'BİST 100', value: 14077.60, change: -0.43 },
    { name: 'BİST 30', value: 16017.94, change: -0.54 },
    { name: 'Dolar', value: 47.23, change: 0.09 },
    { name: 'Euro', value: 52.15, change: 0.05 },
  ];

  const sectors = [
    { name: 'Madencilik', change: 4.92 },
    { name: 'Metal Eşya', change: 2.42 },
    { name: 'Teknoloji', change: 1.34 },
  ];

  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-4">
      {indices.map((idx, i) => (
        <div key={i} className="bg-dark-light border border-dark-lighter rounded-lg p-4">
          <h3 className="text-gray-400 text-sm mb-2">{idx.name}</h3>
          <div className="flex items-end justify-between">
            <span className="text-2xl font-bold text-white">{idx.value.toLocaleString('tr-TR')}</span>
            <span className={`text-lg font-semibold ${idx.change >= 0 ? 'text-primary' : 'text-danger'}`}>
              {idx.change >= 0 ? '+' : ''}{idx.change.toFixed(2)}%
            </span>
          </div>
        </div>
      ))}

      <div className="lg:col-span-4 bg-dark-light border border-dark-lighter rounded-lg p-4">
        <h3 className="text-primary mb-3 font-semibold">🏭 SEKTÖRLER - BUGÜN GÜCÜ DÜŞTÜ ZAYIFA</h3>
        <div className="flex flex-wrap gap-3">
          {sectors.map((sec, i) => (
            <span key={i} className="bg-dark-lighter px-3 py-1 rounded text-sm">
              {sec.name} <span className="text-primary font-bold">+{sec.change.toFixed(2)}%</span>
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};

export default MarketSummary;
