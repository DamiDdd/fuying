<!--退出组件-->

<template>
  <div>exiting...</div>
</template>

<script>
export default {
  name: "Exit",
  mounted() {
    // 删除本地phone标识
    localStorage.removeItem("userPhone");
    localStorage.removeItem("userEmail");
    localStorage.removeItem("userName");
    this.$store.state.isLogin = false;
    // 删除本地admin标识
    if (localStorage.getItem("admin") != null) {
      localStorage.removeItem("admin");
      this.$store.state.isAdmin = false;
    }
    // 自动返回首页
    this.$router.push("/home");
    this.$message({
      type: "success",
      message: this.$t("tips.exit")
    });
  }
};
</script>

<style scoped></style>
