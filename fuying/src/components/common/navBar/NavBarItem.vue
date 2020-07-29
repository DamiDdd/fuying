<template>
  <div id="nav-bar-item" @click="itemClick">
    <slot name="text"></slot>
  </div>
</template>

<script>
export default {
  name: "NavBarItem",
  props:{
    link: {
      type: String,
      required: true
    },
  },
  methods: {
    itemClick() {
      this.$router.replace(this.link)
    },
  }
}
</script>

<style scoped>
  #nav-bar-item{
    flex: 1;
    font-size: 20px;
    margin-top: 3px;
    color: #333;
    float: left;
    min-width: 90px;
    cursor: pointer;
  }
</style>