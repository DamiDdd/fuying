<template>
  <div class="main">
    <div class="contain">
      <el-carousel trigger="click" height="60rem">
        <el-carousel-item v-for="item in imgsrc" :key="item">
          <h3 class="small">
            <img width="100%" :src="item" />
          </h3>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="menu">
      <div class="btn-window" @click="jump('/news')">
        <div class="icon">
          <img src="~assets/img/common/microscope.png" alt="" />
          <h3>检测手段</h3>
        </div>
      </div>
      <div class="btn-window" @click="jump('/intro')">
        <div class="icon">
          <img src="~assets/img/common/detect.png" alt="" />
          <h3>技术原理</h3>
        </div>
      </div>
      <div class="btn-window" @click="jump('/products')">
        <div class="icon">
          <img src="~assets/img/common/listener.png" alt="" />
          <h3>科技服务</h3>
        </div>
      </div>
      <div class="btn-window">
        <div class="icon">
          <img src="~assets/img/common/find.png" alt="" />
          <h3>健康问答</h3>
        </div>
      </div>
    </div>
    <div class="detail-window">
      <div class="showdata">
        <h1 class="bigtext-blue first">iproteome健康</h1>
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
          <el-col v-for="(i, index) in universities" :key="index" :span="4">
            <el-card
              shadow="always"
              style="height: 10rem /* 160/16 */;width: 8.75rem /* 140/16 */; cursor:pointer;"
            >
              <img :src="i.src" @click="goPage(i.href)" class="card-img" />
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
import doctor from "../../assets/img/bg/doctor-bg.jpg";
import medical from "../../assets/img/bg/medical-bg.jpg";
import Fudan from "../../assets/img/home/university/Fudan.jpg";
import Harvard from "../../assets/img/home/university/Harvard.jpg";
import Tsinghua from "../../assets/img/home/university/Tsinghua.jpg";
import ZJ from "../../assets/img/home/university/ZJ.jpg";
import Stanford from "../../assets/img/home/university/Stanford.jpg";
import Hopkins from "../../assets/img/home/university/Hopkins.jpg";

export default {
  name: "Homepage",
  data() {
    return {
      imgsrc: [doctor, medical],
      universities: [
        {
          src: Fudan,
          href: "https://www.fudan.edu.cn/"
        },
        {
          src: Tsinghua,
          href: "https://www.tsinghua.edu.cn/"
        },
        {
          src: ZJ,
          href: "http://www.zju.edu.cn/"
        },
        {
          src: Harvard,
          href: "https://www.harvard.edu/"
        },
        {
          src: Hopkins,
          href: "https://www.jhu.edu/"
        },
        {
          src: Stanford,
          href: "https://www.stanford.edu/"
        }
      ]
    };
  },
  methods: {
    jump(path) {
      this.$router.push({ path: path });
    },
    // 跳转外部链接
    goPage(url) {
      window.location.href = url;
    }
  }
};
</script>

<style scoped>
.main {
  background: #fffafa;
}

.contain {
  width: 100%;
  min-width: 60rem /* 1000/16 */;
  /* min-height: 62.5rem; */
  text-align: center;
}

.menu {
  margin-top: 0rem /* 0/16 */;
  width: 100%;
  min-width: 65rem /* 1000/16 */;
  height: 56.25rem /* 900/16 */;
  background: url("~assets/img/bg/home-bg.jpg") no-repeat center;
}

.btn-window {
  width: 24.8%;
  /* min-width: calc(25%-1rem); */
  height: 100%;
  float: left;
  background: #000;
  opacity: 0.8;
  border: 0.0625rem /* 1/16 */ solid white;
  color: white;
  cursor: pointer;
}

.icon {
  width: 13.75rem /* 220/16 */;
  height: 13.75rem /* 220/16 */;
  /* background: gray; */
  margin-left: auto;
  margin-right: auto;
  margin-top: 20rem /* 320/16 */;
}

.icon img {
  height: 12.5rem /* 200/16 */;
  width: 12.5rem /* 200/16 */;
  margin-left: 0.625rem /* 10/16 */;
}

.icon h3 {
  padding-left: 1.25rem /* 20/16 */;
  font-size: 1.25rem;
}

.btn-window:hover {
  opacity: 0.6;
}

.detail-window {
  background: url("~assets/img/bg/colorful-bg.jpg");
  background-size: cover;
  padding-bottom: 1.25rem /* 20/16 */;
}

.showdata {
  /* background: -webkit-linear-gradient(top, white, lightblue, white); */
  padding-top: 1.875rem /* 30/16 */;
  position: relative;
  min-width: 60rem /* 1000/16 */;
  height: 31.25rem /* 500/16 */;
  margin-left: auto;
  margin-right: auto;
  padding-top: 6.25rem /* 100/16 */;
}

.showdata img {
  float: right;
  position: absolute;
  right: 5rem;
  bottom: 6.25rem /* 100/16 */;
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

.showdata h3 {
  font-size: 1.5rem;
}

.company {
  width: 62.5rem /* 1000/16 */;
  height: 18.75rem /* 300/16 */;
  margin-left: auto;
  margin-right: auto;
}

.company img {
  width: 9.5rem /* 112/16 */;
  margin-left: -1.6rem;
}

.title {
  margin-bottom: 1.875rem /* 30/16 */;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 0.875rem /* 14/16 */;
  opacity: 0.75;
  line-height: 9.375rem /* 150/16 */;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
