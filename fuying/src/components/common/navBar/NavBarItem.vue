<!--导航栏单个菜单-->

<template>
  <div id="nav-bar-item" @click="itemClick" @mouseenter="changeFocus" @mouseleave="removeFocus">
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
    // check(){
    //   if(this.$router.path.indexOf(this.link) !== -1){
    //     console(this.link);
    //   }
    // },
    itemClick() {
      this.$router.replace(this.link)
    },
    changeFocus(e) {
      e.currentTarget.className = 'focus';
    },
    removeFocus(e) {
      e.currentTarget.className = '';
    }
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

  .focus{
    background: url("~assets/img/common/topbar-bt-bg.png") no-repeat bottom center;
  }
</style>