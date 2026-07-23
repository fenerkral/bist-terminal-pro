import React, { useState, useEffect } from 'react';
import Header from './Header';
import MarketSummary from './MarketSummary';
import ScannerTabs from './ScannerTabs';
import StockList from './StockList';
import Sidebar from './Sidebar';

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

const Dashboard: React.FC = () => {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [selectedScanner, setSelectedScanner] = useState('harmonik');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const mockStocks: Stock[] = [
      {
        id: '1',
        code: 'GARAN',
        name: 'Garanti BBVA',
        price: 111.30,
        change: 3,
        changePercent: 2.94,
        volume: 100000000,
        rsi: 59,
        score: 89,
        reason: 'Harmonik kalıp (Gartley), Düşen tepeyi kırmaya hazır'
      },
      {
        id: '2',
        code: 'ASELS',
        name: 'Aselsan',
        price: 116.00,
        change: -3,
        changePercent: -2.52,
        volume: 50000000,
        rsi: 71,
        score: 95,
        reason: 'FVG Kırılım, Gaplar test edildi'
      },
      {
        id: '3',
        code: 'KRDMD',
        name: 'Kredim',
        price: 40.98,
        change: 1,
        changePercent: 2.50,
        volume: 30000000,
        rsi: 65,
        score: 87,
        reason: 'VCP Formasyonu, Hacim Artışı'
      },
    ];

    setStocks(mockStocks);
    setLoading(false);
  }, []);

  return (
    <div className="flex bg-dark min-h-screen">
      <Sidebar />
      <div className="flex-1 overflow-auto">
        <Header />
        <div className="p-6 space-y-6">
          <MarketSummary />
          <ScannerTabs selectedScanner={selectedScanner} setSelectedScanner={setSelectedScanner} />
          <StockList stocks={stocks} loading={loading} />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
