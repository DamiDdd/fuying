<template>
  <div id="app" @click="clicked">
    <main-nav-bar></main-nav-bar>
    <router-view/>
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
  data() {
    return {
      ltime: new Date().getTime(),  // 最后一次点击时间
      ctime: new Date().getTime(),  // current time
      tOut: 10 * 60 * 1000, // ms,无操作退出时间，十分钟
      myBackToTopStyle: {
        'right': '100px',
        'bottom': '150px',
        'width': '40px',
        'height': '40px',
        'border-radius': '20px',
        'line-height': '40px', 
        'background': '#fff'
      }
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
    clicked(){
      this.ltime = new Date().getTime()
    },
    tTime(){
      this.ctime = new Date().getTime()
      if(this.ctime - this.ltime > this.tOut){
        if(localStorage.getItem("userPhone") !== null){
          localStorage.removeItem("userPhone");
          this.$store.state.isLogin = false;
          console.log(localStorage);
          this.$router.push('/home');
          this.$message({
            type: 'success',
            message: '长时间未操作，已为您退出登录'
          });
        }
      }
    }
  }
}
</script>

<style >
  @import "assets/css/base.css";
</style>
