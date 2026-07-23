import React, { useState } from 'react';

const Sidebar: React.FC = () => {
  const [expanded, setExpanded] = useState(false);

  const menuItems = [
    { icon: '🏠', label: 'Anasayfa', href: '/' },
    { icon: '📊', label: 'Taramalar', href: '/scans' },
    { icon: '📈', label: 'Grafik Analiz', href: '/charts' },
    { icon: '⭐', label: 'Favoriler', href: '/favorites' },
    { icon: '🔔', label: 'Uyarılar', href: '/alerts' },
    { icon: '⚙️', label: 'Ayarlar', href: '/settings' },
  ];

  return (
    <div className={`bg-dark-light border-r border-dark-lighter transition-all ${
      expanded ? 'w-64' : 'w-20'
    }`}>
      <div className="p-4 flex justify-between items-center">
        {expanded && <span className="text-primary font-bold">📊 MENU</span>}
        <button
          onClick={() => setExpanded(!expanded)}
          className="text-primary hover:bg-dark-lighter p-2 rounded"
        >
          {expanded ? '←' : '→'}
        </button>
      </div>
      <nav className="mt-4">
        {menuItems.map((item, i) => (
          <a
            key={i}
            href={item.href}
            className="flex items-center space-x-3 px-4 py-3 hover:bg-dark-lighter text-gray-300 hover:text-primary transition"
          >
            <span className="text-xl">{item.icon}</span>
            {expanded && <span>{item.label}</span>}
          </a>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;
