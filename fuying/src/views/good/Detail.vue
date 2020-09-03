<template>
  <div id="detail">
    <div class="num-control">
      <slider></slider>
      <good-view :item="good"></good-view>
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
        count: 0,
        desc: "desc",
        type:[
          {
            name:"基础生理刻画套餐",
            tip:"包括基础",
            price:"100",
          },{
            name:"升级生理刻画套餐",
            tip:"包括升级版",  
            price:"200",
          }
        ],
      }
    }
  },
  mounted(){
    //  在这里申请拿到商品数据
    this.good['count'] = 0;
  }
}
</script>

<style scoped>
  #detail{
    min-height: 500px;
  }
  .num-control{
    margin-left:200px;
  }
</style>