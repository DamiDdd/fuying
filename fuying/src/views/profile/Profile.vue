<template>
  <div id="profile">
    {{this.phone}}
    <el-button class="exitBtn" @click="jump('/reportEdit')">管理员上传信息</el-button>    
    <el-button class="exitBtn" @click="jump('/report')">查看报告</el-button>
    <el-button class="exitBtn" @click="jump('/pdf')">查看pdf</el-button>
    <el-button class="exitBtn" @click="jump('/exit')">退出登录</el-button>
  </div>
</template>

<script>
export default {
  name : "Profile",
  data(){
    return {
      phone: localStorage.getItem("userPhone"),
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
  #profile{
    min-height:500px;
  }
</style>