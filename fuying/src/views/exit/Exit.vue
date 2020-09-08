<template>
  <div></div>
</template>

<script>
export default {
  name: "Exit",
  mounted(){
    localStorage.removeItem("userPhone");
    this.$store.state.isLogin = false;
    // console.log(localStorage);
    // console.log(this.$store.state.isLogin);
    this.$router.push('/home');
    this.$message({
			type: 'success',
			message: '您已退出登录'
		});
  }
}
</script>

<style scoped>

</style>