<!--页脚组件-->

<template>
  <div id="foot-bar">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "FootBar"
}
</script>

<style scoped>
  #foot-bar{
    height: 480px;
    /* width: 1920px; */
    width: var(--screen-width);
    background: url('~assets/img/common/footer.png');
    text-align: center;
    color: white;
    overflow: hidden;
  }
</style>