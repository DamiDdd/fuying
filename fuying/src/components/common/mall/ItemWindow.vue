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
  min-width: 1000px;
  height: 220px;
  display: flex;
  overflow: hidden;
  background: url("~assets/img/bg/item-bg.jpg") no-repeat;
  background-size: 100% 100%;
  cursor: pointer;
}

.img img {
  height: 160px;
  width: 300px;
  margin-top: 10%;
}
.title {
  margin-left: 20px;
  width: 1000px;
  height: 80px;
  font-size: 36px;
}
.desc {
  margin-left: 320px;
  margin-top: 100px;
  height: 100px;
  width: 1000px;
  position: absolute;
  font-size: 20px;
  font-weight: 550;
}
.focus {
  border: 1px solid var(--theme-color);
  border-radius: 15px;
}
.unfocus {
  border: 1px solid var(--theme-color);
  border-radius: 15px;
}

.text {
  text-decoration: underline;
}

.text:hover {
  color: red;
}
</style>
