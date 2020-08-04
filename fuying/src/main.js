import Vue from 'vue'
import App from './App.vue'
import router from './router'
import echarts from "echarts"
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';

Vue.config.productionTip = false;
Vue.prototype.$echarts = echarts;
Vue.use(ElementUI);
// Vue.arguments(ElementUI)

new Vue({
  render: h => h(App),
  router,
  echarts,
}).$mount('#app')
