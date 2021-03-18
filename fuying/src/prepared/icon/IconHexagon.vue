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
  width: 12.5rem /* 200/16 */;
  height: 12.5rem /* 200/16 */;
  /* background: gray; */
  background: url("~assets/img/common/hexagon-shadow.png") no-repeat;
}

.hexagon {
  width: 8.125rem /* 130/16 */;
  height: 8.125rem /* 130/16 */;
  background: url("~assets/img/common/hexagon.png") no-repeat;
}
</style>
