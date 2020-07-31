<template>
  <div id="app">
    <main-nav-bar></main-nav-bar>
    <router-view/>
    <side-bar></side-bar>
    <main-footer></main-footer>
  </div>
</template>

<script>
import MainNavBar from 'content/mainNavBar/MainNavBar'
import MainFooter from 'content/mainFooter/MainFooter'
import SideBar from 'common/sideBar/SideBar'

export default {
  name: 'App',
  components: {
    MainNavBar,
    MainFooter,
    SideBar,
  }
}
</script>

<style >
  @import "assets/css/base.css";
</style>
