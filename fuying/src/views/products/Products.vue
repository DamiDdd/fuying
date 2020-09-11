<template>
  <div id="products">
    <cart-icon :iconStyle="cartIconStyle"></cart-icon>
    <div class="main-div">
      <div class="icon" v-for="(item,index) in goodList" :key="index" @click="enterDetail(item.id)">
        <item-window>
          <p slot="title">{{item.title}}</p>
          <img :src="item.imgurl" slot="img">
          <p slot="desc">{{item.desc}}</p>
        </item-window>
      </div>
    </div>
  </div>
</template>

<script>
import ItemWindow from "components/common/mall/ItemWindow"
// import lab from '../../assets/img/common/lab.png'
// import detect from '../../assets/img/common/detect.png'
import CartIcon from 'components/common/cart/CartIcon'
import Axios from 'axios'


export default {
  name: "Products",
  components:{
    ItemWindow,
    CartIcon,
  },
  props:{
    urlHead:String,
  },
  data(){
    return {
      cartIconStyle: {
        'right': '94px',
        'bottom': '200px',
        'background': '#fff',
        'border-radius':'25px',
      },
      productUrl: this.urlHead + "getProducts",
      goodList:[],
    }
  },
  mounted(){
    // 在这里通过URL获取后端的所有商品信息
    Axios.get(this.productUrl).then((response) => {
      if(response.status === 200){
        this.goodList = response.data['goodList'];
      }
      else{
        this.$message({
          type: 'warning',
					message: '后台出错',
				});
      }
    });

    // this.$set(this.goodList,this.goodList.length,{          
    //   id: "001",
    //   title:"基础套餐",
    //   imgurl: lab,
    //   desc: "基础套餐【19类刻画，44项生理指数;套餐价格仅为500元，购买享受特色服务",})
    // this.$set(this.goodList,this.goodList.length,{          
    //   id: "002",
    //   title:"基础套餐",
    //   imgurl: detect,
    //   desc: "基础套餐【19类刻画，44项生理指数;套餐价格仅为500元，购买享受特色服务",})
    // console.log(this.goodList.length)
  },
  methods:{
    // detail的跳转函数
    enterDetail (id){
      // console.log(id);
      this.$router.push({path:'/detail',query:{goodId:id}});
    }
  },
}
</script>

<style scoped>
  #products{
    min-height:700px;
  }

  .main-div{
    padding-left: 20%;
    padding-top: 2%;
  }
  .icon{
    width: 100%;
  }

  .icon:nth-of-type(odd){
    /* background: #000; */
    margin-left: -20px;
  }
  .icon:nth-of-type(even){
    /* background: gray; */
    margin-left: 40px;
  }
</style>