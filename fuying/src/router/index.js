// 路由

import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

// 设置懒加载
const Home = () => import('views/home/Home')
const Intro = () => import('views/intro/Intro')
const Login = () => import('views/login/Login')
const News = () => import('views/news/News')
const Products = () => import('views/products/Products')
const Report = () => import('views/products/Report')
const Pdf = () => import('views/products/Pdf')

// // 解决路由重复报错问题
// const originalPush = VueRouter.prototype.push
// VueRouter.prototype.push = function push(location) {
//   return originalPush.call(this, location).catch(err => err)
// }

// 1.安装VueRouter
Vue.use(VueRouter)

// 2.配置路由信息
const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    component: Home
  },
  {
    path: '/intro',
    component: Intro
  },  
  {
    path: '/login',
    component: Login,
    meta:{
      isLogin: false,
    },
  },
  {
    path: '/news',
    component: News
  },
  {
    path: '/products',
    component: Products
  },  
  {
    path: '/report',
    component: Report,
    meta:{
      isLogin: true,
    }
  },
  {
    path: '/pdf',
    component: Pdf,
    meta:{
      isLogin: true,
    }
  }
]

// 3.创建路由对象
const router = new VueRouter({
  mode: 'history',
  routes
})


router.beforeEach((to, from, next) => {
  let getPhone = localStorage.getItem("userPhone");
  if(getPhone !== null){
    store.state.isLogin = true;
    // console.log(store.state.isLogin);
    // 对登录状态无要求的页面
    if(to.meta.isLogin == null){
      next();
    }
    else{
      // 需要退出登录才能进入的页面
      if(!to.meta.isLogin){
        next({
          path: '/home',
        })
      }
      else{
        next();
      }
    }
  }
  // 未登录状态
  else{
    // 对登录状态无要求的页面
    if(to.meta.isLogin == null){
      next();
    }
    else{
      // 需要登录才能进入的页面
      if(to.meta.isLogin){
        next({
          path: '/login',
        })
      }
      else{
        next();
      }
    }
  }
})

// 4.导出
export default router