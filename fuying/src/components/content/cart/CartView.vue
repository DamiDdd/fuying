<!--cart条目view-->

<template>
  <div v-if="countExist" id="cart-view" :style="chooseStyle">
    <div class="flag"><input type="checkbox" v-model="good.flag"></div>
    <div class="img"><img :src="good.product_img"></div>
    <div class="title1" @click="jump2detail">{{good.product}}</div>
    <div class="title2">{{good.detail}}</div>
    <div class="price-single">{{good.price}}</div>
    <div class="num-control">
      <div class="reduce" @click="reduceCart"><img src="~assets/img/common/delete.jpg"></div>
      <div class="num">{{good.num}}</div>
      <div class="add" @click="addCart"><img src="~assets/img/common/add.jpg"></div>
    </div>
    <div class="price-sum">{{good.priceSum}}</div>
    <div class="delete"><span  @click="deleteReverse">删除</span>
      <div v-show="this.deleteBtn" class="answer">
        <button class="btn" @click="deleteConfirmed">确定</button>
        <button class="btn" @click="deleteReverse">取消</button>
      </div>
    </div>
  </div>
</template>

<script>
import GLOBAL from '@/common/const'
import Axios from 'axios'

export default {
  name: "CartView",
  props:{
    good: Object,
  },
  data(){
    return{
      deleteBtn: false,
      counturl: GLOBAL.urlHead+"updateCartWeb",
      phone: localStorage.getItem("userPhone"),
    }
  },
  computed:{
    countExist(){
      return this.good.num > 0;
    },
    chooseStyle(){
      if(this.good.flag){
        return "border: 1px solid black";
      }
      else{
        return "";
      }
    }
  },
  mounted(){
  },
  methods:{
    deleteReverse(){
      this.deleteBtn = !this.deleteBtn;
    },
    jump2detail(){
      this.$router.push({path:'/detail',query:{goodId:this.good.product_id}});
    },
    changeNum(){
      let url = this.counturl + "?id=" + this.phone + 
        "&detail_id=" + this.good.detail_id + 
        "&num=" + this.good.num;
      Axios.get(url).then((response) => {
        if(!response.status === 200){
          this.$message({
            type: 'warning',
            message: '后台出错',
          });
        }
      });
    },
    // 添加数量
    addCart(){
      this.good.num++;
      this.good.priceSum = parseFloat(this.good.num * this.good.price).toFixed(2);
      // 向后台传输最新数据
      this.changeNum();
    },
    // 减少数量
    reduceCart(){
      if(this.good.num>1){
        this.good.num--;
        this.good.priceSum = parseFloat(this.good.num * this.good.price).toFixed(2);
        // 向后台传输最新数据
        this.changeNum();
      }
    },
    // 删除购物车条目
    deleteConfirmed(){
      this.good.num = 0;
      this.good.flag = false;
      // 向后台传输数据
      this.changeNum();
    }
  }
}
</script>

<style scoped>
  #cart-view{
    width: 60%;
    min-width: 800px;
    height: 120px;
    border: 1px solid mediumaquamarine;
    margin-left: 400px;
    display: flex;
    margin-bottom: 10px;
    text-align: center;
  }
  .flag, .title1, .title2, .price-single, .num-control, .price-sum, .delete{
    padding-top: 40px;
  }
  .flag{
    width: 10%;
  }
  .img{
    width: 16%;
  }
  .img img{
    height: 120px;
  }
  .title1{    
    width: 14%;
    cursor: pointer;
  }
  .title1:hover{
    font-weight: bold;
  }
  .title2{
    width: 12%;
  }
  .price-single{
    width: 12%;
  }
  .num-control{
    width: 12%;
  }
  .price-sum{
    width: 12%;
  }
  .delete{
    width: 12%;
    cursor: pointer
  }
  .delete span:hover{
    text-decoration: line-through;
  }
  .reduce, .add{
    cursor: pointer;
  }
  .reduce, .num, .add{
    float: left;
    width:33%;
  }
  .reduce img, .add img{
    width: 20px;
  }
  .answer{
    width:100%;
    margin-left: 10px;
    margin-top: 5px;
  }
  .btn{
    float: left;
    width: 60px;
    cursor: pointer;
  }
</style>