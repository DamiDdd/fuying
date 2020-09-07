<template>
  <div id="products">
    <div class="main-div">
      <div v-for="(item,index) in goodsList" :key="index" @click="enterDetail(item.id)">
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
import lab from '../../assets/img/common/lab.png'
import detect from '../../assets/img/common/detect.png'


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
      imgurl: lab,
      desc: "基础套餐【19类刻画，44项生理指数;套餐价格仅为500元，购买享受特色服务",})
    this.$set(this.goodsList,this.goodsList.length,{          
      id: "2",
      title:"基础套餐",
      imgurl: detect,
      desc: "基础套餐【19类刻画，44项生理指数;套餐价格仅为500元，购买享受特色服务",})
    console.log(this.goodsList.length)
  },
  methods:{
    // detail的跳转函数
    enterDetail (id){
      console.log(id);
      this.$router.push("/detail");
    }
  },
}
</script>

<style scoped>
  #products{
    min-height:500px;
  }

  .main-div{
    padding-left: 20%;
    padding-top: 2%;
  }
</style>