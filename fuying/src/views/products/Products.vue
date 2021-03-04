<!--商品总览页面-->

<template>
  <div id="products">
    <img class="nav-bg" src="~assets/img/bg/products-bg.jpg" alt="/" />
    <cart-icon :iconStyle="cartIconStyle"></cart-icon>
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
    <div class="product-div">
      <div
        v-for="(item, index) in goodList"
        :key="index"
        @click="enterDetail(item.id)"
        class="item-div"
        style="cursor: pointer;"
      >
        <div class="text">
          {{ item.title }}
          <br />
          {{ item.desc }}
        </div>
      </div>
      <div class="item-div">
        <div class="text">
          敬请期待
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import ItemWindow from "components/common/mall/ItemWindow";
import CartIcon from "components/common/cart/CartIcon";
import Axios from "axios";
import GLOBAL from "@/common/const";

export default {
  name: "Products",
  components: {
    // ItemWindow,
    CartIcon
  },
  data() {
    return {
      cartIconStyle: {
        right: "94px",
        bottom: "200px",
        background: "#fff",
        "border-radius": "25px"
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
  min-width: 1000px;
  height: 200px;
}

#products {
  min-height: 700px;
}

.main-div {
  padding-left: 13%;
  padding-top: 2%;
  min-height: 700px;
}
.icon {
  width: 100%;
  min-width: 1000px;
  margin-left: 40px;
}

.product-div {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  min-width: 1000px;
  height: 700px;
  /* background: gray; */
}

.item-div {
  width: 33.2%;
  height: 100%;
  float: left;
  background: #000;
  opacity: 0.4;
  border: 1px solid white;
  /* color: white; */
}

.item-div:hover {
  opacity: 0.8;
}

.text {
  /* background: yellow; */
  color: white;
  margin-top: 500px;
  height: 200px;
}
</style>
