<template>
  <div class="main">
    <div class="center rcorner">
    
      <div v-for="(item,i) in imgList" :key="i">
        <upload-img ref="upload" :URL="uploadImgUrl" :limit="limit" :goodData="item"></upload-img>
        <el-button v-show="first(i)" @click="deleteImg(i)">删除分组</el-button>
      </div>
      <el-button @click="addTitle">增加分组</el-button>
      <el-button @click="sendPic" type="primary">点击上传</el-button>
    </div>
  </div>
</template>

<script>
import UploadImg from "common/upload/UploadImg"

export default {
  name: "UploadGood",
  components:{
    UploadImg,
  },
  data(){
    return{
      limit: 3,
      uploadImgUrl: "#",
      imgList: [{id:"01",name:"_slides"}],
      title: "",
      desc: "",
      type: [],
    }
  },
  methods:{
    // 发送图片
    sendPic(){
      let refDic = this.$refs.upload;
      refDic.forEach(element => {
        // console.log(element);
        element.sendPic();
      });
    },
    // 增加图片组
    addTitle(){
      // 这里需要用push使得v-for实时更新
      this.imgList.push({id:"01",name:"add"});
      console.log(this.imgList);
    },
    // 删除图片组
    deleteImg(i){
      console.log(i);
      this.imgList.splice(i,1);
    },
    // 判断是否为第一
    first(i){
      if(i !== 0){
        return true;
      }
      else{
        return false;
      }
    }
  }
}
</script>

<style scoped>
  .main{
    height: 1400px;
    width: 100%;
    min-width: 1600px;
  }
  .center{
    height: 1300px;
    width: 90%;
    margin-left: 5%;
    margin-top: 20px;
  }
</style>