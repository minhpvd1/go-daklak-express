import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: '.',
  publicDir: false,
  server: {
    host: '0.0.0.0',
    port: 3000
  },
  preview: {
    host: '0.0.0.0',
    port: 3000
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        driver: resolve(__dirname, 'driver.html'),
        s01: resolve(__dirname, '01_screen_home_discovery.html'),
        s02: resolve(__dirname, '02_screen_ride_hailing.html'),
        s03: resolve(__dirname, '03_screen_delivery.html'),
        s04: resolve(__dirname, '04_screen_food_discovery.html'),
        s05: resolve(__dirname, '05_screen_kfc_store.html'),
        s06: resolve(__dirname, '06_screen_kfc_food_detail.html'),
        s07: resolve(__dirname, '07_screen_driver_console.html'),
        s08: resolve(__dirname, '08_screen_cart_checkout.html'),
        s09: resolve(__dirname, '09_screen_live_tracking.html'),
        s10: resolve(__dirname, '10_screen_order_history.html'),
        s11: resolve(__dirname, '11_screen_voucher_promotions.html'),
        s12: resolve(__dirname, '12_screen_user_wallet_profile.html'),
        s13: resolve(__dirname, '13_screen_driver_trip_navigation.html'),
        s14: resolve(__dirname, '14_screen_driver_wallet_withdrawal.html'),
        s15: resolve(__dirname, '15_screen_driver_registration.html'),
        s16: resolve(__dirname, '16_screen_dispatch_admin_dashboard.html')
      }
    }
  }
});
