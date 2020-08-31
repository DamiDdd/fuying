<!--主页导航栏-->

<template>
  <nav-bar>
    <img slot="logo" src="~assets/img/common/logo.png">
    <div slot="center">
      <nav-bar-item link="/home"><div slot="text">首页</div></nav-bar-item>
      <nav-bar-item link="/intro"><div slot="text">介绍</div></nav-bar-item>
      <nav-bar-item link="/news"><div slot="text">新闻</div></nav-bar-item>
      <nav-bar-item link="/products"><div slot="text">产品</div></nav-bar-item>
    </div>
    <nav-bar-item v-show="!isLogin()" link="/login" slot="right" class="login"><div slot="text">登录/注册</div></nav-bar-item>
    <div v-show="isLogin()" slot="right">
      <nav-bar-item link="/profile" class="login"><div slot="text">个人中心</div></nav-bar-item>
    </div>
  </nav-bar>
</template>

<script>
import NavBar from 'common/navBar/NavBar'
import NavBarItem from 'common/navBar/NavBarItem'

export default {
  name: "MainNavBar",
  components:{
    NavBar,
    NavBarItem
  },
  methods:{
    isLogin(){
      return this.$store.state.isLogin;
    },
  }
}
</script>

<style scoped>
.login{
  width: 120px;
  padding: auto;
  margin: auto;
}
</style>