<!--简易icon-->

<template>
  <div id="icon" @click="goPage">
    <slot name="img"></slot>
    <slot name="text"></slot>
  </div>
</template>

<script>
export default {
  name: "Icon",
  props:{
    link: {
      type: String,
      required: true
    },
  },
  methods: {
    goPage() {
      window.location.href = this.link;
    },
  }
}
</script>

<style scoped>
  #icon{
    background: gray;
    width: 300px;
    height: 300px;
    cursor: pointer;
  }
</style>