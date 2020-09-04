<template>
  <div id="detail">
    <div class="num-control">
      <div class="left"><slider :imgWidth=600></slider></div>
      <div class="right"><good-view :item="good"></good-view></div>
    </div>
    <div class="img-window">
      <div class="label">
        <!-- <div class="type" v-for="(i,index) in good.imgs" :key="index" @click="typeChoose(index)" :class="active(index)">{{i.name}}</div> -->
        <div class="type" v-for="(i,index) in good.imgs" :key="index">{{i.name}}</div>
      </div>
      <div class="imgs">
        <!-- {{good.imgs[this.index].imgs}} -->
        <!-- <img v-for="" src="" alt=""> -->
      </div> 
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
          }
        ],
        imgs:[
          {
            name:"1",
            imgs:[
              "",
              "",
              ""
            ],
          },
          {
            name:"2",
            imgs:[
              "",
              ""
            ],
          },
          {
            name:"3",
            imgs:[
              "",
              ""
            ],
          },
        ]
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
    min-height: var(--screen-height);
    width: var(--screen-width);
    /* background: gray; */
  }
  .num-control{
    min-height: 600px;
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
    min-height: 600px;
    background: url("~assets/img/bg/item-bg.jpg") top right;
    background-size: 100% 100%;
  }
  .cartcontrol{
    height: 700px;
    margin-left: 100px; 
  }
  .img-window{
    margin-top: 130px;
    min-height: 600px;
    /* background: #000; */
  }
</style>