import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import { VueCookies } from 'vue-cookies';
//import ipify from 'ipify';

createApp(App).use(router,VueCookies).mount('#app')
