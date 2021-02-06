<!--侧边栏-->

<template>
  <div id="side-bar" class="smalltext">{{$t('public.sidebar')}}</div>
</template>

<script>
export default {
  name: "SideBar"
}
</script>

<style scoped>
  #side-bar{
    /* background: white; */
    width:20px;
    height:200px;
    position: fixed;
    left:10px;
    top: 370px;
  }
</style>