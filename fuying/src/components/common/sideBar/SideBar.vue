<!--侧边栏-->

<template>
  <div id="side-bar" class="smalltext">{{ $t("public.sidebar") }}</div>
</template>

<script>
export default {
  name: "SideBar"
};
</script>

<style scoped>
#side-bar {
  /* background: white; */
  width: 1.25rem /* 20/16 */;
  height: 12.5rem /* 200/16 */;
  position: fixed;
  left: .625rem /* 10/16 */;
  top: 23.125rem /* 370/16 */;
}
</style>
