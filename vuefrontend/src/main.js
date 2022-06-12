import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import { StripePlugin } from '@vue-stripe/vue-stripe';

const options = {
  pk: process.env.STRIPE_PUBLISHABLE_KEY,
  stripeAccount: process.env.STRIPE_ACCOUNT,
  apiVersion: process.env.API_VERSION,
  locale: process.env.LOCALE,
};

createApp(App).use(router,StripePlugin, options).mount('#app')

