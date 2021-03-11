<!--导航栏单个菜单-->

<template>
  <div
    id="nav-bar-item"
    @click="itemClick"
    @mouseenter="changeFocus"
    @mouseleave="removeFocus"
  >
    <slot name="text"></slot>
  </div>
</template>

<script>
export default {
  name: "NavBarItem",
  props: {
    link: {
      type: String,
      required: true
    }
  },
  methods: {
    itemClick() {
      this.$router.push(this.link);
    },
    changeFocus(e) {
      e.currentTarget.className = "focus";
    },
    removeFocus(e) {
      e.currentTarget.className = "";
    }
  }
};
</script>

<style scoped>
#nav-bar-item {
  flex: 1;
  font-size: 1.0625rem /* 17/16 */;
  margin-top: .5rem /* 8/16 */;
  color: white;
  float: left;
  min-width: 5.625rem /* 90/16 */;
  cursor: pointer;
}

/* .focus {
  /* background: url("~assets/img/common/topbar-bt-bg.png") no-repeat bottom center; */
  /* font-weight: bold; */
  /* color: wheat; */
/* }  */
</style>
