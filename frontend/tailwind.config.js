/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        dark: '#0f1419',
        'dark-light': '#1a1f2e',
        'dark-lighter': '#242a3a',
        primary: '#00ff88',
        danger: '#ff3333',
        warning: '#ffaa00',
        info: '#00aaff',
      },
    },
  },
  plugins: [],
};
