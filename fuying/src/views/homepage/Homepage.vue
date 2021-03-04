<template>
  <div class="main">
    <div class="contain">
      <el-carousel trigger="click" height="880px">
        <el-carousel-item v-for="item in imgsrc" :key="item">
          <h3 class="small"><img :src="item" /></h3>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="menu">
      <div class="btn-window">
        <div class="icon">
          <img src="~assets/img/common/detect.png" alt="" />
          <h3>科技服务</h3>
        </div>
      </div>
      <div class="btn-window">
        <div class="icon">
          <img src="~assets/img/common/detect.png" alt="" />
          <h3>科技服务</h3>
        </div>
      </div>
      <div class="btn-window">
        <div class="icon">
          <img src="~assets/img/common/detect.png" alt="" />
          <h3>科技服务</h3>
        </div>
      </div>
      <div class="btn-window">
        <div class="icon">
          <img src="~assets/img/common/detect.png" alt="" />
          <h3>科技服务</h3>
        </div>
      </div>
    </div>
    <div class="showdata">
      <h1 class="bigtext-blue first">复瑛健康</h1>
      <h1 class="bigtext-blue">蛋白质医学研发网络</h1>
      <br />
      <h3>三个计算中心 亿级存储计算能力，万级并发服务能力</h3>
      <h3>三个检测中心 十万级检测能力</h3>
      <h3>九个队列中心 万级样本</h3>
      <img src="~assets/img/home/map.png" />
    </div>
    <div class="company">
      <el-row :gutter="8">
        <h2 style="text-align: center;" class="content title">合作伙伴</h2>
        <el-col v-for="item in 6" :key="item" :span="4">
          <el-card shadow="always" style="width: 140px;">
            <img src="~assets/img/home/university/Fudan.png" />
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import temp1 from "../../assets/img/bg/bgtemp1.jpg";
import temp2 from "../../assets/img/bg/bgtemp2.jpg";

export default {
  name: "Homepage",
  data() {
    return {
      imgsrc: [temp1, temp2]
    };
  }
};
</script>

<style scoped>
.main {
  background: #fffafa;
}

.contain {
  width: 100%;
  min-width: 1000px;
  min-height: 1000px;
  text-align: center;
}

.menu {
  margin-top: -120px;
  width: 100%;
  min-width: 1000px;
  height: 860px;
  background: url("~assets/img/bg/home-bg.jpg") no-repeat center;
}

.btn-window {
  width: 24.8%;
  height: 100%;
  float: left;
  background: #000;
  opacity: 0.8;
  border: 1px solid white;
  color: white;
  cursor: pointer;
}

.icon {
  width: 220px;
  height: 220px;
  /* background: gray; */
  margin-left: auto;
  margin-right: auto;
  margin-top: 320px;
}

.icon img {
  height: 200px;
  width: 200px;
  margin-left: 10px;
}

.icon h3 {
  padding-left: 20px;
}

.btn-window:hover {
  opacity: 0.6;
  /* font-size: 20px; */
}

.showdata {
  background: -webkit-linear-gradient(top, white, lightblue, white);
  padding-top: 30px;
  position: relative;
  min-width: 1000px;
  height: 500px;
  margin-left: auto;
  margin-right: auto;
  padding-top: 100px;
}

.showdata img {
  float: right;
  position: absolute;
  right: 15%;
  bottom: 100px;
  opacity: 0.6;
}

.showdata img:hover {
  opacity: 1;
}

.showdata h1,
h3 {
  position: relative;
  margin-left: 20%;
}

.company {
  width: 1000px;
  height: 300px;
  margin-left: auto;
  margin-right: auto;
}

.company img {
  width: 112px;
}

.title {
  margin-bottom: 30px;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
