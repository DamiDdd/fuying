// 路由

import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";

// 解决当前路由重复跳转报错的细节问题
const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err);
};

// 设置懒加载
// const Home = () => import("views/home/Home");
// const Login2 = () => import("views/login/Login2");
const Intro = () => import("views/intro/Intro");
const Login = () => import("views/login/Login");
const News = () => import("views/news/News");
const Products = () => import("views/products/Products");
const Report = () => import("views/profile/Report");
const Pdf = () => import("views/profile/Pdf");
const Exit = () => import("views/exit/Exit");
const ReportEdit = () => import("views/manager/ReportEdit");
const Profile = () => import("views/profile/Profile");
const Detail = () => import("views/goods/Detail");
const Cart = () => import("views/cart/Cart");
const UploadCommend = () => import("views/manager/UploadCommend");
const ForgetPass = () => import("views/login/ForgetPass");
const Manager = () => import("views/manager/Manager");
const Payment = () => import("views/order/Payment");
const UploadGood = () => import("views/manager/UploadGood");
const Health = () => import("views/profile/Health");
const Homepage = () => import("views/homepage/Homepage");
const NewsDetail = () => import("views/news/NewsDetail");

// 1.安装VueRouter
Vue.use(VueRouter);

// 2.配置路由信息
// meta中包含的属性
// isLogin：对登录状态的要求
// isAdmin：对管理员权限的要求
const routes = [
  {
    path: "/",
    redirect: "/home",
    meta: {
      title: "首页"
    }
  },
  {
    path: "/home",
    component: Homepage,
    meta: {
      title: "首页"
    }
  },
  {
    path: "/intro",
    component: Intro,
    meta: {
      title: "介绍"
    }
  },
  {
    path: "/login",
    component: Login,
    meta: {
      isLogin: false,
      title: "登录/注册"
    }
  },
  {
    path: "/news",
    component: News,
    meta: {
      title: "新闻"
    }
  },
  {
    path: "/products",
    component: Products,
    meta: {
      title: "产品"
    }
  },
  {
    path: "/report",
    component: Report,
    meta: {
      isLogin: true,
      title: "报告"
    }
  },
  {
    path: "/pdf",
    component: Pdf,
    meta: {
      isLogin: true
    }
  },
  {
    path: "/exit",
    component: Exit,
    meta: {
      isLogin: true
    }
  },
  {
    path: "/reportEdit",
    component: ReportEdit,
    meta: {
      isLogin: true,
      isAdmin: true,
      title: "编辑报告"
    }
  },
  {
    path: "/uploadCommend",
    component: UploadCommend,
    meta: {
      isLogin: true,
      isAdmin: true
    }
  },
  {
    path: "/profile",
    component: Profile,
    meta: {
      isLogin: true,
      title: "个人中心"
    }
  },
  {
    path: "/detail",
    component: Detail,
    meta: {
      title: "商品详情"
    }
  },
  {
    path: "/cart",
    component: Cart,
    meta: {
      isLogin: true,
      title: "我的购物车"
    }
  },
  {
    path: "/forgetPass",
    component: ForgetPass,
    meta: {
      isLogin: false,
      title: "忘记密码"
    }
  },
  {
    path: "/manager",
    component: Manager,
    meta: {
      isLogin: true,
      isAdmin: true,
      title: "管理"
    }
  },
  {
    path: "/payment",
    component: Payment,
    meta: {
      isLogin: true,
      title: "付款页面"
    }
  },
  {
    path: "/uploadGood",
    component: UploadGood,
    meta: {
      isLogin: true,
      isAdmin: true,
      title: "上传商品"
    }
  },
  {
    path: "/health",
    component: Health,
    meta: {
      isLogin: true,
      title: "个人健康"
    }
  },
  {
    path: "/newsDetail",
    component: NewsDetail,
    title: "新闻详情页"
  }
  // {
  //   path: "/homepage",
  //   component: Home
  // },
  // {
  //   path: "/login2",
  //   component: Login2,
  //   meta: {
  //     isLogin: false
  //   }
  // }
];

// 3.创建路由对象
const router = new VueRouter({
  // mode: 'history', //注释后默认为hash模式
  base: "health/",
  routes
});

// 设置各种进入权限判断
router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title;
  }

  let getPhone = localStorage.getItem("userPhone");
  if (getPhone !== null) {
    store.state.isLogin = true;
    // 对登录状态无要求的页面
    if (to.meta.isLogin == null) {
      next();
    } else {
      // 需要退出登录才能进入的页面
      if (!to.meta.isLogin) {
        Vue.prototype.$message({
          type: "warning",
          message: "请先退出登录"
        });
        next({
          path: "/home"
        });
      }
      // 需要管理员权限的页面
      else if (to.meta.isAdmin) {
        let getAdmin = localStorage.getItem("admin");
        // 有管理员权限
        if (getAdmin !== null) {
          store.state.isAdmin = true;
          Vue.prototype.$message({
            type: "success",
            message: "欢迎 admin：" + getAdmin
          });
          next();
        }
        // 无管理员权限
        else {
          Vue.prototype.$message({
            type: "warning",
            message: "无权限"
          });
          next({
            path: from.fullPath
          });
        }
      } else {
        next();
      }
    }
  }
  // 未登录状态
  else {
    store.state.isLogin = false;
    // 对登录状态无要求的页面
    if (to.meta.isLogin == null) {
      next();
    } else {
      // 需要登录才能进入的页面
      if (to.meta.isLogin) {
        Vue.prototype.$message({
          type: "warning",
          message: "请先登录"
        });
        next({
          path: "/login"
        });
      } else {
        next();
      }
    }
  }
});

router.afterEach(() => {
  window.scrollTo(0, 0);
});

// 4.导出
export default router;
