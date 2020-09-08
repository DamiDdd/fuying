<template>
  <div id="cart-icon" :style="iconStyle" @click="jump2cart">
    <img v-show="isLogin()" src="~assets/img/common/purchase-active.png">
    <img v-show="!isLogin()" src="~assets/img/common/purchase.png">
  </div>
</template>

<script>
export default {
  name: "CartIcon",
  props:{
    iconStyle:{
      type: Object,
    }
  },
  methods:{
    isLogin(){
      return this.$store.state.isLogin;
    },
    jump2cart(){
      this.$router.push("/cart");
    }
  }
}
</script>

<style scoped>
  #cart-icon{
    width: 50px;
    height: 50px;
    position: fixed;
    cursor: pointer;
    text-align: center;
    box-shadow: 0 0 6px rgba(0,0,0,.12);
    z-index: 99;
  }
  img{
    width: 40px;
  }
</style>