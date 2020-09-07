<template>
  <div id="item-window">
    <div class="i-div">
      <div class="title"><slot name="title"></slot></div>
      <div class="img"><slot name="img"></slot></div>
      <div class="desc"><slot name="desc"></slot></div>
    </div>
  </div>
</template>

<script>

export default {
  name: "ItemWindow",
  components:{
  },
  methods:{
  }
}
</script>

<style scoped>
  .i-div{
    width: 400px;
    height: 350px;
    /* overflow: hidden; */
    margin-left: 100px;
    margin-top: 20px;
    background: url("~assets/img/bg/item-bg.jpg") repeat top right;
    float: left;
  }
  .img img{
    width: 400px;
    height: 270px;
  }
  .desc{
    background: gray;
    /* 预备设置遮罩层 */
    /* margin-top: -300px; */
  }
  
</style>