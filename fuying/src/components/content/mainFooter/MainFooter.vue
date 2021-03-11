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
  font-size: 2.25rem /* 36/16 */;
  padding-top: 12.5rem /* 200/16 */;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
.footer-icon img {
  margin: 0 1.25rem /* 20/16 */ 0 1.25rem /* 20/16 */;
  cursor: pointer;
}
.footer-author {
  font-size: .8125rem /* 13/16 */;
  line-height: .8125rem /* 13/16 */;
  margin-top: 3.125rem /* 50/16 */;
}
</style>
