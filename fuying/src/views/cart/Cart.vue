<template>
  <div id="cart"></div>
</template>

<script>
export default {
  name: 'Cart',
  data(){
    return{
      phone: localStorage.getItem("userPhone")
    }
  }
}
</script>

<style scoped>

</style>