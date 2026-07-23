import React from 'react';

interface ScannerTabsProps {
  selectedScanner: string;
  setSelectedScanner: (scanner: string) => void;
}

const ScannerTabs: React.FC<ScannerTabsProps> = ({ selectedScanner, setSelectedScanner }) => {
  const scanners = [
    { id: 'harmonik', label: '🎯 Harmonik' },
    { id: 'fvg', label: '📍 FVG' },
    { id: 'kiran', label: '🔴 Kıran' },
    { id: 'ortak-al', label: '💚 Ortak AL' },
    { id: 'everest', label: '⛰️ Everest' },
    { id: 'vcp', label: '📦 VCP' },
    { id: 'tavan', label: '🎪 Tavan' },
    { id: 'mum', label: '🕯️ Mum' },
  ];

  return (
    <div className="bg-dark-light border border-dark-lighter rounded-lg p-4">
      <h2 className="text-primary font-bold mb-4">🔍 TARAMA MODÜLÜ</h2>
      <div className="flex flex-wrap gap-2">
        {scanners.map((scanner) => (
          <button
            key={scanner.id}
            onClick={() => setSelectedScanner(scanner.id)}
            className={`px-4 py-2 rounded font-semibold transition ${
              selectedScanner === scanner.id
                ? 'bg-primary text-dark border-2 border-primary'
                : 'bg-dark-lighter border border-dark-lighter text-gray-300 hover:border-primary'
            }`}
          >
            {scanner.label}
          </button>
        ))}
      </div>
    </div>
  );
};

export default ScannerTabs;
