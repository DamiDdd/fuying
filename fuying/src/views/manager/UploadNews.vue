<template>
  <div>
    <div class="nav-bg"></div>
    <div class="main">
      <div class="contain">
        <p class="bigtext" style="padding-bottom: 1rem;">上传新闻</p>
        <el-row
          ><p class="title">title</p>
          <el-input v-model="title" class="input"></el-input
        ></el-row>
        <el-row>
          <p class="title">date</p>
          <el-date-picker
            class="picker"
            v-model="date"
            type="date"
            format="yyyy-MM-dd"
            value-format="yyyy-MM-dd"
            placeholder="选择日期时间"
          >
          </el-date-picker
        ></el-row>
        <el-row>
          <p class="title">url</p>
          <el-input v-model="url" class="input"></el-input>
        </el-row>
        <el-row>
          <input
            class="upload-input"
            type="file"
            accept="image/gif,image/jpeg,image/jpg,image/png"
            @change="changeImage($event)"
            ref="avatarInput"
          />
        </el-row>
        <img class="tech-img" :src="img" />
        <el-row
          ><el-button type="primary" class="submitbtn" @click="handleUpload"
            >上传</el-button
          ></el-row
        >
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import GLOBAL from "@/common/const";
import notfound from "../../assets/img/common/notfound.png";

export default {
  name: "UploadNews",
  data() {
    return {
      title: "",
      date: "",
      url: "",
      img: notfound,
      uploadurl: GLOBAL.urlHead2 + "uploadNews/"
    };
  },
  methods: {
    // 改变image
    changeImage(e) {
      var file = e.target.files[0];
      var reader = new FileReader();
      var that = this;
      reader.readAsDataURL(file);
      reader.onload = function() {
        that.img = this.result;
      };
    },
    handleUpload() {
      let that = this;
      let params = new URLSearchParams();
      params.append("title", this.title);
      params.append("date", this.date);
      params.append("url", this.url);
      params.append("img", this.img);
      Axios.post(this.uploadurl, params, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      })
        .then(function(response) {
          console.log(response);
          that.$message({
            type: "success",
            message: "上传成功"
          });
        })
        .catch(function(error) {
          console.log(error);
          that.$message({
            type: "warning",
            message: "请检查上传信息"
          });
        });
    }
  }
};
</script>

<style scoped>
.nav-bg {
  width: 100%;
  min-width: 75rem /* 1200/16 */;
  height: 5.5rem /* 200/16 */;
}
.main {
  /* background: gray; */
  min-height: 60rem;
  width: 80%;
  min-width: 40rem;
  margin-left: auto;
  margin-right: auto;
  border: 0.05rem solid silver;
}
.contain {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 4rem;
}
.tech-img {
  width: 30rem;
  height: 20rem;
}
.input {
  width: 35rem;
}
.upload-input {
  margin-top: 1.5rem;
}
.submitbtn {
  width: 13.75rem /* 220/16 */;
  /* margin-left: 43%; */
  margin-top: 1.25rem /* 20/16 */;
  margin-bottom: 1.25rem /* 20/16 */;
}
.title{
  padding-top: 1.5rem;
}
</style>
