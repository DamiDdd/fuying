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
          <div class="info"></div>
          <div class="image"></div>
        </div>
        <div class="right-middle">
          <p class="content-blue">收件人管理</p>
        </div>
        <div class="right-bottom">

        </div>
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
      address: '',
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
    height: 50%;
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
    border: 1px solid;
    width: 69%;
    height: 80%;
    float: left;
  }

  .image{
    border: 1px solid;
    width: 30%;
    height: 80%;
    float: right;
  }

  .right p{
    margin-left: 5%;
  }
</style>