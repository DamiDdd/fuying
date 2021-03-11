<!--主页页脚，相关链接未给出-->

<template>
  <foot-bar>
    <h3 class="footer-tip">iproteome</h3>
    <div class="footer-icon">
      <img src="~assets/img/common/phone.png" />
      <img src="~assets/img/common/message.png" />
      <img src="~assets/img/common/wechat.png" />
      <img src="~assets/img/common/place.png" />
    </div>
  </foot-bar>
</template>

<script>
import FootBar from "common/footer/FootBar";

export default {
  name: "MainFooter",
  components: {
    FootBar
  }
};
</script>

<style scoped>
.footer-tip {
  font-size: 36px;
  padding-top: 200px;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
.footer-icon img {
  margin: 0 20px 0 20px;
  cursor: pointer;
}
.footer-author {
  font-size: 13px;
  line-height: 13px;
  margin-top: 50px;
}
</style>
