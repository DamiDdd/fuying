<!--购物车icon组件-->

<template>
  <div id="cart-icon" :style="iconStyle" @click="jump2cart">
    <img v-show="isLogin()" src="~assets/img/common/purchase-active.png" />
    <img v-show="!isLogin()" src="~assets/img/common/purchase.png" />
  </div>
</template>

<script>
export default {
  name: "CartIcon",
  props: {
    // icon自定样式
    iconStyle: {
      type: Object
    }
  },
  methods: {
    // 获取本地登录状态
    isLogin() {
      return this.$store.state.isLogin;
    },
    // 跳转至cart
    jump2cart() {
      this.$router.push("/cart");
    }
  }
};
</script>

<style scoped>
#cart-icon {
  width: 3.125rem /* 50/16 */;
  height: 3.125rem /* 50/16 */;
  position: fixed;
  cursor: pointer;
  text-align: center;
  box-shadow: 0 0 .375rem /* 6/16 */ rgba(0, 0, 0, 0.12);
  z-index: 99;
}
img {
  width: 2.5rem /* 40/16 */;
}
</style>
