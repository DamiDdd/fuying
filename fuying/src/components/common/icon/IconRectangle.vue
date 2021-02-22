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
  width: 300px;
  height: 300px;
  pointer-events: none;
}
#icon-rectangle img {
  cursor: pointer;
  pointer-events: all;
  margin-top: 40px;
}
</style>
