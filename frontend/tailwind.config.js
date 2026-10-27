module.exports = {
  presets: [
    require('frappe-ui/src/utils/tailwind.config')
  ],
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        hrms: {
          purple: '#453D89',
          deep: '#301044',
          pink: '#C8499A',
          bg: '#f7f4f8',
          muted: '#75657D',
          border: '#E7DDF0',
          ink: '#292132',
        },
      },
      fontSize: {
        'body-sm': ['0.875rem', { lineHeight: '1.5' }],
        'body-md': ['1rem', { lineHeight: '1.5' }],
        'body-lg': ['1.125rem', { lineHeight: '1.6' }],
        'body-xl': ['1.25rem', { lineHeight: '1.6' }],
        'display-sm': ['1.875rem', { lineHeight: '1.2' }],
        'display-md': ['2.25rem', { lineHeight: '1.15' }],
        'display-lg': ['3rem', { lineHeight: '1.1' }],
        'display-xl': ['3.75rem', { lineHeight: '1.05' }],
      },
      backgroundImage: {
        'brand-gradient': 'linear-gradient(135deg, #453D89 0%, #7b2d87 52%, #c33d91 100%)',
        'brand-gradient-soft': 'linear-gradient(135deg, rgba(69, 61, 137, 0.08), rgba(200, 73, 154, 0.12))',
      },
      boxShadow: {
        card: '0 4px 16px rgba(48, 16, 68, 0.06)',
        'card-hover': '0 12px 28px rgba(48, 16, 68, 0.12)',
        panel: '0 20px 60px rgba(48, 16, 68, 0.14)',
        cta: '0 8px 24px rgba(69, 61, 137, 0.22)',
      },
    },
  },
  plugins: [],
}
