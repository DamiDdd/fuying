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
    position: relative;
    z-index: 10;
    display: flex;
    height: 44px;
    width: var(--screen-width);
    line-height: 44px;
    text-align: center;
  }
  
  .nav-logo{
    width: 60px;
  }

  .nav-logo img{
    width: 24px;
    height: 24px;
    margin-top: 5px;
    vertical-align: middle;
  }

  .nav-center{
    flex: 1;
  }

  .nav-right{
    width: 120px;
    text-align: left;
  }
</style>