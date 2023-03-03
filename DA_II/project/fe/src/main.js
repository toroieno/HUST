import Vue from 'vue';
import store from '@/store';
import router from '@/router';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
