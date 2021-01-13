<template>
  <div class="windows">
    <el-row class="topRow">
      <el-input class="short-input" v-model="search_num"></el-input>
      <el-button type="primary" class="right-btn" @click="searchNum">搜索用户</el-button>
    </el-row>

  </div>
</template>

<script>
export default {
  name : "Manager",
  data(){
    return{
      search_num: "",
      
    }
  },

  methods:{
    searchNum(){
      console.log(this.search_num);
    },
  }
}
</script>

<style scoped>
  .windows{
    width: 80%;
    margin-top: 20px;
    min-width: 1000px;
    min-height: 700px;
    margin-left: auto;
    margin-right: auto;
  }
  .topRow{
    width: 100%;
  }
  .short-input{
    width: 200px;
    padding-right: 10px;
  }
</style>