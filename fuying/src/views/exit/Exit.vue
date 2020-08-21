<template>
  <div></div>
</template>

<script>
export default {
  name: "Exit",
  mounted(){
    localStorage.removeItem("userPhone");
    this.$store.state.isLogin = true;
    console.log(localStorage);
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