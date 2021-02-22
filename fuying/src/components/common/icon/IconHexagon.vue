<!--矩形icon-->

<template>
  <div id="icon-hexagon">
    <div class="hexagon">
      <slot name="img"></slot>
      <slot name="text"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "IconHexagon"
};
</script>

<style scoped>
#icon-hexagon {
  width: 200px;
  height: 200px;
  /* background: gray; */
  background: url("~assets/img/common/hexagon-shadow.png") no-repeat;
}

.hexagon {
  width: 130px;
  height: 130px;
  background: url("~assets/img/common/hexagon.png") no-repeat;
}
</style>
