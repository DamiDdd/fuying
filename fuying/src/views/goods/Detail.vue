<!--详情页面-->

<template>
  <div id="detail">
  <cart-icon :iconStyle="cartIconStyle"></cart-icon>
    <div class="num-control">
      <!-- slider未传入图片参数时，默认显示没有相关信息图样 -->
      <div class="left"><slider :imgWidth=600></slider></div>
      <div class="right"><good-view :item="good"></good-view></div>
    </div>
    <div class="img-window">
      <div class="label">
        <div class="type" v-for="(i,index) in good.imgs" :key="index" @click="tagChoose(index)" :class="judgeActive(index)">
          <div @mouseenter="changeFocus" @mouseleave="removeFocus">{{i.name}}</div>
        </div>
      </div>
      <div class="imgs">
        <img v-for="(i,index) in good.imgs[this.index].imgs" :key="index" :src="i">
      </div> 
    </div>
  </div>
</template>

<script>
import GoodView from "components/content/detail/GoodView"
import Slider from "components/common/slide/Slider";
import CartIcon from 'components/common/cart/CartIcon'
import Axios from 'axios'
import GLOBAL from '@/common/const'


export default {
  name: "Detail",
  components:{
    GoodView,
    Slider,
    CartIcon
  },
  data(){
    return{
      detailUrl: GLOBAL.urlHead +"getproductsdetail?id=",
      goodId: 0,
      index:0,
      // 关于iconStyle的细节设定
      cartIconStyle: {
        'right': '94px',
        'bottom': '200px',
        'background': '#fff',
        'border-radius':'25px',
      },
      // 传参
      good:{
        title: "",
        count: 1,
        desc: "",
        index: 0,
        type:[
          // 数据样例
          // {
          //   id: "1",
          //   name:"基础生理刻画套餐",
          //   tip:"包括基础",
          //   price: 100.10,
          // },
        ],
        imgs:[
          // 数据样例
          // {
          //   name:"服务详情",
          //   imgs:[
          //     "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1020757406,2710278676&fm=26&gp=0.jpg",
          //     "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1020757406,2710278676&fm=26&gp=0.jpg"
          //   ],
          // },
        ]
      }
    }
  },
  mounted(){
    this.goodId = this.$route.query.goodId;
    this.good['count'] = 1;
    this.detailUrl += this.goodId
    //  在这里申请拿到商品数据
    Axios.get(this.detailUrl).then((response) => {
      if(response.status === 200){
        console.log(response.data);
        // 不需要双向绑定
        let data = response.data;
        this.good.desc = data.desc;
        this.good.imgs = data.imgs;
        this.good.type = data.type;
        this.good.title = data.title;
      }
      else{
        this.$message({
          type: 'warning',
					message: '后台出错',
				});
      }
    });

  },
  methods:{
    tagChoose(index){
      this.index = index;
    },
    judgeActive(index){
      if(this.index === index){
        return "active"
      }
      else{
        return ""
      }
    },
    changeFocus(e){
      e.currentTarget.className = 'focus';
    },
    removeFocus(e) {
      e.currentTarget.className = '';
    },
  }
}
</script>

<style scoped>
  #detail{
    min-height: var(--screen-height);
    width: var(--screen-width);
    background: -webkit-linear-gradient(top,white,lightblue,white);
  }
  .num-control{
    min-height: 600px;
    width: 80%;
    margin-left:200px;
    padding-top: 100px;
  }
  .left{
    float: left;
    width: 800px;
    min-height: 450px;
    margin-top: 80px;
  }
  .right{
    float: left;
    position: absolute;
    margin-left: 800px;
    width: 800px;
    min-height: 600px;
  }
  .cartcontrol{
    height: 700px;
    margin-left: 100px; 
  }
  .img-window{
    margin-top: 130px;
    margin-left: 19%;
    min-height: 600px;
    width: 70%;
  }
  .label{
    margin-left: 5%;
  }
  .type{
    float: left;
    width: 10%;
    height: 30px;
    text-align: center;
    border:1px solid #ccc; 
    border-style:none solid;
    padding-top: 8px;
    cursor: pointer;  
  }
  /* 设定图片菜单选中样式 */
  .active{
    background: url("~assets/img/common/topbar-bt-bg.png") no-repeat top center;
    background-size: 90% 10%;
    font-weight: 600;
  }
  .imgs{
    padding-top: 45px;
    padding-bottom: 200px;
  }
  .imgs img{
    width: 90%;
    margin-left: 5%;
    padding-top: 0.5%;
  }
  .imgs img:first-of-type{
    padding-top:0;
  }
  .focus{
    font-weight: 600;
  }
</style>