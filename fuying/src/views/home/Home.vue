<template>
  <div id="home">
    <home-menu></home-menu>
    <home-ad></home-ad>
  </div>
</template>

<script>
import HomeAd from 'content/home/HomeAd'
import HomeMenu from 'content/home/HomeMenu'

export default {
  name: "Home",
  components: {
    HomeAd,
    HomeMenu
  }
}
</script>

<style scoped>
  #home{
    min-height:500px;
  }
</style>