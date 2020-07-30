<template>
  <div id="home-product">
    <div id="pre-product">
      <div id="product">
        <div id="product-text">
          <p class="smalltext-blue">基础套餐【19类刻画，44项生理指数】</p>
          <p class="title">复瑛健康蛋白质组学生理刻画个人版</p>
          <p class="smalltext">套餐价格仅为500元，购买享受特色服务</p>
          <p class="bigtext-blue"><span @click="productClick">了解详情 ></span><span @click="buyClick">购买 ></span></p>
        </div>
      </div>
      <div id="pre-intro">
        <p class="bigtext">蛋白质组学</p>
        <p class="title">蛋白质组学是以蛋白质为研究对象，研究细胞、组织或生物体蛋白质种类、组成及其变化规律的科学</p>
        <p class="bigtext-blue bottom">为什么要检测蛋白质？</p>
        <img src="~assets/img/common/arrow.png">
      </div>
    </div>
    <div id="intro">
      <div id="intro-top">
        
      </div>
      <div id="intro-middle">
        <div class="right">
        
        </div>
        <div class="left">
        
        </div>
      </div>
      <div id="intro-bottom">
        
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeProduct",
  methods: {
    productClick(){
      this.$router.replace("/products")
    },
    buyClick(){
      this.$router.replace("login")
    }
  }
}
</script>

<style scoped>
  #home-product{
    width: var(--screen-width);
  }

  #pre-product{
    background: -webkit-linear-gradient(top,white,lightblue,white);
  }
  
  #product{
    background: url("~assets/img/home/product.png") no-repeat;
    background-position: 150px 0px;
    height: var(--screen-height);
  }
  
  #product-text{
    width: 600px;
    height: 300px;
    position: relative;
    margin-left: 1000px;
    padding-top: 160px;
    /* background: gray; */
    text-align: center;
  }

  #product-text .title{
    color: var(--text-color);
  }

  .bigtext-blue span{
    margin-right: 30px;
    margin-left: 20px;
    cursor: pointer;
  }

  #pre-intro{
    width: var(--screen-width);
    height: var(--screen-height);
    /* background: gray; */
    text-align: center;
  }

  #pre-intro .title{
    width: 900px;
    line-height: 50px;
    margin-left: auto;
    margin-right: auto;
  }

  .bottom{
    margin-top: 350px;
  }

  #intro{
    width: var(--screen-width);
    height: 1800px;
    background: -webkit-linear-gradient(top,white,lightblue,white);
  }

  #intro-top{
    height: 640px;
    background: whitesmoke;
  }

  #intro-middle{
    height: 260px;
    background: beige;
  }

  #intro-bottom{
    height: 900px;
    background: gray;
  }
</style>