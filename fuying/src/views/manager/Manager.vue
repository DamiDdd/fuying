<template>
  <div class="windows">
    <el-row class="topRow">
      <el-input class="short-input" v-model="filter[0].value"></el-input>
      <el-button type="primary" class="right-btn" @click="searchNum">搜索用户</el-button>
    </el-row>
    <el-table
      ref="multipleTable"
      :data="show_data"
      class="main-table"
      @sort-change="changeTableSort"
      :default-sort="{prop:'id',order:'ascending'}"
      tooltip-effect="dark">
      <el-table-column label="订单编号" prop="orderID" width="130" sortable="custom"></el-table-column>
      <el-table-column label="用户名" prop="username" width="130" sortable="custom"></el-table-column>
      <el-table-column label="创建日期" prop="createtime" width="230" sortable="custom"></el-table-column>
      <el-table-column label="订单编号" prop="sampleID" width="130" sortable="custom"></el-table-column>
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
      filter: [{value:"",field:"any"}],
      pagesize:8,
      currentPage:1,
      total: 0,
      selected_data: [],
      show_data:[],
      pdfUrl: GLOBAL.urlHead2 + "get_pdf/?",
      getAllUrl: GLOBAL.urlHead2 + "get_all_report/",
      sort:[{property:"orderID",direction:"ASC"}],
    }
  },

  mounted(){
    this.getAllData();
    // this.selected_data = [
    //     {orderID: "000001", username: "qjj", createtime: "2021-01-12 00:00:00", status: "new"},
    //     {orderID: "000002", username: "abb", createtime: "2021-01-12 00:00:01", status: "waiting"},
    //     {orderID: "teset123", username: "cdd", createtime: "2021-01-12 00:00:02", status: "finished", sampleID: "EXP000001", phone: "18818273750"},
    //     {orderID: "test123", username: "abb", createtime: "2021-01-12 00:00:03", status: "finished", sampleID: "EXP000002", phone: "18818273750"},
    // ]; 
  },

  methods:{
    getAllData(){
      // let params = new URLSearchParams();
      // params.append("id",localStorage.getItem("userPhone"));
      // params.append("filter",filter);
      // params.append("sort",sort);
      // console.log(params);
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
          console.log(data);
          this.selected_data = data;
          this.getShowData();
          this.total = this.selected_data.length;
          console.log(this.total);
        }
      }).catch((error)=>{
        this.$message({
          type: 'warning',
          message: '后台出错',
        });
        console.log(error);
      });
    },
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
    searchNum(){
      console.log(this.filter);
      this.getAllData();
    },
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
    handleEdit(index,row){
      console.log(index,row);
      if(row.tips === "detail"){
        console.log("detail");
      }
      else if(row.tips === "edit"){
        this.$router.push({path: '/reportEdit'});
      }
      else if(row.tips === "report"){
        var url = this.pdfUrl+"orderID="+row.orderID+"&phone="+row.phone;
        window.open(url);      }
    },
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
  .short-input{
    width: 200px;
    padding-right: 10px;
  }
  .main-table{
    margin-top: 20px;
    margin-left: 20%;
  }
</style>