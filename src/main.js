import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import { VueCookies } from 'vue-cookies';
//import ipify from 'ipify';
$cookies.config('1m')
createApp(App).use(router,VueCookies).mount('#app')

