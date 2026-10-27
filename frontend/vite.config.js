import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import { getProxyOptions } from 'frappe-ui/src/utils/vite-dev-server'
import { webserver_port } from '../../../sites/common_site_config.json'

// https://vitejs.dev/config/
export default defineConfig({
  base: process.env.NODE_ENV === 'production' ? '/assets/hrms_demo_app/frontend/' : '/',
  plugins: [vue()],
  server: {
    port: 8080,
    proxy: getProxyOptions({ port: webserver_port }),
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  build: {
    outDir: path.resolve(__dirname, '../hrms_demo_app/public/frontend'),
    emptyOutDir: true,
    target: 'es2015',
    cssCodeSplit: false,
    rollupOptions: {
      output: {
        format: 'iife',
        name: 'HRMSPortal',
        inlineDynamicImports: true,
        entryFileNames: 'index.js',
        assetFileNames: (assetInfo) =>
          assetInfo.name?.endsWith('.css') ? 'index.css' : 'assets/[name][extname]',
      },
    },
  },
  optimizeDeps: {
    include: ['frappe-ui > feather-icons', 'showdown', 'engine.io-client'],
  },
})
