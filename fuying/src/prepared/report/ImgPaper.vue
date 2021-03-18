<!--前端生成报告所用的组件，备用-->

<template>
  <div id="img-paper">
    <div class="window">
      <div class="title-div">
        <slot name="title1"></slot>
      </div>
      <div class="img-div">
        <slot name="img1"></slot>
      </div>
      <div class="text-div">
        <slot name="text1"></slot>
      </div>
    </div>
    <div class="window">
      <div class="title-div">
        <slot name="title2"></slot>
      </div>
      <div class="img-div">
        <slot name="img2"></slot>
      </div>
      <div class="text-div">
        <slot name="text2"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImgPaper"
};
</script>

<style scoped>
#img-paper {
  height: var(--paper-height);
  width: var(--paper-width);
  margin-left: auto;
  margin-right: auto;
  border: .0625rem /* 1/16 */ solid var(--theme-color);
  margin-bottom: .6625rem /* 10.6/16 */;
}

.window {
  height: calc(var(--paper-height-half) - .625rem /* 10/16 */);
  width: calc(var(--paper-width) - .625rem /* 10/16 */);
  border: .03125rem /* 0.5/16 */ solid #000;
  margin-top: .3125rem /* 5/16 */;
  margin-left: auto;
  margin-right: auto;
}

.title-div {
  height: 1.6875rem /* 27/16 */;
  width: calc(var(--paper-width) - .625rem /* 10/16 */);
  border-width: 0 0 .03125rem /* 0.5/16 */ 0;
  border-style: solid;
  border-color: gray;
}

.title-div p {
  margin-top: .625rem /* 10/16 */;
  text-align: center;
  color: var(--theme-color);
  font-size: 1rem /* 16/16 */;
}

.img-div {
  height: 18.75rem /* 300/16 */;
  width: calc(var(--paper-width) - .625rem /* 10/16 */);
}

.img-div img {
  height: 17.5rem /* 280/16 */;
  margin-left: 7.5rem /* 120/16 */;
}

.text-div {
  height: 3.75rem /* 60/16 */;
  overflow: hidden;
  width: calc(var(--paper-width) - .625rem /* 10/16 */);
}

.text-div p {
  margin-top: .625rem /* 10/16 */;
  font-size: .875rem /* 14/16 */;
  text-indent: 2rem;
  margin-left: .625rem /* 10/16 */;
}
</style>
