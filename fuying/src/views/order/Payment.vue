<template>
  <div class="main">
    <h2 class="title">请确认您的订单信息</h2>
    <el-table :data="orderList" class="data_table">
      <!-- <el-table-column prop="img" label="图" width="182"></el-table-column> -->
      <el-table-column prop="title" label="服务" width="300"></el-table-column>
      <el-table-column prop="name" label="收件人" width="200"></el-table-column>
      <el-table-column prop="num" label="数量" width="200"></el-table-column>
      <el-table-column prop="total" label="总价" width="200"></el-table-column>
    </el-table>
    <div class="scan">
      <h2 class="bigtext">请支付<span class="bigtext-blue">¥{{total}}</span>元</h2>
      <img :src="scancode">
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import GLOBAL from '@/common/const'

export default {
  name: 'Payment',
  data(){
    return{
      paymentID:"",
      orderList: [],
      total: 200,
      scancode:"",
      count: 0,
      getCodeUrl: GLOBAL.urlHead+"paymentQRcode/",
      getStatusUrl: GLOBAL.urlHead+"paymentStatus/",
    }
  },
  mounted(){
    this.paymentID = this.$route.query.id;
    console.log(this.paymentID);
    Axios.get(this.getCodeUrl+"?paymentID="+this.paymentID).then((response)=>{
      if(response.status === 200 && response.data['success']){
        let data = response.data;
        this.scancode = data.QRcode;
        this.orderList = data.order_list;
        this.orderList.forEach(element => {
          element.title = element.title+"-"+element.subtile;
        });
        this.total = data.total;
        let timer = setInterval(() => {
          this.count++;
          console.log(this.count);
          if(this.count >= 1000){
            clearInterval(timer);
          }
        },100)
      }
    });
  },
  methods:{
  }
}
</script>

<style scoped>
  .main{
    width: 80%;
    min-width: 1200px;
    min-height: 1000px;
    margin-top: 2 0px;
    margin-left: auto;
    margin-right: auto;
    /* border: solid 1px; */
  }
  .title{
    padding-left: 100px;
  }
  .data_table{
    width: 960px;
    height: 350px;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
  }
  .scan{
    width: 960px;
    height: 500px;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    /* border: solid 1px; */
  }
  .scan img{
    width: 420px;
    height: 420px;
  }
  .scan span{
    margin-left: 10px;
    margin-right: 10px;
  }
  
</style>