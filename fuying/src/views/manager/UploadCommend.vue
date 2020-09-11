<template>
  <div id="upload-commend">
    <input type="text" placeholder="请输入用户编号" v-model="user">
    <button @click="searchUser">查询</button>
  </div>
</template>

<script>
export default {
  name: "UploadCommend",
  props:{
    urlHead:String,
  },
  data(){
    return{
      user: "",
      findUrl: this.urlHead + "getevaluation?exp="+this.user,
    }
  },
  methods:{
    searchUser(){

    }
  }
}
</script>

<style>

</style>