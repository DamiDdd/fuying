<!--首页最后一个页面，广告宣传页-->

<template>
  <div id="home-ad">
    <div class="ad-map">
      <p class="title">{{ $t("home.title1") }}</p>
      <p class="content">{{ $t("home.content1") }}</p>
      <p class="content">{{ $t("home.content2") }}</p>
      <p class="content">{{ $t("home.content3") }}</p>
      <img src="~assets/img/home/map.png" />
    </div>
    <div class="ad-company">
      <p class="title">{{ $t("home.title2") }}</p>
      <div id="university">
        <img
          src="~assets/img/home/university/Harvard.png"
          @click="goPage('https://www.harvard.edu/')"
        />
        <img
          src="~assets/img/home/university/Johns Hopkins.png"
          @click="goPage('https://www.jhu.edu/')"
        />
        <img
          src="~assets/img/home/university/Baylor.png"
          @click="goPage('https://www.bcm.edu/')"
        />
        <img
          src="~assets/img/home/university/Mayo.png"
          @click="goPage('https://mandarin.mayoclinic.org/')"
        />
        <img
          src="~assets/img/home/university/Stanford.png"
          @click="goPage('https://www.stanford.edu/')"
        />
        <img
          src="~assets/img/home/university/Tsinghua.png"
          @click="goPage('https://www.tsinghua.edu.cn/')"
        />
        <img
          src="~assets/img/home/university/Fudan.png"
          @click="goPage('https://www.fudan.edu.cn/')"
        />
        <img
          src="~assets/img/home/university/Fudan-ZL.png"
          @click="goPage('https://www.shca.org.cn/')"
        />
        <img
          src="~assets/img/home/university/Zhejiang.png"
          @click="goPage('http://www.zy91.com/index/index.jhtml')"
        />
        <img
          src="~assets/img/home/university/ZhongShan.png"
          @click="goPage('http://www.zs-hospital.sh.cn/')"
        />
        <!-- <img src="~assets/img/home/university.png"> -->
      </div>
      <div class="right-text">
        <p class="title">{{ $t("home.promise") }}</p>
        <button @click="buyClick">Try it now</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeAd",
  methods: {
    // 跳转商城
    buyClick() {
      this.$router.push("/products");
    },
    // 跳转外部链接
    goPage(url) {
      window.location.href = url;
    }
  }
};
</script>

<style scoped>
.ad-map,
.ad-company {
  width: var(--screen-width);
  text-align: center;
}
.ad-company {
  height: 1000px;
  background: url("~assets/img/bg/doctor.png") no-repeat bottom left;
}
#university {
  height: 380px;
  width: 620px;
  margin-left: auto;
  margin-right: auto;
}
#university img {
  cursor: pointer;
}
.ad-map .title {
  padding-bottom: 30px;
}
.ad-map .content {
  text-align: left;
  margin-left: 35%;
  /* margin-left: 750px; */
}
.ad-map img,
.ad-company img {
  padding-top: 20px;
}
.right-text {
  width: 760px;
  /* margin-left: 700px; */
  margin-left: 30%;
  margin-top: var(--div-bottom);
  line-height: 50px;
}
button {
  background-color: #ffce6b;
  border: none;
  color: #6b6b6b;
  padding: 15px 50px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 24px;
  font-weight: bold;
  cursor: pointer;
  border-radius: 15px;
  outline: none;
}
</style>
