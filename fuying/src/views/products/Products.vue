<!--商品总览页面-->

<template>
  <div id="products">
    <div class="nav-bg"></div>
    <!-- <div class="main-div">
      <div
        class="icon"
        v-for="(item, index) in goodList"
        :key="index"
        @click="enterDetail(item.id)"
      >
        <item-window>
          <p slot="title">{{ item.title }}</p>
          <img :src="item.imgurl" slot="img" />
          <p slot="desc">{{ item.desc }}</p>
        </item-window>
      </div>
    </div> -->
    <div class="bg-div">
      <div class="product-div">
        <div
          v-for="(item, index) in goodList"
          :key="index"
          @click="enterDetail(item.id)"
          class="item-div"
          style="cursor: pointer;"
        >
          <div class="text">
            <p class="title" style="color: white; padding-top: 1rem;">
              {{ item.title }}
            </p>
            <p style="padding-top: 0.5rem; font-size: 1.2rem;">
              {{ item.desc }}
            </p>
          </div>
        </div>
        <div class="item-div third">
          <div class="text">
            <p class="title" style="color: white; padding-top: 1rem;">
              敬请期待
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import ItemWindow from "components/common/mall/ItemWindow";
import Axios from "axios";
import GLOBAL from "@/common/const";

export default {
  name: "Products",

  data() {
    return {
      cartIconStyle: {
        right: "5.875rem /* 94/16 */",
        bottom: "12.5rem /* 200/16 */",
        background: "#fff",
        "border-radius": "1.5625rem /* 25/16 */"
      },
      productUrl: GLOBAL.urlHead + "getProducts/",
      goodList: []
    };
  },
  mounted() {
    // 在这里通过URL获取后端的所有商品信息
    Axios.get(this.productUrl).then(response => {
      if (response.status === 200) {
        this.goodList = response.data["goodList"];
      } else {
        this.$message({
          type: "warning",
          message: this.$t("tips.servererror")
        });
      }
    });
  },
  methods: {
    // detail的跳转函数
    enterDetail(id) {
      this.$router.push({ path: "/detail", query: { goodId: id } });
    }
  }
};
</script>

<style scoped>
.nav-bg {
  width: 100%;
  min-width: 62.5rem /* 1000/16 */;
  height: 12.5rem /* 200/16 */;
  background: url("~assets/img/bg/item-bg.jpg");
  background-size: top cover;
}

#products {
  min-height: 43.75rem /* 700/16 */;
}

.main-div {
  padding-left: 13%;
  padding-top: 2%;
  min-height: 43.75rem /* 700/16 */;
}

.icon {
  width: 100%;
  min-width: 62.5rem /* 1000/16 */;
  margin-left: 2.5rem /* 40/16 */;
}

.bg-div {
  width: 100%;
  min-height: 45rem /* 720/16 */;
  background: url("~assets/img/bg/colorful-bg.jpg");
  background-size: cover;
}

.product-div {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  min-width: 62.5rem /* 1000/16 */;
  height: 43.75rem /* 700/16 */;
}

.item-div {
  width: 33%;
  height: 100%;
  float: left;
  /* background: #000; */
  opacity: 1;
  border: 0.0625rem /* 1/16 */ solid white;
  /* color: white; */
}

.item-div:nth-child(1) {
  background: url("~assets/img/bg/health-bg.jpg") center bottom;
  background-size: cover;
}

.item-div:nth-child(2) {
  background: url("~assets/img/bg/cancer-bg.jpg");
  background-size: cover;
}

.third {
  background: url("~assets/img/bg/intro-bg.jpg");
  background-size: cover;
}

.item-div:hover {
  opacity: 0.8;
}

.text {
  background: black;
  color: white;
  margin-top: 31.25rem /* 500/16 */;
  height: 12.5rem /* 200/16 */;
  opacity: 0.6;
  padding-left: 1.25rem /* 20/16 */;
}

.text:hover {
  opacity: 1;
}
</style>
