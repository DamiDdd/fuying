<template>
  <div id="news">
    <div class="nav-bg"></div>
    <div class="bg">
      <div class="main">
        <el-row>
          <el-col
            :span="6"
            v-for="(o, index) in news"
            :key="o"
            :offset="index % 3 == 0 ? 2 : 1"
            style="padding-top: 1.625rem;"
          >
            <el-card :body-style="{ padding: '0rem /* 0/16 */' }">
              <img :src="o.img" class="image" />
              <div style="height: 6rem; padding: .875rem /* 14/16 */;">
                <span>{{ o.title }}</span>
                <div class="bottom clearfix">
                  <time class="time">{{ currentDate }}</time>
                  <el-button type="text" class="button" @click="showNews(o.url)"
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
import news1 from "../../assets/img/news/news1.png";
import news2 from "../../assets/img/news/news2.png";

export default {
  name: "News",
  data() {
    return {
      currentDate: new Date(),
      news: [
        {
          title: "Nature Medicine|深度纵向分析揭示衰老标志物和衰老类型",
          img: news1,
          url: "https://mp.weixin.qq.com/s/NMYSQFMaZa9s1QhhL-Whmg"
        },
        {
          title: "Nature Communications|乳腺癌定量蛋白质组和蛋白质基因组图谱",
          img: news2,
          url: "https://mp.weixin.qq.com/s/VszRZiI01Z7e0LUVjNiF8g"
        }
      ]
    };
  },
  methods: {
    showNews(url) {
      window.location.href = url;
    }
  }
};
</script>

<style scoped>
#news {
  min-height: 31.25rem /* 500/16 */;
}

.nav-bg {
  width: 100%;
  min-width: 75rem /* 1200/16 */;
  height: 12.5rem /* 200/16 */;
  background: url("~assets/img/bg/news-bg.png");
  background-size: top cover;
}

.bg {
  background: -webkit-linear-gradient(top, white, lightblue, white);
}

.main {
  width: 70%;
  min-width: 75rem /* 1200/16 */;
  margin-left: auto;
  margin-right: auto;
  min-height: 50rem /* 800/16 */;
  /* background: gray; */
}

.time {
  font-size: 0.8125rem /* 13/16 */;
  color: #999;
}

.bottom {
  margin-top: 0.8125rem /* 13/16 */;
  line-height: 0.75rem /* 12/16 */;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 25rem /* 400/16 */;
  height: 20.75rem /* 300/16 */;
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
