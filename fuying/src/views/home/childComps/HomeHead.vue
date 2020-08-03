<!--首页第一个页面-->

<template>
  <div id="home-head">
    <div class="left-text">
      <p class="bigtext">感觉身上不适，</p>
      <p class="bigtext">但是医院各项检查指标均正常？</p>
      <p class="bigtext bottom">您的身体可能处于<span>亚健康状态！</span></p>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeHead",
}
</script>

<style scoped>
  #home-head{
    width: var(--screen-width);
    height: var(--screen-height);
    background: url("~assets/img/bg/index1-bg.png") no-repeat top right;
  }

  .left-text{
    width: 600px;
    height: 400px;
    position: relative;
    margin-left: 300px;
    padding-top: 260px;
  }

  .left-text .bigtext{
    color: black;
  }

  .bottom{
    padding-top: 100px;
  }

  .bottom span{
    color: var(--theme-color);
  }
</style>