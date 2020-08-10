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
}
</script>

<style scoped>
  #img-paper{
    height: var(--paper-height);
    width: var(--paper-width);
    margin-left: auto;
    margin-right: auto;
    /* background: gray; */
    border: 1px solid var(--theme-color);
    margin-bottom: 11px;
  }

  .window{
    height: calc(var(--paper-height-half) - 10px);
    width: calc(var(--paper-width) - 10px);
    border: 0.5px solid #000;
    margin-top: 5px;
    margin-left: auto;
    margin-right: auto;
  }

  .title-div{
    height: 27px;
    width: calc(var(--paper-width) - 10px);
    /* background: #000; */
    border-width: 0 0 0.5px 0;
    border-style: solid;
    border-color: gray;
  }

  .title-div p{
    margin-top: 10px;
    text-align: center;
    color: var(--theme-color);
    font-size: 16px;
  }

  .img-div{
    height: 300px;
    width: calc(var(--paper-width) - 10px);
    /* background: gray; */
  }

  .img-div img{
    height: 280px;
    margin-left: 120px;
  }

  .text-div{
    height: 60px;
    overflow: hidden;
    width: calc(var(--paper-width) - 10px);
    /* background: gray; */
  }

  .text-div p{
    margin-top: 10px;
    font-size: 14px;
    text-indent: 2rem;
    margin-left: 10px;
  }
</style>