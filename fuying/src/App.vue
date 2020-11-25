<template>
  <div id="app" @click="clicked">
    <main-nav-bar></main-nav-bar>
    <router-view v-if="isRouterAlive"/>
    <side-bar></side-bar>
    <main-footer></main-footer>
    <back-to-top        
      transitionName="fade"
      :customStyle="myBackToTopStyle" 
      :visibilityHeight="300" 
      :backPosition="50">
    </back-to-top>    
  </div>
</template>

<script>
import MainNavBar from 'content/mainNavBar/MainNavBar'
import MainFooter from 'content/mainFooter/MainFooter'
import SideBar from 'common/sideBar/SideBar'
import BackToTop from 'common/backToTop/BackToTop'

export default {
  name: 'App',
  provide(){
    return{
      reload: this.reload,
    }
  },
  data() {
    return {
      ltime: new Date().getTime(),  // 最后一次点击时间
      ctime: new Date().getTime(),  // current time
      tOut: 10 * 60 * 1000, // ms,无操作退出时间，十分钟
      myBackToTopStyle: { // 返回顶部的函数
        'right': '100px',
        'bottom': '150px',
        'width': '40px',
        'height': '40px',
        'border-radius': '20px',
        'line-height': '40px', 
        'background': '#fff'
      },
      isRouterAlive: true, // 控制路由页面显示信息
    }
  },
  components: {
    MainNavBar,
    MainFooter,
    SideBar,
    BackToTop,
  },
  mounted(){
    window.setInterval(this.tTime,1000)
  },
  methods:{
    // 监听鼠标点击事件
    clicked(){
      this.ltime = new Date().getTime()
    },
    // 自动退出函数
    tTime(){
      this.ctime = new Date().getTime()
      if(this.ctime - this.ltime > this.tOut){
        // 重置上次点击时间
        this.ltime = this.ctime;
        if(localStorage.getItem("userPhone") !== null){
          localStorage.removeItem("userPhone");
          localStorage.removeItem("userEmail");
          localStorage.removeItem("userName");
          this.$store.state.isLogin = false;
          if(localStorage.getItem("admin")!=null){
            localStorage.removeItem("admin");
            this.$store.state.isAdmin = false;
          }
          this.$router.push('/home');
          this.$message({
            type: 'success',
            message: '长时间未操作，已为您退出登录'
          });
        }
      }
    },
    // 刷新页面函数，通过inject注入引用
    reload(){
      this.isRouterAlive = false;
      this.$nextTick(function(){
        this.isRouterAlive = true;
      })
    }
  }
}
</script>

<style >
  @import "assets/css/base.css";
</style>
