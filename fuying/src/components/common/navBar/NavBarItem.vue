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
    computed: {
      // isActive() {
      //   return this.$route.path.indexOf(this.link) !== -1
      // },
      // activeStyle() {
      //   // 这里尝试抓取isActive，控制台报错，router相关
      //   console.log(this.$router);
      //   return this.isActive ? {'color' : 'red'} : {}
      //   // return this.isActive ? {'background' : '~assets/img/logo.png'} : {}
      // }
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