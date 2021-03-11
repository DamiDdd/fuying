<template>
  <div id="news">
    <img class="nav-bg" src="~assets/img/bg/news-bg.jpg" alt="/" />
    <div class="bg">
      <div class="main">
        <el-row>
          <el-col
            :span="6"
            v-for="(o, index) in news"
            :key="o"
            :offset="index % 3 == 0 ? 2 : 1"
            style="padding-bottom: 10px"
          >
            <el-card :body-style="{ padding: '0px' }">
              <img :src="o.img" class="image" />
              <div style="padding: 14px;">
                <span>{{ o.title }}</span>
                <div class="bottom clearfix">
                  <time class="time">{{ currentDate }}</time>
                  <el-button type="text" class="button" @click="showNews(index)"
                    >操作按钮</el-button
                  >
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
import temp1 from "../../assets/img/bg/intro-bg.jpg";
import temp2 from "../../assets/img/bg/news-bg.jpg";

export default {
  name: "News",
  data() {
    return {
      currentDate: new Date(),
      news: [
        { title: "基因", img: temp1 },
        { title: "基因", img: temp2 },
        { title: "科学", img: temp1 },
        { title: "科学", img: temp2 },
        { title: "imean", img: temp2 },
        { title: "imean", img: temp1 }
      ]
    };
  },
  methods: {
    showNews(index) {
      console.log(index);
      this.$router.push("/newsDetail");
    }
  }
};
</script>

<style scoped>
#news {
  min-height: 500px;
}

.nav-bg {
  width: 100%;
  min-width: 1200px;
  height: 200px;
}

.bg {
  background: -webkit-linear-gradient(top, white, lightblue, white);
}

.main {
  width: 70%;
  min-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  min-height: 800px;
  /* background: gray; */
}

.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 400px;
  height: 300px;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>
