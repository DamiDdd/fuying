<!--个人档案页面-->

<template>
  <div id="profile">
    <div class="main">
      <div class="left">
        <div class="left-top">
          <p class="content-blue">功能列表</p>
          <el-button @click="jump('/cart')">查看购物车</el-button>
          <el-button @click="callOn">查看订单</el-button>
          <!-- <el-button @click="jump('/pdf')">查看报告</el-button> -->
          <el-button class="warning" @click="jump('/exit')">退出登录</el-button>
        </div>
        <div v-show="admin" class="left-bottom">
          <p class="content-blue">管理员</p>
          <el-button @click="jump('/reportEdit')">管理员上传信息</el-button>    
          <el-button @click="jump('/manager')">报告管理</el-button>    
          <!-- <el-button @click="jump('/uploadCommend')">管理员上传评价</el-button> -->
        </div>
      </div>
      <div class="right">
        <div class="right-top">
          <p class="content-blue">个人信息</p>
          <div class="info">
            <div class="info-content">
              <!-- <p>用户名：<input type="text" v-model="name"></p> -->
              <p>用户名：{{name}}</p>
              <p>手机号：{{phone}}</p>
              <!-- <p>邮箱：<input type="text" v-model="email"></p> -->
              <p>邮箱：{{email}}</p>
            </div>
            <div class="btn">
              <!-- <el-button>修改密码</el-button> -->
              <!-- <el-button @click="submitMsg">提交修改</el-button> -->
            </div>
          </div>
          <div class="image">
            <img src="~assets/img/common/user.png">
          </div>
        </div>
        <div class="right-middle">
          <p class="content-blue">收件人管理</p>
          <el-table :data="addressTable" class="data_table">
            <el-table-column prop="user" label="收件人姓名" width="180"></el-table-column>
            <el-table-column prop="phone" label="电话" width="180"></el-table-column>
            <el-table-column prop="address" label="地址" width="400"></el-table-column>
            <!-- <el-table-column label="操作" width="100"></el-table-column> -->
          </el-table>
        </div>
        <!-- <div class="right-bottom">
        </div> -->
      </div>
    </div>
    <modal :show="modal" :title="titleM" v-on:hideModal="hideModal" v-on:submit="confirm">
      <div class="in-content">
        <table class="el-table el-table--fit el-table--border table-detail">
          <thead>
            <tr>
              <th width="160px">服务</th>
              <th width="160px">下单日期</th>
              <th width="160px">数目</th>
              <th width="160px">总价</th>
              <th width="160px">状态</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td colspan="5" style="text-align: center;" v-show="emptyOrder">暂无信息！</td>
            </tr>
            <tr v-for="(item,index) in orderInList" :key="index">
              <td @click="jump2detail(item.product_id)" class="good">{{item.product}}-{{item.detail}}</td>
              <td v-text="item.date"></td>
              <td v-text="item.num"></td>
              <td v-text="item.priceSum"></td>
              <td class="available" v-show="available(item.status)" @click="solveStatus(item.order_id,item.phone,item.status)" v-text="item.status"></td>
              <td v-show="!available(item.status)" v-text="item.status"></td>
            </tr>
          </tbody>
        </table>
        <table v-show="transport" class="el-table el-table--fit el-table--border table-detail transport">
          <thead>
            <tr>
              <th width="100px">订单号</th>
              <th width="100px">物流号</th>
              <th width="100px">时间</th>
              <th width="200px">运输信息<span class="after" @click="unspread">^收起</span></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item,index) in transportMsg" :key="index">
              <td v-text="item.orderID"></td>
              <td v-text="item.ExpressNumber"></td>
              <td v-text="item.time"></td>
              <td v-text="item.context"></td>
            </tr>
          </tbody>
        </table>
      </div>
    </modal>
  </div>
</template>

<script>
import Modal from 'components/common/modal/Modal'
import GLOBAL from '@/common/const'
import Axios from 'axios'

export default {
  name : "Profile",
  components:{
    Modal,
  },
  data(){
    return {
      phone: localStorage.getItem("userPhone"),
      name: localStorage.getItem("userName"),
      email: localStorage.getItem("userEmail"),
      orderUrl: GLOBAL.urlHead + "getOrders/",
      transportUrl: GLOBAL.urlHead + "getExpressList/",
      addUrl: GLOBAL.urlHead + "getCommonlyAddress/",
      pdfUrl: GLOBAL.urlHead2 + "get_pdf/",
      emptyOrder: false,
      transport: false,
      addressTable:[{
        user: "a",
        phone: "13333333333",
        address: "北京",
      }],
      modal: false,
      titleM: "您的订单",
      orderInList:[{
        order_id: "A01",
        product: "基础套餐",
        product_id: "00001",
        detail: "升级版",
        detail_id: "1",
        product_img: "",
        price: 200,
        num: 2,
        priceSum: 400,
        date: "2020/9/1 10:00",
        status: "pending",
      }],
      transportMsg:[],
    }
  },
  mounted(){
    let url = this.addUrl + "?phone=" + this.phone;
    Axios.get(url).then((response) => {
      if(response.status === 200){
        let data = response.data;
        // console.log(data);
        this.addressTable = data;
      }
    }).catch((error)=>{
      this.$message({
        type: 'warning',
        message: '后台出错',
      });
      console.log(error);
    });
  },
  computed:{
    admin(){
      if(localStorage.getItem("admin")!=null){
        return true;
      }
      else{
        return false;
      }
    },
  },
  methods:{
    available(status){
      if(status === "in_transit" || status === "report")
        return true;
      else{
        return false;
      }
    },
    solveStatus(order_id,phone,status){
      switch(status){
        case "in_transit":
          this.transport = true;
          Axios.post(this.transportUrl+"?orderID="+order_id+"&phone="+phone).then((response) => {
            if(response.status === 200){
              let data = response.data;
              // console.log(data);
              this.transportMsg = data;
            }
          }).catch((error)=>{
            this.$message({
              type: 'warning',
              message: '后台出错',
            });
            console.log(error);
          });
          break;
        case "report":
          var url = this.pdfUrl+"orderID="+order_id+"&phone="+phone;
          window.open(url);
          break;
        default:
          break;
      }
    },
    unspread(){
      this.transport = false;
    },
    jump(link) {
      this.$router.push(link);
    },
    jump2detail(goodId){
      this.$router.push({path:'/detail',query:{goodId:goodId}});
    },
    submitMsg(){
      console.log(this.name + this.email);
    },
    callOn(){
      this.modal = true;
      let url = this.orderUrl +"?phone="+ this.phone;
      Axios.get(url).then((response) => {
        if(response.status === 200){
          let data = response.data;
          console.log(data);
          this.orderInList = data;
          if(this.orderInList.length === 0){
            this.emptyOrder = true;
          }
        }
      }).catch((error)=>{
        this.$message({
          type: 'warning',
          message: '后台出错',
        });
        console.log(error);
      });
    },
    hideModal(){
      this.modal = false;
      this.transport = false;
    },
    confirm(){
      this.modal = false;
      this.transport = false;
    }
  }
}
</script>

<style scoped>
  #profile{
    background: url("~assets/img/bg/doctor.png") no-repeat bottom left;
  }

  .main{
    width: 100%;
    min-width: var(--min-width);
    height: 1000px;
    /* border: 1px solid; */
    /* margin-left: 14%; */
    margin-top: 80px;
    display: flex;
  }

  .left{
    width: 30%;
    height: 100%;
    margin-left: 14%;
  }

  .left div button{
    width: 80%;
    margin-left: 10%;
    margin-bottom: 2%;
  }

  .left div p{
    text-align: center;
  }

  .right{
    width: 50%;
    height: 100%;
  }

  .left-top{
    width: 80%;
    height: 50%;
    margin-left: 10%;
    border: 1px solid var(--theme-color);
  }

  .left-bottom{
    width: 80%;
    height: 30%;
    margin-left: 10%;
    border: 1px solid var(--theme-color);
  }
  
  .right-top{
    width: 100%;
    height: 40%;
    border: 1px solid;
  }

  .right-middle{
    width: 100%;
    height: 40%;
    border: 1px solid;
  }

  .right-bottom{
    width: 100%;
    height: 20%;
    border: 1px solid;
  }

  #profile{
    min-height:500px;
  }

  .warning{
    color: red;
    font-weight: bold;
  }

  .info{
    width: 69%;
    height: 80%;
    float: left;
  }

  .info p{
    font-weight: bold;
    margin-top: 5%;
    padding-left: 5%;
    font-size: 20px;
  }

  .info-content{
    height: 70%;
  }

  .btn{
    display: flex;
    margin-left: 30%;
  }

  .btn button{
    margin-top: 2%;
    margin-left: 10%;
  }

  .image{
    width: 30%;
    height: 80%;
    float: right;
  }

  .image img{
    min-width: 200px;
    width: 80%;
  }

  .right p{
    margin-left: 5%;
  }
  
  input{
    border: none;
    font-weight: bold;
  }

  .data_table{
    margin-left: 5%;
    width: 95%;
    height: 300px;
    overflow: auto;
  }

  .in-content{
    width: 800px;
    height: 500px;
    overflow: auto;
  }
  
  .good{
    cursor: pointer;
  }

  .good:hover{
    font-weight: bold;
  }

  .transport{
    margin-top: 80px;
  }

  .after{
    float: right;
    margin-right: 10px;
    color: lightblue;
    cursor: pointer;
  }

  .available{
    cursor: pointer;
  }
  .available:hover{
    color: lightblue;
    font-weight: bold;
  }
</style>