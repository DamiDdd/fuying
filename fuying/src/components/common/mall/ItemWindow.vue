<!--服务总览页view-->

<template>
  <div id="item-window">
    <div
      id="i-div"
      class="unfocus"
      @mouseenter="changeFocus"
      @mouseleave="removeFocus"
    >
      <div class="title"><slot name="title"></slot></div>
      <div class="img"><slot name="img"></slot></div>
      <div class="desc"><slot name="desc"></slot></div>
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
.title {
  margin-left: 20px;
  width: 14%;
  font-size: 36px;
  line-height: 50px;
}
.img img {
  height: 160px;
  max-width: 180px;
  margin-top: 10%;
}
.desc {
  height: 50%;
  width: 50%;
  margin-left: 13%;
  margin-top: 3%;
  font-size: 20px;
  font-weight: 550;
}
.focus {
  border: 2px solid var(--theme-color);
  border-radius: 15px;
}
.unfocus {
  border: 1px solid white;
  border-radius: 15px;
}
</style>
