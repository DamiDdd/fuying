<template>
  <div id="products">
    <div class="main-div">
      <item-window v-for="(item,index) in goodsList" :key="index">
        <p slot="title">{{item.title}}</p>
        <img :src="item.imgurl" slot="img">
        <p slot="desc">{{item.desc}}</p>
      </item-window>
    </div>
  </div>
</template>

<script>
import ItemWindow from "components/common/mall/ItemWindow"

export default {
  name: "Products",
  components:{
    ItemWindow,
  },
  data(){
    return {
      goodsList:[],
    }
  },
  mounted(){
    // 在这里通过URL获取后端的所有商品信息
    this.$set(this.goodsList,this.goodsList.length,{          
      id: "1",
      title:"基础套餐",
      imgurl: "https://www.fenghbio.cn/themes/echq/images/con1.jpg",
      desc: "基础套餐【19类刻画，44项生理指数;套餐价格仅为500元，购买享受特色服务",})
    console.log(this.goodsList.length)
  },
  props:{
  },
}
</script>

<style scoped>
  #products{
    min-height:500px;
  }

  .main-div{
    padding-left:200px;
  }
</style>