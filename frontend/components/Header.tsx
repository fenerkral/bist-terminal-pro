import React, { useState, useEffect } from 'react';

const Header: React.FC = () => {
  const [time, setTime] = useState<string>('');

  useEffect(() => {
    const updateTime = () => {
      const now = new Date();
      setTime(now.toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' }));
    };
    updateTime();
    const interval = setInterval(updateTime, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="bg-dark-light border-b border-dark-lighter p-4 flex justify-between items-center">
      <div className="flex items-center space-x-4">
        <h1 className="text-2xl font-bold text-primary">📊 BİST TERMİNAL</h1>
        <span className="text-gray-400">Merhaba Eray 👋</span>
      </div>
      <div className="flex items-center space-x-4">
        <span className="text-2xl font-mono text-primary">{time}</span>
        <span className="text-gray-400 text-sm">23 Temmuz Perşembe</span>
      </div>
    </div>
  );
};

export default Header;
