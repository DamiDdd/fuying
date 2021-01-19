<template>
  <div>Payment</div>
</template>

<script>
export default {
  name: 'Payment',
  data(){
    return{
      orderId:"",
    }
  },
  mounted(){
    this.orderId = this.$route.query.id;
    console.log(this.orderId);
  }
}
</script>

<style scoped>

</style>