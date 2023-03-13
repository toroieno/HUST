import Vue from 'vue';
import store from '@/store';
import router from '@/router';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import { vueI18n } from './plugins/i18n';

Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
  store,
  router,
  vuetify,
  // i18n: vueI18n,
  render: h => h(App)
}).$mount('#app')

