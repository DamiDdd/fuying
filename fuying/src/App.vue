<template>
  <div id="app">
    <main-nav-bar></main-nav-bar>
    <router-view/>
    <main-footer></main-footer>
  </div>
</template>

<script>
  import MainNavBar from 'content/mainNavBar/MainNavBar'
  import MainFooter from 'content/mainFooter/MainFooter'

  export default {
    name: 'App',
    components: {
      MainNavBar,
      MainFooter
    }
  }
</script>

<style >
  @import "assets/css/base.css";
</style>
