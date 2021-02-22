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
  background-position: 150px 0px;
  height: var(--screen-height);
}

#product-text {
  width: 600px;
  height: 300px;
  position: relative;
  margin-left: 60%;
  padding-top: 160px;
  text-align: center;
}

#product-text .title {
  color: var(--text-color);
}

#product-text .bigtext-blue span {
  margin-right: 30px;
  margin-left: 20px;
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
  width: 900px;
  line-height: 50px;
  margin-left: auto;
  margin-right: auto;
}

#pre-intro .bottom {
  margin-top: 350px;
}

#intro {
  width: var(--screen-width);
  height: 1800px;
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
  height: 640px;
}

#intro-top .left {
  height: 840px;
  width: 700px;
  /* margin-left: 100px; */
  text-align: center;
}

#intro-top .left p {
  margin-left: 120px;
}

#intro-top .right {
  height: 840px;
  width: 700px;
  padding-right: 100px;
  text-align: center;
}

#intro-top #home-pie {
  margin-left: 20%;
  margin-top: -200px;
}

#intro-middle {
  height: 260px;
  width: 100%;
}

#intro-middle .left {
  height: 260px;
  width: 1000px;
}

#intro-middle .left img {
  height: 200px;
  margin-left: 12%;
  margin-top: 30px;
}

#intro-middle .right {
  margin-left: -200px;
  height: 260px;
  width: 40%;
  margin-top: 50px;
}

#intro-bottom {
  height: 900px;
}

#intro-bottom .left {
  height: 900px;
  width: 700px;
  text-indent: 2rem;
}

#intro-bottom .left p {
  width: 470px;
  line-height: 30px;
  /* margin-left: 300px; */
  margin-left: 30%;
  margin-top: 200px;
}

#intro-bottom .right {
  height: 900px;
  width: 700px;
  margin-right: 120px;
  /* margin-right: 14%; */
}

#intro-bottom .right img {
  margin-left: 80px;
}

.yellow {
  color: #ffb658;
}
.sp1 {
  margin-left: 15%;
}
</style>
