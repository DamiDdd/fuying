<template>
<div>
<!-- action替换为目标后台网址 -->
<!-- data替换为商品信息、分组信息 -->
<!-- limit为当前组别的最大上传数 -->
<el-upload
  :action="URL"
  :data="goodData"
  accept="image/png,image/gif,image/jpg,image/jpeg"
  ref="upload"
  :auto-upload="false"
  :multiple="true"
  list-type="picture-card"
  :limit="limit"
  :on-preview="handlePictureCardPreview"
  :on-remove="handleRemove"
  :on-change="handleChange"
  :on-exceed="handleExceed"
  >
  <i class="el-icon-plus"></i>
</el-upload>
<!-- <el-button @click="sendPic" type="primary">点击上传</el-button> -->
<el-dialog :visible.sync="dialogVisible">
  <img width="100%" :src="dialogImageUrl" alt="">
</el-dialog>
</div>
</template>

<script>
export default {
  name: "UploadImg",
  props:{
    limit:{
      type: Number,
      default:3,
    },
    URL:{
      type: String,
      default:"#",
    },
    goodData:{
      type: Object,
    }
  },
  data() {
    return {
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
    }
  },
  methods: {
    handleRemove(file,fileList) {
      console.log(file,fileList);
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    handleChange(file,fileList){
      console.log(file,fileList);
    },
    handleExceed(){
      this.$message({
        type:"warning",
        message:"当前组最多上传"+this.limit+"个文件",
      })
    },
    sendPic(){
      console.log(this.goodData.id+this.goodData.name+"...uploading");
      this.$refs.upload.submit();
    }
  }
}
</script>

<style scoped>

</style>