<template>
  <div id="detail">
    <div class="num-control">
      <div class="left"><slider :imgWidth=600></slider></div>
      <div class="right"><good-view :item="good"></good-view></div>
    </div>
  </div>
</template>

<script>
import GoodView from "components/content/detail/GoodView"
import Slider from "components/common/slide/Slider";

export default {
  name: "Detail",
  components:{
    GoodView,
    Slider,
  },
  data(){
    return{
      // 传参
      good:{
        title: "title",
        count: 1,
        desc: "desc, i think i should add some words here to fill this div. desc, i think i should add some words here to fill this div",
        type:[
          {
            id: "1",
            name:"基础生理刻画套餐",
            tip:"包括基础",
            price: 100,
          },{
            id: "2",
            name:"升级",
            tip:"包括升级版",  
            price: 200,
          },
          // {
          //   id: "2",
          //   name:"升级生理刻画套餐",
          //   tip:"包括升级版",  
          //   price: 200,
          // },{
          //   id: "2",
          //   name:"升级生理刻画套餐",
          //   tip:"包括升级版",  
          //   price: 200,
          // }
        ],
      }
    }
  },
  mounted(){
    //  在这里申请拿到商品数据
    this.good['count'] = 1;
  }
}
</script>

<style scoped>
  #detail{
    min-height: 500px;
  }
  .num-control{
    margin-left:200px;
    margin-top: 100px;
  }
  .left{
    float: left;
    /* background: blue; */
    width: 800px;
    min-height: 450px;
  }
  .right{
    float: left;
    position: absolute;
    margin-left: 800px;
    width: 800px;
    min-height: 450px;
    background: url("~assets/img/bg/item-bg.jpg") top right;
    background-size: 100% 100%;
  }
  .cartcontrol{
    margin-left: 100px; 
  }
</style>