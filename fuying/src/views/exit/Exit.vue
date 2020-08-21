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
  }
}
</script>

<style scoped>

</style>