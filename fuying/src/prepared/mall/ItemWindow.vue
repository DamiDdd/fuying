<!--服务总览页view-->

<template>
  <div id="item-window">
    <div
      id="i-div"
      class="unfocus"
      @mouseenter="changeFocus"
      @mouseleave="removeFocus"
    >
      <div class="img"><slot name="img"></slot></div>
      <!-- <div class="img"><img src="~assets/img/bg/bgtemp3.jpg" /></div> -->
      <div class="title"><slot name="title"></slot></div>
      <div class="desc">
        <slot name="desc"></slot><a class="text">->点击了解详情</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ItemWindow",
  methods: {
    changeFocus(e) {
      e.currentTarget.className = "focus";
    },
    removeFocus(e) {
      e.currentTarget.className = "unfocus";
    }
  }
};
</script>

<style scoped>
#item-window {
  margin-bottom: 1%;
}
#i-div {
  width: 80%;
  min-width: 62.5rem /* 1000/16 */;
  height: 13.75rem /* 220/16 */;
  display: flex;
  overflow: hidden;
  background: url("~assets/img/bg/item-bg.jpg") no-repeat;
  background-size: 100% 100%;
  cursor: pointer;
}

.img img {
  height: 10rem /* 160/16 */;
  width: 18.75rem /* 300/16 */;
  margin-top: 10%;
}
.title {
  margin-left: 1.25rem /* 20/16 */;
  width: 62.5rem /* 1000/16 */;
  height: 5rem /* 80/16 */;
  font-size: 2.25rem /* 36/16 */;
}
.desc {
  margin-left: 20rem /* 320/16 */;
  margin-top: 6.25rem /* 100/16 */;
  height: 6.25rem /* 100/16 */;
  width: 62.5rem /* 1000/16 */;
  position: absolute;
  font-size: 1.25rem /* 20/16 */;
  font-weight: 550;
}
.focus {
  border: 0.0625rem /* 1/16 */ solid var(--theme-color);
  border-radius: 0.9375rem /* 15/16 */;
}
.unfocus {
  border: 0.0625rem /* 1/16 */ solid var(--theme-color);
  border-radius: 0.9375rem /* 15/16 */;
}

.text {
  text-decoration: underline;
}

.text:hover {
  color: red;
}
</style>
