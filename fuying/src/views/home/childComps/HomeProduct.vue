<!--首页第二个页面，展示一些产品-->

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
        <img src="~assets/img/common/arrow.png" @click="scrollScreen">
      </div>
    </div>
    <div id="intro">
      <div id="intro-top">
        <div class="left">
          <p class="bigtext-blue">
            <span class="yellow sp1">50%</span>以上的标志物是蛋白质
          </p>
          <home-pie></home-pie>
        </div>
        <div class="right">
          <p class="bigtext-blue">
            超过<span class="yellow">98%</span>的药物靶点是蛋白质
          </p>
          <icon-hexa-win></icon-hexa-win>
        </div>
      </div>
      <div id="intro-middle">
        <div class="left">
          <img src="~assets/img/home/transcription.png">
        </div>
        <div class="right smalltext-blue">
          <p>1、蛋白质组是基因组的功能最终行动者</p>
          <p>2、与基因表达水平并非一一对应关系，基因组无法替代蛋白质组</p>
          <p>3、蛋白质组可规避基因组、转录组层面的诸多无效信息</p>
        </div>
      </div>
      <div id="intro-bottom">
        <div class="left">
          <p class="smalltext-blue">
            <span class="yellow">蛋白质组学-生理刻画</span>是通过检测客户生理功能
            （包括常规指标、免疫力指数、器官功能、代谢功能、机体衰老功能等）
            相关的蛋白信息，准确把握生理状态，这个过程叫做“蛋白质组学-生理刻画”
          </p>
          <p class="content">根据蛋白信息为您定制更系统的生活方案，让机体保持青春，让生活更加舒适。</p>
        </div>
        <div class="right">
          <img src="~assets/img/home/index5-p.png">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HomePie from 'components/content/homePie/HomePie'
import IconHexaWin from 'components/content/homeIcons/IconHexaWin'

export default {
  name: "HomeProduct",
  components: {
    HomePie,
    IconHexaWin
  },
  methods: {
    productClick(){
      this.$router.push("/products")
    },
    buyClick(){
      this.$router.push("/products")
    },
    scrollScreen(){
      window.scrollTo({
        top: 2500,
        left: 0,
        behavior: "smooth"
      })
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
    margin-left: 60%;
    padding-top: 160px;
    text-align: center;
  }

  #product-text .title{
    color: var(--text-color);
  }

  #product-text .bigtext-blue span{
    margin-right: 30px;
    margin-left: 20px;
    cursor: pointer;
  }

  #pre-intro{
    width: var(--screen-width);
    height: var(--screen-height);
    text-align: center;
  }

  #pre-intro img{
    cursor: pointer;
  }

  #pre-intro .title{
    width: 900px;
    line-height: 50px;
    margin-left: auto;
    margin-right: auto;
  }

  #pre-intro .bottom{
    margin-top: 350px;
  }

  #intro{
    width: var(--screen-width);
    height: 1800px;
    /* background: -webkit-linear-gradient(top,white,lightblue,white); */
  }

  #intro div{
    overflow: hidden;
  }

  .left{
    float: left;
  }

  .right{
    float: right;
  }

  #intro-top{
    height: 640px;
  }

  #intro-top .left{
    height: 840px;
    width: 900px;
    text-align: center;
  }

  #intro-top .right{
    height: 840px;
    width: 700px;
    text-align: center;
  }
  
  #intro-top #home-pie{
    margin-left: 20%;
    margin-top: -200px;
  }

  #intro-middle{
    height: 260px;
    width: 100%; 
  }

  #intro-middle .left{
    height: 260px;
    width: 1000px;
  }

  #intro-middle .left img{
    height: 200px;
    margin-left: 12%;
    margin-top: 30px;
  }

  #intro-middle .right{
    margin-left: -200px;
    height: 260px;
    width: 40%;
    margin-top: 50px;
  }
  
  #intro-bottom{
    height: 900px;
  }

  #intro-bottom .left{
    height: 900px;
    width: 700px;
    text-indent: 2rem;
  }

  #intro-bottom .left p{
    width: 470px;
    line-height: 30px;
    /* margin-left: 300px; */
    margin-left: 30%;
    margin-top: 200px;
  }

  #intro-bottom .right{
    height: 900px;
    width: 700px;
    margin-right: 120px;
    /* margin-right: 14%; */
  }

  #intro-bottom .right img{
    margin-left: 80px;
  }

  .yellow{
    color: #ffb658;
  }
  .sp1{
    margin-left: 15%;
  }
</style>