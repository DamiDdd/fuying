<template>
  <div id="home">
    <home-head></home-head>
    <home-product></home-product>
    <home-menu></home-menu>
    <home-ad></home-ad>
  </div>
</template>

<script>
import HomeAd from 'views/home/childComps/HomeAd'
import HomeMenu from 'views/home/childComps/HomeMenu'
import HomeHead from 'views/home/childComps/HomeHead'
import HomeProduct from 'views/home/childComps/HomeProduct'

export default {
  name: "Home",
  components: {
    HomeAd,
    HomeMenu,
    HomeHead,
    HomeProduct,
  },
  mounted(){
    console.log(localStorage);
    console.log(this.$store.state.isLogin);
  }
}
</script>

<style scoped>
  #home{
    min-height:500px;
  }
</style>