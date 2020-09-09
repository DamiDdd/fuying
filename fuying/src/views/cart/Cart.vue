<template>
  <div id="cart">
    <p class="title">我的购物车</p>
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
            console.log(element.count);
            sign = false;
          }
        });
      }
      return sign;
    }
  },
  data(){
    return{
      phone: localStorage.getItem("userPhone"),
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
    // this.goods.forEach(element => {
      
    // });
    // 在这里拿到cart数据
  },
  methods:{
    jump2mall(){
      this.$router.push('/products');
    }
  }
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
</style>