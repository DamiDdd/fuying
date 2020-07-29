<template>
  <div id="home">
    <home-ad></home-ad>
  </div>
</template>

<script>
  import HomeAd from 'content/home/HomeAd'


  export default {
    name: "Home",
    components: {
      HomeAd
    }
  }
</script>

<style scoped>
  #home{
    min-height:500px;
  }
</style>