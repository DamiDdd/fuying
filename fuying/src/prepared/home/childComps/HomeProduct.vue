<!--首页第二个页面，展示一些产品-->

<template>
  <div id="home-product">
    <div id="pre-product">
      <div id="product">
        <div id="product-text">
          <p class="smalltext-blue">{{ $t("home.content5") }}</p>
          <p class="title">{{ $t("home.title8") }}</p>
          <p class="smalltext">{{ $t("home.content6") }}</p>
          <p class="bigtext-blue">
            <span @click="productClick">{{ $t("home.detail") }} ></span
            ><span @click="buyClick">{{ $t("home.purchase") }} ></span>
          </p>
        </div>
      </div>
      <div id="pre-intro">
        <p class="bigtext">{{ $t("home.title9") }}</p>
        <p class="title">{{ $t("home.content7") }}</p>
        <p class="bigtext-blue bottom">{{ $t("home.title10") }}</p>
        <img src="~assets/img/common/arrow.png" @click="scrollScreen" />
      </div>
    </div>
    <div id="intro">
      <div id="intro-top">
        <div class="left">
          <p class="bigtext-blue">
            <span class="yellow sp1">50%</span>{{ $t("home.content8") }}
          </p>
          <home-pie></home-pie>
        </div>
        <div class="right">
          <p class="bigtext-blue">
            {{ $t("home.content9") }}<span class="yellow">98%</span
            >{{ $t("home.content10") }}
          </p>
          <icon-hexa-win></icon-hexa-win>
        </div>
      </div>
      <div id="intro-middle">
        <div class="left">
          <img src="~assets/img/home/transcription.png" />
        </div>
        <div class="right smalltext-blue">
          <p>{{ $t("home.content11") }}</p>
          <p>{{ $t("home.content12") }}</p>
          <p>{{ $t("home.content13") }}</p>
        </div>
      </div>
      <div id="intro-bottom">
        <div class="left">
          <p class="smalltext-blue">
            {{ $t("home.content14") }}
            <span class="yellow">{{ $t("home.content15") }}</span>
            {{ $t("home.content16") }}
          </p>
          <p class="content">{{ $t("home.content17") }}</p>
        </div>
        <div class="right">
          <img src="~assets/img/home/index5-p.png" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HomePie from "components/content/homePie/HomePie";
import IconHexaWin from "components/content/homeIcons/IconHexaWin";

export default {
  name: "HomeProduct",
  components: {
    HomePie,
    IconHexaWin
  },
  methods: {
    productClick() {
      this.$router.push("/products");
    },
    buyClick() {
      this.$router.push("/products");
    },
    scrollScreen() {
      window.scrollTo({
        top: 2500,
        left: 0,
        behavior: "smooth"
      });
    }
  }
};
</script>

<style scoped>
#home-product {
  width: var(--screen-width);
}

#pre-product {
  background: -webkit-linear-gradient(top, white, lightblue, white);
}

#product {
  background: url("~assets/img/home/product.png") no-repeat;
  background-position: 9.375rem /* 150/16 */ 0rem /* 0/16 */;
  height: var(--screen-height);
}

#product-text {
  width: 37.5rem /* 600/16 */;
  height: 18.75rem /* 300/16 */;
  position: relative;
  margin-left: 60%;
  padding-top: 10rem /* 160/16 */;
  text-align: center;
}

#product-text .title {
  color: var(--text-color);
}

#product-text .bigtext-blue span {
  margin-right: 1.875rem /* 30/16 */;
  margin-left: 1.25rem /* 20/16 */;
  cursor: pointer;
}

#pre-intro {
  width: var(--screen-width);
  height: var(--screen-height);
  text-align: center;
}

#pre-intro img {
  cursor: pointer;
}

#pre-intro .title {
  width: 56.25rem /* 900/16 */;
  line-height: 3.125rem /* 50/16 */;
  margin-left: auto;
  margin-right: auto;
}

#pre-intro .bottom {
  margin-top: 21.875rem /* 350/16 */;
}

#intro {
  width: var(--screen-width);
  height: 112.5rem /* 1800/16 */;
  /* background: -webkit-linear-gradient(top,white,lightblue,white); */
}

#intro div {
  overflow: hidden;
}

.left {
  float: left;
}

.right {
  float: right;
}

#intro-top {
  height: 40rem /* 640/16 */;
}

#intro-top .left {
  height: 52.5rem /* 840/16 */;
  width: 43.75rem /* 700/16 */;
  text-align: center;
}

#intro-top .left p {
  margin-left: 7.5rem /* 120/16 */;
}

#intro-top .right {
  height: 52.5rem /* 840/16 */;
  width: 43.75rem /* 700/16 */;
  padding-right: 6.25rem /* 100/16 */;
  text-align: center;
}

#intro-top #home-pie {
  margin-left: 20%;
  margin-top: -12.5rem /* 200/16 */;
}

#intro-middle {
  height: 16.25rem /* 260/16 */;
  width: 100%;
}

#intro-middle .left {
  height: 16.25rem /* 260/16 */;
  width: 62.5rem /* 1000/16 */;
}

#intro-middle .left img {
  height: 12.5rem /* 200/16 */;
  margin-left: 12%;
  margin-top: 1.875rem /* 30/16 */;
}

#intro-middle .right {
  margin-left: -12.5rem /* 200/16 */;
  height: 16.25rem /* 260/16 */;
  width: 40%;
  margin-top: 3.125rem /* 50/16 */;
}

#intro-bottom {
  height: 56.25rem /* 900/16 */;
}

#intro-bottom .left {
  height: 56.25rem /* 900/16 */;
  width: 43.75rem /* 700/16 */;
  text-indent: 2rem;
}

#intro-bottom .left p {
  width: 29.375rem /* 470/16 */;
  line-height: 1.875rem /* 30/16 */;
  margin-left: 30%;
  margin-top: 12.5rem /* 200/16 */;
}

#intro-bottom .right {
  height: 56.25rem /* 900/16 */;
  width: 43.75rem /* 700/16 */;
  margin-right: 7.5rem /* 120/16 */;
  /* margin-right: 14%; */
}

#intro-bottom .right img {
  margin-left: 5rem /* 80/16 */;
}

.yellow {
  color: #ffb658;
}
.sp1 {
  margin-left: 15%;
}
</style>
