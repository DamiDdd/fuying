<template>
  <div id="foot-bar">
    <div class="footer-tip"><slot name="tip">tip</slot></div>
    <div class="footer-icon"><slot name="icon">icon</slot></div>
    <div class="footer-author"><slot name="author">author</slot></div>
  </div>
</template>

<script>
export default {
  name: "FootBar"
}
</script>

<style scoped>
  #foot-bar{
    height:500px;
    width: 100%;
    background: url('~assets/img/common/footer.png');
    text-align: center;
  }
  .footer-tip{
    height: 100px;
    /* background: red; */
  }
  .footer-author{
    height: 100px;
    /* background: darkblue; */
  }
  .footer-icon{
    height: 300px;
    /* background: green; */
  }
</style>