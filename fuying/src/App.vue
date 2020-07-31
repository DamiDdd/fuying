<template>
  <div id="app">
    <main-nav-bar></main-nav-bar>
    <router-view/>
    <side-bar></side-bar>
    <main-footer></main-footer>
    <el-tooltip placement="top" content="返回顶部">
      <back-to-top        
        transitionName="fade"
        :customStyle="myBackToTopStyle" 
        :visibilityHeight="300" 
        :backPosition="50"></back-to-top>
    </el-tooltip>
    
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
  }
}
</script>

<style >
  @import "assets/css/base.css";
</style>
