<template>
  <div class="windows">
    <el-row class="topRow">
      <el-input class="m-input" placeholder="全局搜索" v-model="filter[0].value"></el-input>
      <el-button type="primary" class="right-btn" @click="searchNum">搜索用户</el-button>
    </el-row>
    <el-row class="topRow">
        <el-input class="s-input" style="width: 130px" placeholder="订单编号" v-model="filter[1].value"></el-input>
        <el-input class="s-input" style="width: 120px" placeholder="用户名" v-model="filter[2].value"></el-input>
        <el-input class="s-input" style="width: 220px" placeholder="创建日期" v-model="filter[3].value"></el-input>
        <el-input class="s-input" style="width: 120px" placeholder="样品编号" v-model="filter[4].value"></el-input>
      <el-button class="right-btn" @click="clearSearch">清空搜索</el-button>
      <el-button type="primary" class="right-btn" @click="searchNum">搜索用户</el-button>
    </el-row>
    <el-table
      ref="multipleTable"
      :data="show_data"
      class="main-table"
      @sort-change="changeTableSort"
      :default-sort="{prop:'id',order:'ascending'}"
      tooltip-effect="dark">
      <el-table-column label="订单编号" prop="orderID" width="140" sortable="custom"></el-table-column>
      <el-table-column label="用户名" prop="username" width="130" sortable="custom"></el-table-column>
      <el-table-column label="创建日期" prop="createtime" width="230" sortable="custom"></el-table-column>
      <el-table-column label="样品编号" prop="sampleID" width="130" sortable="custom"></el-table-column>
      <el-table-column label="状态" prop="status" width="130"></el-table-column>
      <!-- <el-table-column label="状态" prop="status" width="130" sortable="custom"></el-table-column> -->
      <el-table-column label="操作" width="130">
        <template scope="scope">
          <el-button @click="handleEdit(scope.$index,scope.row)">
            {{scope.row.tips}}
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div style="text-align: center;margin-top: 30px;">
      <el-pagination
        background
        layout="prev,pager,next"
        :page-size="pagesize"
        :total="total"
        :current-page="currentPage"
        @current-change="handleCurrentChange"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
import GLOBAL from '@/common/const'
import Axios from 'axios'
// import qs from 'qs'

export default {
  name : "Manager",
  data(){
    return{
      // filter: [{value:"",field:"any"}],
      filter: [{value:"",field:"any"},{value:"",field:"orderID"},{value:"",field:"username"},{value:"",field:"createtime"},{value:"",field:"sampleID"}],
      pagesize:8,
      currentPage:1,
      total: 0,
      selected_data: [],
      show_data:[],
      pdfUrl: GLOBAL.urlHead2 + "get_pdf/",
      getAllUrl: GLOBAL.urlHead2 + "get_all_report/",
      sort:[{property:"orderID",direction:"ASC"}],
    }
  },

  mounted(){
    this.getAllData();
    // 数据样例
    // this.selected_data = [
    //     {orderID: "000001", username: "qjj", createtime: "2021-01-12 00:00:00", status: "new"},
    //     {orderID: "000002", username: "abb", createtime: "2021-01-12 00:00:01", status: "waiting"},
    //     {orderID: "teset123", username: "cdd", createtime: "2021-01-12 00:00:02", status: "finished", sampleID: "EXP000001", phone: "18818273750"},
    //     {orderID: "test123", username: "abb", createtime: "2021-01-12 00:00:03", status: "finished", sampleID: "EXP000002", phone: "18818273750"},
    // ]; 
  },

  methods:{
    // 获取报告数据的方法
    getAllData(){
      Axios.get(this.getAllUrl,
        {params:{
          id: localStorage.getItem("userPhone"),
          filter: JSON.stringify(this.filter),
          sort: JSON.stringify(this.sort),
        },},                   
        {headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      })
      .then((response) => {
        if(response.status === 200){
          let data = response.data;
          // console.log(data);
          this.selected_data = data;
          this.getShowData();
          this.total = this.selected_data.length;
          // console.log(this.total);
        }
      }).catch((error)=>{
        this.$message({
          type: 'warning',
          message: '后台出错',
        });
        console.log(error);
      });
    },

    // 处理当前页的展示数据
    getShowData(){
      console.log(this.selected_data);
      // 此处修正show_data值为展示值
      this.show_data = this.selected_data.slice((this.currentPage-1)*this.pagesize, this.currentPage*this.pagesize);
      this.show_data.forEach(element => {
        if(element.status === "new"){
          element.tips = "detail";
        }
        else if(element.status === "waiting"){
          element.tips = "edit";
        }
        else if(element.status === "finished"){
          element.tips = "report";
        }
      });
    },

    // 清空搜索条件
    clearSearch(){
      this.filter.forEach(element => {
        element.value = "";
      });
      this.getAllData();
    },

    // 根据已经填写的filter搜索
    searchNum(){
      console.log(this.filter);
      this.getAllData();
    },

    // 改变
    changeTableSort(column){
      console.log(column);
      var filterName = column.prop;
      var sortingType = column.order;
      // 通过后台处理排序
      if(sortingType == "descending"){
        sortingType = "DESC";
        console.log(filterName+"降序");
      }
      else{
        sortingType = "ASC"
        console.log(filterName+"升序");
      }
      this.sort[0].property = filterName;
      this.sort[0].direction = sortingType;
      this.getAllData();
      console.log(this.selected_data)
    },

    // 具体操作，根据不同status不同响应
    handleEdit(index,row){
      console.log(index,row);
      if(row.tips === "detail"){
        console.log("detail");
      }
      else if(row.tips === "edit"){
        this.$router.push({path: '/reportEdit'});
      }
      else if(row.tips === "report"){
        var url = this.pdfUrl+"?orderID="+row.orderID+"&phone="+row.phone;
        window.open(url);      }
    },

    // 换页
    handleCurrentChange(newPage){
      this.currentPage = newPage;
      this.getShowData();  
    },
  }
}
</script>

<style scoped>
  .windows{
    width: 80%;
    margin-top: 20px;
    min-width: 1000px;
    min-height: 700px;
    margin-left: auto;
    margin-right: auto;
  }
  .topRow{
    width: 100%;
    margin-left: 20%;
  }
  .m-input{
    width: 200px;
    padding-right: 10px;
  }
  .s-input{
    padding-right: 10px;
    padding-top: 10px;
  }
  .main-table{
    margin-top: 20px;
    margin-left: 20%;
  }
</style>