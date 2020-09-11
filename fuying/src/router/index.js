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
const Report = () => import('views/profile/Report')
const Pdf = () => import('views/profile/Pdf')
const Exit = () => import('views/exit/Exit')
const ReportEdit = () => import('views/manager/ReportEdit')
const Profile = () => import('views/profile/Profile')
const Detail = () => import('views/goods/Detail')
const Cart = () => import('views/cart/Cart')
const UploadCommend = () => import('views/manager/UploadCommend')

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
  },
  {
    path: '/exit',
    component: Exit,
    meta:{
      isLogin : true,
    }
  },
  {
    path: '/reportEdit',
    component: ReportEdit,
    meta:{
      isLogin : true,
      isAdmin : true,
    }
  },
  {
    path: '/uploadCommend',
    component: UploadCommend,
    meta:{
      isLogin : true,
      isAdmin : true,
    }
  },
  {
    path: '/profile',
    component: Profile,
    meta:{
      isLogin : true,
    }
  },
  {
    path: '/detail',
    component: Detail,
  },
  {
    path: '/cart',
    component: Cart,
    meta:{
      isLogin: true,
    }
  },
]

// 3.创建路由对象
const router = new VueRouter({
  mode: 'history',
  routes
})

// 设置各种进入权限判断
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
        Vue.prototype.$message({
          type: 'warning',
          message: '请先退出登录',
        });
        next({
          path: '/home',
        })
      }
      // 需要管理员权限的页面
      else if(to.meta.isAdmin){
        let getAdmin = localStorage.getItem("admin");
        // 有管理员权限
        if(getAdmin !== null){
          store.state.isAdmin = true;
          Vue.prototype.$message({
            type: 'success',
            message: '欢迎 admin：'+getAdmin,
          });
          next();
        }
        // 无管理员权限
        else{
          Vue.prototype.$message({
            type: 'warning',
            message: '无权限',
          });
          next({
            path: from.fullPath,
          });
        }
      }
      else{
        next();
      }
    }
  }
  // 未登录状态
  else{
    store.state.isLogin = false;
    // 对登录状态无要求的页面
    if(to.meta.isLogin == null){
      next();
    }
    else{
      // 需要登录才能进入的页面
      if(to.meta.isLogin){
        Vue.prototype.$message({
          type: 'warning',
          message: '请先登录',
        });
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