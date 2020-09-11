<template>
  <div id="cart">
    <p class="title">我的购物车</p>
    <div class="tips" v-if="!emptyCart">
      <div class="flag"><input type="checkbox" v-model="all" @click="chooseAll"> 全选</div>
      <div class="img"></div>
      <div class="title1">套餐</div>
      <div class="title2">服务内容</div>
      <div class="price-single">单价</div>
      <div class="num-control">数目</div>
      <div class="price-sum">总价</div>
      <div class="delete"></div>
    </div>
    <div v-for="(item,index) in goods" :key="index">
      <cart-view :good="goods[index]"></cart-view>
    </div>
    <div v-if="emptyCart" class="empty" @click="jump2mall">您的购物车空空如也,去商城看看吧！</div>
  </div>
</template>

<script>
import lab from '../../assets/img/common/lab.png'
import CartView from 'components/content/cart/CartView'

export default {
  name: 'Cart',
  components:{
    CartView,
  },
  computed:{
    emptyCart(){
      let sign = true;
      if(this.goods.length == 0){
        return sign;
      }
      else{
        this.goods.forEach(element => {
          if(element.count > 0){
            sign = false;
          }
        });
      }
      return sign;
    },
  },
  data(){
    return{
      phone: localStorage.getItem("userPhone"),
      all: false,
      goods:[
        {
          goodId: "001",
          goodTitle: "生理刻画基本套餐",
          typeId: "2",
          typeTitle: "升级版",
          imgurl: lab,
          price: 200,
          count: 1,
          priceSum: 400,
        },
        {
          goodId: "001",
          goodTitle: "生理刻画基本套餐",
          typeId: "1",
          typeTitle: "基础版",
          imgurl: lab,
          price: 100,
          count: 1,
          priceSum: 200,
        },
      ],
    }
  },
  mounted(){
    // 在这里拿到cart数据

    // 初始化flag参数
    this.goods.forEach(element => {
      this.$set(element,"flag",false);
    });
  },
  methods:{
    chooseAll(){
      this.goods.forEach(element => {
        if(element.count > 0){
          // 在all改变前执行
          element.flag = !this.all;
        }
    });
    },
    jump2mall(){
      this.$router.push('/products');
    }
  },
}
</script>

<style scoped>
  #cart{
    min-height:800px;
  }
  .title{
    margin-left: 400px;
  }
  .empty{
    margin-left: 400px;
  }
  .tips{
    width: 60%;
    min-width: 800px;
    height: 40px;
    margin-left: 400px;
    text-align: center;
    display: flex;
  }
  .flag{
    width: 10%;
    margin-left: 20px;
  }
  .img{
    width: 16%;
  }
  .title1{    
    width: 14%;
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
  }
</style>