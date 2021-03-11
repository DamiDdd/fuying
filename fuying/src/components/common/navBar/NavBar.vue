<!--顶部导航栏-->

<template>
  <div id="nav-bar">
    <div class="nav-logo"><slot name="logo">logo</slot></div>
    <div class="nav-center"><slot name="center">choices</slot></div>
    <div class="nav-right"><slot name="right">user</slot></div>
  </div>
</template>

<script>
export default {
  name: "NavBar"
};
</script>

<style scoped>
#nav-bar {
  height: 4.375rem; /* 70/16 */
  /* position: relative; */
  position: fixed;
  z-index: 10;
  display: flex;
  width: var(--screen-width);
  min-width: 50rem /* 800/16 */;
  line-height: 2.75rem /* 44/16 */;
  text-align: center;
  overflow: hidden;
  background: #222222;
  opacity: 0.5;
}

#nav-bar:hover {
  opacity: 0.8;
}

.nav-logo {
  width: 6rem;
}

.nav-logo img {
  /* width: 1.5rem /* 24/16 */
  height: 2.8125rem /* 45/16 */;
  margin-top: .3125rem /* 5/16 */;
  margin-left: 1.25rem /* 20/16 */;
  vertical-align: middle;
}

.nav-center {
  flex: 1;
  margin-left: 6rem;
}

.nav-right {
  width: 7.5rem /* 120/16 */;
  text-align: left;
}
</style>
