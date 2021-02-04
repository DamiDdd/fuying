import Vue from 'vue'
import App from './App.vue'
import router from './router'
import echarts from "echarts"
import store from './store'
import ElementUI from 'element-ui'
import i18n from './assets/i18n/i18n'
import 'element-ui/lib/theme-chalk/index.css';

Vue.config.productionTip = false;
Vue.prototype.$echarts = echarts;
Vue.use(ElementUI);

new Vue({
  render: h => h(App),
  i18n,
  router,
  store,
  echarts,
}).$mount('#app')
