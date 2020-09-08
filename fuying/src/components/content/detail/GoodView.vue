<template>
  <div class="cartcontrol">
    <div class="main title">{{item.title}}</div>
    <div class="text">{{item.desc}}</div>
    <div class="label"><div class="type" v-for="(i,index) in item.type" :key="index" @click="typeChoose(index)" :class="active(index)">{{i.name}}</div></div>
    <div class="text">
      {{item.type[this.index].tip}}
    </div>    
    <div class="price">
      <span class="price-1">价格</span>
      <span class="price-2">¥</span>
      <span class="price-3">{{sumPrice}}</span>
    </div>
    <div class="reduce" @click="deleteCart"><img src="~assets/img/common/delete.jpg"></div>
    <div class="num">{{item.count}}</div>
    <div class="add" @click="addCart"><img src="~assets/img/common/add.jpg"></div>
    <button id="add2cart" @mouseenter="changeFocus" @mouseleave="removeFocus">加入购物车</button>
    <button id="purchase" @mouseenter="changeFocus" @mouseleave="removeFocus">立即购买</button>
  </div>
</template>

<script>
export default {
  name:"GoodView",
  data(){
    return{
      index: 0
    }
  },
  props:{
    item:{
      type: Object,
      //  默认赋值count为0
      default(){
        return{
          count: 1,
        }
      }
    }
  },
  computed:{
    itemnum(){
      return this.item.count > 0;
    },
    sumPrice(){
      let price = this.item.count * this.item.type[this.index].price;
      price = parseFloat(price).toFixed(2);
      return price;
    },
  },
  methods:{
    active(index){
      if(this.index == index)
        return "active";
      else{        
        return "";
      }
    },
    addCart(){
      this.item.count++;
    },
    deleteCart(){
      if(this.item.count>1)
        this.item.count--;
    },
    typeChoose(index){
      // console.log(index);
      this.item.count = 1;
      this.index = index;
    },
    changeFocus(e) {
      e.currentTarget.className = 'focus';
    },
    removeFocus(e) {
      e.currentTarget.className = 'unfocus';
    },
  }
}
</script>

<style scoped>
  .cartcontrol{
    width: 550px;
    /* background: gray; */
    overflow: hidden;
  }
  .cartcontrol div{
    margin-top: 20px;
  }
  .main{
    font-size: 40px;
  }
  .text{
    /* background: gray; */
    height: 50px;
    font-size: 18px;
    line-height: 23px;
    color:gray;
    overflow: auto;
  }
  .reduce, .add, .type{
    cursor: pointer;
  }
  .reduce, .num{
    float: left;
  }
  .label{
    /* background: gray; */
    width: 600px;
    height: 80px;
    display: flex;
    overflow: auto;
  }
  .type{
    /* width: 130px; */
    height: 30px;
    /* float: left; */
    border: 1px solid wheat;
    margin-left: 20px;
    padding-top: 10px;
    padding-left: 10px;
    padding-right: 10px;
  }
  .type:first-of-type{
    margin-left: 0px;
  }
  .price{
    color:red;
    font-weight: bold;
  }
  .price-1{
    font-size: 20px;
  }
  .price-2{
    font-size: 20px;
    margin-left: 20px;
  }
  .price-3{
    font-size: 40px;
    margin-left: 10px;
  }
  .reduce img, .add img{
    width: 40px;
  }
  .num{
    font-size: 30px;
    margin-left: 30px;
    margin-right: 30px;
    text-align: center;
    width:80px;
  }
  .active{
    border: 1px solid red;
    background: url("~assets/img/common/bingo.jpg") no-repeat bottom right;
    background-size: 12px 12px;
    font-weight: 600;
  }
  button {
    border: none;
    padding: 15px 50px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 24px;
    font-weight: bold;
    cursor: pointer;
    border-radius: 15px;
    outline: none;
  }
  #add2cart{
    background-color: #ffce6b;
    color: #6b6b6b;
    margin-right: 2%;
  }
  #purchase{
    margin-top: 20px;
    background-color: #ffb3a7;
    color:  white;
  }
  .focus{
    border: 0.5px solid gray;
  }
</style>