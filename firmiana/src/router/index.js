// 路由

import Vue from "vue";
import VueRouter from "vue-router";

// 设置懒加载
const Register = () => import("../components/Register");

// 1.安装VueRouter
Vue.use(VueRouter);

// 2.配置路由信息
// meta中包含的属性
// isLogin：对登录状态的要求
// isAdmin：对管理员权限的要求
const routes = [
  {
    path: "/",
    redirect: "/register",
  },
  {
    path: "/register",
    component: Register,
    // meta:{
    //   isLogin: false,
    // },
  },
];

// 3.创建路由对象
const router = new VueRouter({
  mode: "history",
  routes,
});

// 4.导出
export default router;
