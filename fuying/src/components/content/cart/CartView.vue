<template>
  <div v-if="countExist" id="cart-view" :style="choose">
    <div class="flag"><input type="checkbox" v-model="good.flag"></div>
    <div class="img"><img :src="good.imgurl"></div>
    <div class="title1" @click="jump2detail">{{good.goodTitle}}</div>
    <div class="title2">{{good.typeTitle}}</div>
    <div class="price-single">{{good.price}}</div>
    <div class="num-control">
      <div class="reduce" @click="deleteCart"><img src="~assets/img/common/delete.jpg"></div>
      <div class="num">{{good.count}}</div>
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
export default {
  name: "CartView",
  props:{
    good: Object,
  },
  data(){
    return{
      deleteBtn: false,
    }
  },
  computed:{
    countExist(){
      return this.good.count > 0;
    },
    choose(){
      if(this.good.flag){
        return "border: 1px solid black";
      }
      else{
        return "";
      }
    }
  },
  mounted(){
    this.good.price = parseFloat(this.good.price).toFixed(2);
    this.good.priceSum = parseFloat(this.good.count * this.good.price).toFixed(2);
  },
  methods:{
    deleteReverse(){
      this.deleteBtn = !this.deleteBtn;
    },
    jump2detail(){
      this.$router.push({path:'/detail',query:{goodId:this.good.goodId}});
    },
    addCart(){
      this.good.count++;
      this.good.priceSum = parseFloat(this.good.count * this.good.price).toFixed(2);
      // 向后台传输最新数据
    },
    deleteCart(){
      if(this.good.count>1){
        this.good.count--;
        this.good.priceSum = parseFloat(this.good.count * this.good.price).toFixed(2);
        // 向后台传输最新数据
      }
    },
    deleteConfirmed(){
      this.good.count = 0;
      this.good.flag = false;
      // console.log(this.good.count);
      // 向后台传输数据
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