// 路由

import Vue from 'vue'
import VueRouter from 'vue-router'

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
    component: Login
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
    component: Report
  },
  {
    path: '/pdf',
    component: Pdf
  }
]

// 3.创建路由对象
const router = new VueRouter({
  mode: 'history',
  routes
})

// 4.导出
export default router