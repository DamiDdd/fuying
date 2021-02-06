<!--商品总览页面-->

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
import CartIcon from 'components/common/cart/CartIcon'
import Axios from 'axios'
import GLOBAL from '@/common/const'


export default {
  name: "Products",
  components:{
    ItemWindow,
    CartIcon,
  },
  data(){
    return {
      cartIconStyle: {
        'right': '94px',
        'bottom': '200px',
        'background': '#fff',
        'border-radius':'25px',
      },
      productUrl: GLOBAL.urlHead + "getProducts/",
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
					message: this.$t('tips.servererror'),
				});
      }
    });
  },
  methods:{
    // detail的跳转函数
    enterDetail (id){
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
    padding-left: 13%;
    padding-top: 2%;
  }
  .icon{
    width: 100%;
    min-width: 1000px;
  }

  /* 显示交错效果 */
  .icon:nth-of-type(odd){
    margin-left: -20px;
  }
  .icon:nth-of-type(even){
    margin-left: 40px;
  }
</style>