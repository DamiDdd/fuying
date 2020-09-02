<template>
  <div id="item-window">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "ItemWindow",
}
</script>

<style scoped>
  #item-window{
    width: 600px;
    height: 300px;
    padding-left: 100px;
    padding-top: 20px;
    background: url("~assets/img/bg/item-bg.jpg") no-repeat top right;
  }
</style>