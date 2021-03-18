<!--主页导航栏-->

<template>
  <nav-bar>
    <img slot="logo" src="~assets/img/logo.png" />
    <div slot="center">
      <nav-bar-item link="/home"
        ><div class="focus" slot="text">{{ $t("nav.home") }}</div></nav-bar-item
      >
      <nav-bar-item link="/intro"
        ><div class="focus" slot="text">
          {{ $t("nav.intro") }}
        </div></nav-bar-item
      >
      <nav-bar-item link="/news"
        ><div class="focus" slot="text">{{ $t("nav.news") }}</div></nav-bar-item
      >
      <nav-bar-item link="/products"
        ><div class="focus" slot="text">
          {{ $t("nav.product") }}
        </div></nav-bar-item
      >

      <nav-bar-item v-show="isAdmin" link="/admin" style="width: 8rem;"
        ><div class="focus" slot="text">
          {{ $t("nav.admin") }}
        </div></nav-bar-item
      >
      <div class="right">
        <el-dropdown placement="bottom" trigger="hover" @command="batchOperate">
          <span
            class="el-dropdown-link focus btn"
            style="font-size: 1.05rem;"
          >
            语言
          </span>
          <el-dropdown-menu slot="dropdown" class="dropdown">
            <el-dropdown-item class="item" command="cn">中文</el-dropdown-item>
            <el-dropdown-item class="item" command="en"
              >ENGLISH</el-dropdown-item
            >
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
    <nav-bar-item v-show="isLogin" link="/cart" class="cart" slot="right"
      ><div class="focus" slot="text">
        <!-- <img class="icon" src="~assets/img/common/cart.png" alt="" /> -->
        {{ $t("nav.cart") }}
      </div></nav-bar-item
    >
    <nav-bar-item v-show="!isLogin" link="/login" slot="right" class="login"
      ><div class="focus" slot="text">
        {{ $t("nav.login_register") }}
      </div></nav-bar-item
    >
    <div v-show="isLogin" slot="right">
      <nav-bar-item link="/profile" class="login"
        ><div class="focus" slot="text">
          {{ $t("nav.profile") }}
        </div>
      </nav-bar-item>
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
    },
    isAdmin() {
      // return this.$store.state.isAdmin;
      if (localStorage.getItem("admin") != null) {
        return true;
      } else {
        return false;
      }
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
  /* width: 7.5rem; /* 120/16 */
  padding: auto;
  margin: auto;
}

.right {
  position: absolute;
  margin-top: 0.1875rem;
  right: 6.25rem /* 100/16 */;
  width: 15.5rem /* 200/16 */;
  font-size: 1.6875rem /* 27/16 */;
}

.el-dropdown-link {
  cursor: pointer;
  color: white;
  padding-bottom: 0rem /* 0/16 */;
  margin-bottom: 0rem /* 0/16 */;
}

.dropdown {
  /* background: #333333; */
  padding-top: 0rem /* 0/16 */;
  /* opacity: 50%; */
}

.focus:hover {
  color: wheat;
}
.icon {
  width: 1.5rem;
  margin-top: 0.4rem;
}

.cart {
}
</style>
