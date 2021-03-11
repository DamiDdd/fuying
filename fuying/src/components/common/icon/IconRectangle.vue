<!--六边形icon-->

<template>
  <div id="icon-rectangle" @click="iconClick">
    <slot name="img"></slot>
    <slot name="text"></slot>
  </div>
</template>

<script>
export default {
  name: "IconRectangle",
  props: {
    link: {
      type: String,
      required: true
    }
  },
  methods: {
    iconClick() {
      this.$router.replace(this.link);
    }
  }
};
</script>

<style scoped>
#icon-rectangle {
  background: url("~assets/img/common/rectangle-withshadow.png") no-repeat;
  width: 18.75rem /* 300/16 */;
  height: 18.75rem /* 300/16 */;
  pointer-events: none;
}
#icon-rectangle img {
  cursor: pointer;
  pointer-events: all;
  margin-top: 2.5rem /* 40/16 */;
}
</style>
