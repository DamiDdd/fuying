<!--个人档案页面-->

<template>
  <div id="profile">
    <div class="main">
      <div class="left">
        <div class="left-top">
          <p class="content-blue">功能列表</p>
          <el-button @click="jump('/cart')">查看购物车</el-button>
          <el-button >查看订单</el-button>
          <el-button @click="jump('/pdf')">查看报告</el-button>
          <el-button class="warning" @click="jump('/exit')">退出登录</el-button>
        </div>
        <div v-show="admin" class="left-bottom">
          <p class="content-blue">管理员</p>
          <el-button @click="jump('/reportEdit')">管理员上传信息</el-button>    
          <el-button @click="jump('/uploadCommend')">管理员上传评价</el-button>
        </div>
      </div>
      <div class="right">
        <div class="right-top">
          <p class="content-blue">个人信息</p>
          <div class="info">
            <div class="info-content">
              <p>用户名：<input type="text" v-model="name"></p>
              <p>手机号：{{phone}}</p>
              <p>邮箱：<input type="text" v-model="email"></p>
            </div>
            <div class="btn">
              <el-button>修改密码</el-button>
              <el-button @click="submitMsg">提交修改</el-button>
            </div>
          </div>
          <div class="image">
            <img src="~assets/img/common/user.png">
          </div>
        </div>
        <div class="right-middle">
          <p class="content-blue">收件人管理</p>
          <el-table :data="addressTable" class="data_table">
            <el-table-column prop="name" label="收件人姓名" width="100"></el-table-column>
            <el-table-column prop="phone" label="电话" width="180"></el-table-column>
            <el-table-column prop="address" label="地址" width="320"></el-table-column>
            <el-table-column label="操作" width="100"></el-table-column>
  </el-table>
        </div>
        <!-- <div class="right-bottom">

        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name : "Profile",
  data(){
    return {
      phone: localStorage.getItem("userPhone"),
      name: '',
      email: '',
      addressTable:[{
        name: "a",
        phone: "13333333333",
        address: "北京",
      },{
        name: "b",
        phone: "13333333333",
        address: "上海",
      }],
    }
  },
  computed:{
    admin(){
      if(localStorage.getItem("admin")!=null){
        return true;
      }
      else{
        return false;
      }
    }
  },
  methods:{
    jump(link) {
      this.$router.push(link)
    },
    submitMsg(){
      console.log(this.name + this.email);
    }
  }
}
</script>

<style scoped>
  .main{
    width: 75%;
    min-width: 1200px;
    height: 1000px;
    /* border: 1px solid; */
    margin-left: 14%;
    margin-top: 80px;
    display: flex;
  }

  .left{
    width: 35%;
    height: 100%;
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
    width: 65%;
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
    margin-left: 20%;
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
    width: 700px;
  }
</style>