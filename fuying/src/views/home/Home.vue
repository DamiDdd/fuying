<template>
  <div id="home">
    <home-head></home-head>
    <home-menu></home-menu>
    <home-ad></home-ad>
  </div>
</template>

<script>
import HomeAd from 'content/home/HomeAd'
import HomeMenu from 'content/home/HomeMenu'
import HomeHead from 'content/home/HomeHead'

export default {
  name: "Home",
  components: {
    HomeAd,
    HomeMenu,
    HomeHead
  }
}
</script>

<style scoped>
  #home{
    min-height:500px;
  }
</style>