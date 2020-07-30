<template>
  <div id="home">
    <home-head></home-head>
    <home-product></home-product>
    <home-menu></home-menu>
    <home-ad></home-ad>
  </div>
</template>

<script>
import HomeAd from 'content/home/HomeAd'
import HomeMenu from 'content/home/HomeMenu'
import HomeHead from 'content/home/HomeHead'
import HomeProduct from 'content/home/HomeProduct'

export default {
  name: "Home",
  components: {
    HomeAd,
    HomeMenu,
    HomeHead,
    HomeProduct,
  }
}
</script>

<style scoped>
  #home{
    min-height:500px;
  }
</style>