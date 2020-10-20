<!--顶部导航栏-->

<template>
  <div id="nav-bar">
    <div class="nav-logo"><slot name="logo">logo</slot></div>
    <div class="nav-center"><slot name="center">choices</slot></div>
    <div class="nav-right"><slot name="right">user</slot></div>
  </div>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style scoped>
  #nav-bar {
    height: 50px;
    overflow: auto;
    position: relative;
    z-index: 10;
    display: flex;
    width: var(--screen-width);
    min-width: var(--min-width);
    line-height: 44px;
    text-align: center;
  }
  
  .nav-logo{
    width: 3%;
  }

  .nav-logo img{
    width: 24px;
    height: 24px;
    margin-top: 5px;
    vertical-align: middle;
  }

  .nav-center{
    flex: 1;
    margin-left: 2%;
    /* margin-left: 70%; */
  }

  .nav-right{
    width: 120px;
    text-align: left;
  }
</style>