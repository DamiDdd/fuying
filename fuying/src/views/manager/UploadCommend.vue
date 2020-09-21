<!--管理员用户评价页面-->

<template>
  <div id="upload-commend">
    <div>
      <input type="text" placeholder="请输入用户编号" v-model="user">
      <button @click="searchUser">查询</button>
    </div>
    <div>
      <div>该用户的健康得分为：{{scoreSum}}</div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import GLOBAL from '@/common/const'


export default {
  name: "UploadCommend",
  data(){
    return{
      user: "", // for test 080578
      findUrl: GLOBAL.urlHead + "getevaluation?exp=",
      mainData: [],
      scoreSum: 500,
    }
  },
  methods:{
    // 查找这个用户的相关数据
    searchUser(){
      let url = this.findUrl +this.user;
      if(this.user.length === 0){
          this.$message({
						type: 'warning',
						message: '请输入用户编号',
					});
      }
      else{
        Axios.get(url).then((response) => {
          console.log(response);
          if(response.status == 200){
            // 此处重置评分
            this.scoreSum = 500;
            let data = response.data;
            this.solveData(data);
          }
        }).catch((error) => {
          console.log(error);
          this.$message({
						type: 'warning',
						message: '未查询到相应用户',
          });
          this.scoreSum = 500;
        })
      }
    },

    // 处理数据
    solveData(data){
      console.log(data);
      // 这里为了功能划分清晰，采用了读两遍的方式，后续提升速度可以合并
      data.forEach(element => {
        let table = element['sum_table'];
        let length = element['sum_table'].length;
        this.scoreSum += parseInt(table[length-1][2]);
      });
      // data.forEach(element => {
      //   let 
      // })
    }
  }
}
</script>

<style>

</style>