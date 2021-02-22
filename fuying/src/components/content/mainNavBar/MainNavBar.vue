<!--主页导航栏-->

<template>
  <nav-bar>
    <img slot="logo" src="~assets/img/logo.png" />
    <div slot="center">
      <nav-bar-item link="/home"
        ><div slot="text">{{ $t("nav.home") }}</div></nav-bar-item
      >
      <nav-bar-item link="/intro"
        ><div slot="text">{{ $t("nav.intro") }}</div></nav-bar-item
      >
      <nav-bar-item link="/news"
        ><div slot="text">{{ $t("nav.news") }}</div></nav-bar-item
      >
      <nav-bar-item link="/products"
        ><div slot="text">{{ $t("nav.product") }}</div></nav-bar-item
      >
      <div class="right">
        <el-dropdown placement="bottom" trigger="click" @command="batchOperate">
          <el-button class="search-btn" size="mini">
            language/语言
          </el-button>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="cn">中文</el-dropdown-item>
            <el-dropdown-item command="en">ENGLISH</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
    <nav-bar-item v-show="!isLogin" link="/login" slot="right" class="login"
      ><div slot="text">{{ $t("nav.login_register") }}</div></nav-bar-item
    >
    <div v-show="isLogin" slot="right">
      <nav-bar-item link="/profile" class="login"
        ><div slot="text">{{ $t("nav.profile") }}</div></nav-bar-item
      >
    </div>
  </nav-bar>
</template>

<script>
import NavBar from "common/navBar/NavBar";
import NavBarItem from "common/navBar/NavBarItem";

export default {
  name: "MainNavBar",
  components: {
    NavBar,
    NavBarItem
  },
  computed: {
    isLogin() {
      return this.$store.state.isLogin;
    }
  },
  methods: {
    batchOperate(command) {
      switch (command) {
        case "cn":
          console.log("cn");
          localStorage.setItem("lang", "cn");
          break;
        case "en":
          console.log("en");
          localStorage.setItem("lang", "en");
          break;
      }
      location.reload();
    }
  }
};
</script>

<style scoped>
.login {
  /* width: 120px; */
  padding: auto;
  margin: auto;
}

.right {
  margin-top: 3px;
  margin-left: 92%;
  width: 100px;
  /* background: gray; */
}
</style>
