<template>
  <div id="products">
    <item-window v-for="(item,index) in goodsList" :key="index" :goods="item">
      {{item.title}}
    </item-window>
  </div>
</template>

<script>
import ItemWindow from "components/common/mall/ItemWindow"

export default {
  name: "Products",
  components:{
    ItemWindow,
  },
  data(){
    return{
      goodsList:[
        {
          id: "1",
          title:"aaa",
          des: "hhh",
        },
        {
          id: "2",
          title: "bbb",
          des: "hhh",
        }
      ],
    }
  },
  // props:{
  //   goodsList:{
  //     type: Array,
  //     default: []
  //   }
  // },
}
</script>

<style scoped>
  #products{
    min-height:500px;
  }
</style>