<template>
  <div id="news">
    <div class="nav-bg"></div>
    <div class="bg">
      <div class="main">
        <div class="main2">
          <el-row>
            <el-col
              :span="6"
              v-for="(o, index) in news"
              :key="index"
              :offset="index % 3 == 0 ? 2 : 1"
              style="padding-top: 1.625rem; cursor: pointer;"
            >
              <el-card :body-style="{ padding: '0rem' }">
                <img :src="o.img" class="image" @click="showNews(o.url)" />
                <div
                  style="height: 6rem; padding: .875rem /* 14/16 */; "
                  @click="showNews(o.url)"
                >
                  <span style="font-size: 1.2rem;">{{ o.title }}</span>
                  <div class="bottom clearfix">
                    <time class="time">{{ o.date }}</time>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </div>
        <div class="pagination">
          <el-pagination
            :page-size="6"
            layout="prev, pager, next"
            :total="total"
            @current-change="handleCurrentChange"
            hide-on-single-page
          >
          </el-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import news1 from "../../assets/img/news/news1.png";
// import news2 from "../../assets/img/news/news2.png";
import Axios from "axios";
import GLOBAL from "@/common/const";

export default {
  name: "News",
  data() {
    return {
      newsUrl: GLOBAL.urlHead + "getNews/?page=",
      news: [
        // {
        //   title: "Nature Medicine|深度纵向分析揭示衰老标志物和衰老类型",
        //   img: news1,
        //   date: "2021/3/19",
        //   url: "https://mp.weixin.qq.com/s/NMYSQFMaZa9s1QhhL-Whmg"
        // },
        // {
        //   title: "Nature Communications|乳腺癌定量蛋白质组和蛋白质基因组图谱",
        //   img: news2,
        //   date: "2021/3/19",
        //   url: "https://mp.weixin.qq.com/s/VszRZiI01Z7e0LUVjNiF8g"
        // }
      ],
      total: 20
    };
  },
  mounted() {
    this.getNews(1);
  },
  methods: {
    showNews(url) {
      window.location.href = url;
    },
    handleCurrentChange(val) {
      console.log(val);
      console.log(`当前页: ${val}`);
      this.getNews(val);
    },
    getNews(page) {
      let url = this.newsUrl + page;
      Axios.get(url).then(response => {
        if (response.status === 200) {
          this.news = response.data["news_list"];
          this.total = response.data["count"];
          console.log(this.news);
        } else {
          this.$message({
            type: "warning",
            message: this.$t("tips.servererror")
          });
        }
      });
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
  min-height: 60rem;
  /* background: gray; */
}

.main2 {
  min-height: 50rem;
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
  width: 27rem /* 400/16 */;
  height: 13.25rem;
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

.pagination {
  width: 50rem;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}
</style>
