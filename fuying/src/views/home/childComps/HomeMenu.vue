<!--首页第三个页面，提供服务菜单-->

<template>
  <div id="home-menu">
    <p class="title">{{ $t("home.title7") }}</p>
    <p class="content">{{ $t("home.content4") }}</p>
    <div class="menu-lists">
      <icon-rectangle link="/intro"
        ><img src="~assets/img/common/detect.png" slot="img" />
        <p class="content" slot="text">{{ $t("home.btn1") }}</p></icon-rectangle
      >
      <icon-rectangle link="/report"
        ><img src="~assets/img/common/report.png" slot="img" />
        <p class="content" slot="text">{{ $t("home.btn2") }}</p></icon-rectangle
      >
      <icon-rectangle link="/ask"
        ><img src="~assets/img/common/earphone.png" slot="img" />
        <p class="content" slot="text">{{ $t("home.btn3") }}</p></icon-rectangle
      >
    </div>
    <div class="menu-lists">
      <icon-rectangle link="/cart"
        ><img src="~assets/img/common/cart.png" slot="img" />
        <p class="content" slot="text">{{ $t("home.btn4") }}</p></icon-rectangle
      >
      <icon-rectangle link="/products"
        ><img src="~assets/img/common/file.png" slot="img" />
        <p class="content" slot="text">{{ $t("home.btn5") }}</p></icon-rectangle
      >
      <icon-rectangle link="/intro"
        ><img src="~assets/img/common/find.png" slot="img" />
        <p class="content" slot="text">{{ $t("home.btn6") }}</p></icon-rectangle
      >
    </div>
  </div>
</template>

<script>
import IconRectangle from "common/icon/IconRectangle";

export default {
  name: "HomeMenu",
  components: {
    IconRectangle
  }
};
</script>

<style scoped>
#home-menu {
  width: var(--screen-width);
  text-align: center;
  padding-bottom: var(--div-bottom);
}
.content {
  padding-bottom: var(--div-bottom);
}
.menu-lists {
  width: 850px;
  height: 300px;
  display: flex;
  margin-left: auto;
  margin-right: auto;
}
</style>
