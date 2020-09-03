<template>
  <div class="cartcontrol">
    <div class="title">{{item.title}}</div>
    <div class="text">{{item.desc}}</div>
    <div class="type" v-for="(i,index) in item.type" :key="index" @click="typeChoose(index)">{{i.name}}</div>
    <div class="tip">
      {{item.type[this.index].tip}}
    </div>    
    <div class="price">
      {{item.type[this.index].price}}
    </div>
    <div class="reduce" @click="deleteCart">-</div>
    <div class="num">{{item.count}}</div>
    <div class="add" @click="addCart">+</div>
  </div>
</template>

<script>
export default {
  name:"GoodView",
  data(){
    return{
      index: 0
    }
  },
  props:{
    item:{
      type: Object,
      //  默认赋值count为0
      default(){
        return{
          count: 0,
        }
      }
    }
  },
  computed:{
    itemnum(){
      return this.item.count > 0;
    },
  },
  methods:{
    addCart(){
      this.item.count++;
    },
    deleteCart(){
      if(this.item.count>0)
        this.item.count--;
    },
    typeChoose(index){
      console.log(index);
      this.index = index;
    },
  }
}
</script>

<style scoped>
  .reduce, .add, .type{
    cursor: pointer;
  }
</style>