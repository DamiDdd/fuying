<template>
  <div class="main">
    <h2 class="title">{{ $t("payment.title") }}</h2>
    <el-table :data="orderList" class="data_table">
      <!-- <el-table-column prop="img" label="图" width="182"></el-table-column> -->
      <el-table-column
        prop="title"
        :label="$t('payment.service')"
        width="300"
      ></el-table-column>
      <el-table-column
        prop="name"
        :label="$t('payment.receiver')"
        width="200"
      ></el-table-column>
      <el-table-column
        prop="num"
        :label="$t('payment.num')"
        width="200"
      ></el-table-column>
      <el-table-column
        prop="total"
        :label="$t('payment.total')"
        width="200"
      ></el-table-column>
    </el-table>
    <div class="scan">
      <h2 class="bigtext">
        {{ $t("payment.paytips") }}<span class="bigtext-blue">¥{{ total }}</span
        >{{ $t("payment.yuan") }}
      </h2>
      <img :src="scancode" />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import GLOBAL from "@/common/const";
import unavailable from "@/assets/img/common/unavailable.png";

export default {
  name: "Payment",
  data() {
    return {
      paymentID: "",
      phone: localStorage.getItem("userPhone"),
      orderList: [],
      total: 200,
      scancode: "",
      count: 0,
      status: "",
      timeMax: 10, // 最大响应时长-分钟
      getCodeUrl: GLOBAL.urlHead + "paymentQRcode/",
      getStatusUrl: GLOBAL.urlHead + "paymentStatus/"
    };
  },
  mounted() {
    this.paymentID = this.$route.query.id;
    console.log(this.paymentID);
    Axios.get(this.getCodeUrl + "?paymentID=" + this.paymentID).then(
      response => {
        if (response.status === 200 && response.data["success"]) {
          let data = response.data;
          this.scancode = data.QRcode;
          this.orderList = data.order_list;
          this.orderList.forEach(element => {
            element.title = element.title + "-" + element.subtile;
          });
          this.total = data.total;
          let timer = setInterval(() => {
            Axios.get(
              this.getStatusUrl +
                "?paymentID=" +
                this.paymentID +
                "&?id=" +
                this.phone
            ).then(response => {
              if (response.status === 200) {
                let data = response.data;
                console.log(data);
                this.status = data.status;
              }
            });
            this.count++;
            // console.log(this.count);
            if (this.count >= this.timeMax * 60) {
              clearInterval(timer);
              this.scancode = unavailable;
              this.$message({
                type: "warning",
                message: this.$t("tips.unavailablecode")
              });
            }
          }, 1000);
        }
      }
    );
  },
  methods: {}
};
</script>

<style scoped>
.main {
  width: 80%;
  min-width: 1200px;
  min-height: 1000px;
  margin-top: 2 0px;
  margin-left: auto;
  margin-right: auto;
  /* border: solid 1px; */
}
.title {
  padding-left: 100px;
}
.data_table {
  width: 960px;
  height: 240px;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}
.scan {
  width: 960px;
  height: 500px;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
  /* border: solid 1px; */
}
.scan img {
  width: 420px;
  height: 420px;
}
.scan span {
  margin-left: 10px;
  margin-right: 10px;
}
</style>
