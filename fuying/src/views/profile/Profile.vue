<!--个人档案页面-->

<template>
  <div id="profile">
    <div class="main">
      <div class="left">
        <div class="left-top">
          <p class="content-blue">{{ $t("profile.title") }}</p>
          <el-button @click="jump('/cart')">{{ $t("profile.cart") }}</el-button>
          <el-button @click="jump('/health')">{{
            $t("profile.health")
          }}</el-button>
          <el-button @click="callOn">{{ $t("profile.order") }}</el-button>
          <!-- <el-button @click="jump('/pdf')">查看报告</el-button> -->
          <el-button class="warning" @click="jump('/exit')">{{
            $t("profile.exit")
          }}</el-button>
        </div>
        <!-- <div v-show="admin" class="left-bottom">
          <p class="content-blue">{{ $t("profile.manager") }}</p>
          <el-button @click="jump('/reportEdit')">{{
            $t("profile.upload")
          }}</el-button>
          <el-button @click="jump('/manager')">{{
            $t("profile.report")
          }}</el-button>
          <el-button @click="jump('/uploadGood')">{{
            $t("profile.uploadgood")
          }}</el-button>
        </div> -->
      </div>
      <div class="right">
        <div class="right-top">
          <p class="content-blue">{{ $t("profile.profile") }}</p>
          <div class="info">
            <div class="info-content">
              <!-- <p>用户名：<input type="text" v-model="name"></p> -->
              <p>{{ $t("public.username") }}：{{ name }}</p>
              <p>{{ $t("public.phone") }}：{{ phone }}</p>
              <!-- <p>邮箱：<input type="text" v-model="email"></p> -->
              <p>{{ $t("public.email") }}：{{ email }}</p>
            </div>
            <div class="btn">
              <!-- <el-button>修改密码</el-button> -->
              <!-- <el-button @click="submitMsg">提交修改</el-button> -->
            </div>
          </div>
          <div class="image">
            <el-avatar :size="80" :src="circleUrl"></el-avatar>
            <!-- <img src="~assets/img/common/user.png"> -->
          </div>
        </div>
        <div class="right-middle">
          <p class="content-blue">{{ $t("profile.receiverarray") }}</p>
          <el-table :data="addressTable" class="data_table">
            <el-table-column
              prop="user"
              :label="$t('profile.receiver')"
              width="180"
            ></el-table-column>
            <el-table-column
              prop="phone"
              :label="$t('public.phone')"
              width="180"
            ></el-table-column>
            <el-table-column
              prop="address"
              :label="$t('public.address')"
              width="400"
            ></el-table-column>
            <!-- <el-table-column label="操作" width="100"></el-table-column> -->
          </el-table>
        </div>
        <!-- <div class="right-bottom">
        </div> -->
      </div>
    </div>
    <modal
      :show="modal"
      :title="titleM"
      v-on:hideModal="hideModal"
      v-on:submit="confirm"
    >
      <div class="in-content">
        <table class="el-table el-table--fit el-table--border table-detail">
          <thead>
            <tr>
              <th width="10rem /* 160/16 */">{{ $t("profile.service") }}</th>
              <th width="10rem /* 160/16 */">{{ $t("profile.date") }}</th>
              <th width="10rem /* 160/16 */">{{ $t("profile.num") }}</th>
              <th width="10rem /* 160/16 */">{{ $t("profile.total") }}</th>
              <th width="10rem /* 160/16 */">{{ $t("profile.status") }}</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td colspan="5" style="text-align: center;" v-show="emptyOrder">
                {{ $t("tips.noinfo") }}
              </td>
            </tr>
            <tr v-for="(item, index) in orderInList" :key="index">
              <td @click="jump2detail(item.product_id)" class="good">
                {{ item.product }}-{{ item.detail }}
              </td>
              <td v-text="item.date"></td>
              <td v-text="item.num"></td>
              <td v-text="item.priceSum"></td>
              <td
                class="available"
                v-show="available(item.status)"
                @click="solveStatus(item.order_id, item.phone, item.status)"
                v-text="item.status"
              ></td>
              <td v-show="!available(item.status)" v-text="item.status"></td>
            </tr>
          </tbody>
        </table>
        <table
          v-show="transport"
          class="el-table el-table--fit el-table--border table-detail transport"
        >
          <thead>
            <tr>
              <th width="6.25rem /* 100/16 */">{{ $t("profile.orderid") }}</th>
              <th width="6.25rem /* 100/16 */">{{ $t("profile.transitid") }}</th>
              <th width="6.25rem /* 100/16 */">{{ $t("profile.time") }}</th>
              <th width="12.5rem /* 200/16 */">
                {{ $t("profile.info")
                }}<span class="after" @click="unspread"
                  >^{{ $t("profile.withdraw") }}</span
                >
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in transportMsg" :key="index">
              <td v-text="item.orderID"></td>
              <td v-text="item.ExpressNumber"></td>
              <td v-text="item.time"></td>
              <td v-text="item.context"></td>
            </tr>
          </tbody>
        </table>
      </div>
    </modal>
  </div>
</template>

<script>
import Modal from "components/common/modal/Modal";
import GLOBAL from "@/common/const";
import Axios from "axios";

export default {
  name: "Profile",
  components: {
    Modal
  },
  data() {
    return {
      phone: localStorage.getItem("userPhone"),
      name: localStorage.getItem("userName"),
      email: localStorage.getItem("userEmail"),
      orderUrl: GLOBAL.urlHead + "getOrders/",
      transportUrl: GLOBAL.urlHead + "getExpressList/",
      addUrl: GLOBAL.urlHead + "getCommonlyAddress/",
      pdfUrl: GLOBAL.urlHead2 + "get_pdf/",
      emptyOrder: false,
      transport: false,
      addressTable: [
        {
          user: "a",
          phone: "13333333333",
          address: "北京"
        }
      ],
      modal: false,
      titleM: "您的订单",
      orderInList: [
        {
          order_id: "A01",
          product: "基础套餐",
          product_id: "00001",
          detail: "升级版",
          detail_id: "1",
          product_img: "",
          price: 200,
          num: 2,
          priceSum: 400,
          date: "2020/9/1 10:00",
          status: "pending"
        }
      ],
      transportMsg: [],
      circleUrl:
        "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
    };
  },
  mounted() {
    let url = this.addUrl + "?phone=" + this.phone;
    Axios.get(url)
      .then(response => {
        if (response.status === 200) {
          let data = response.data;
          // console.log(data);
          this.addressTable = data;
        }
      })
      .catch(error => {
        this.$message({
          type: "warning",
          message: this.$t("tips.servererror")
        });
        console.log(error);
      });
  },
  computed: {
    admin() {
      if (localStorage.getItem("admin") != null) {
        return true;
      } else {
        return false;
      }
    }
  },
  methods: {
    available(status) {
      if (status === "in_transit" || status === "report") return true;
      else {
        return false;
      }
    },
    solveStatus(order_id, phone, status) {
      switch (status) {
        case "in_transit":
          this.transport = true;
          Axios.post(
            this.transportUrl + "?orderID=" + order_id + "&phone=" + phone
          )
            .then(response => {
              if (response.status === 200) {
                let data = response.data;
                // console.log(data);
                this.transportMsg = data;
              }
            })
            .catch(error => {
              this.$message({
                type: "warning",
                message: this.$t("tips.servererror")
              });
              console.log(error);
            });
          break;
        case "report":
          var url = this.pdfUrl + "orderID=" + order_id + "&phone=" + phone;
          window.open(url);
          break;
        default:
          break;
      }
    },
    unspread() {
      this.transport = false;
    },
    jump(link) {
      this.$router.push(link);
    },
    jump2detail(goodId) {
      this.$router.push({ path: "/detail", query: { goodId: goodId } });
    },
    submitMsg() {
      console.log(this.name + this.email);
    },
    callOn() {
      this.modal = true;
      let url = this.orderUrl + "?phone=" + this.phone;
      Axios.get(url)
        .then(response => {
          if (response.status === 200) {
            let data = response.data;
            console.log(data);
            this.orderInList = data;
            if (this.orderInList.length === 0) {
              this.emptyOrder = true;
            }
          }
        })
        .catch(error => {
          this.$message({
            type: "warning",
            message: this.$t("tips.servererror")
          });
          console.log(error);
        });
    },
    hideModal() {
      this.modal = false;
      this.transport = false;
    },
    confirm() {
      this.modal = false;
      this.transport = false;
    }
  }
};
</script>

<style scoped>
#profile {
  background: url("~assets/img/bg/doctor.png") no-repeat bottom left;
}

.main {
  width: 100%;
  min-width: var(--min-width);
  height: 62.5rem /* 1000/16 */;
  /* margin-left: 14%; */
  padding-top: 5rem /* 80/16 */;
  display: flex;
}

.left {
  width: 20%;
  height: 100%;
  margin-left: 14%;
}

.left div button {
  width: 80%;
  margin-left: 10%;
  margin-bottom: 2%;
}

.left div p {
  text-align: center;
}

.right {
  width: 60%;
  height: 100%;
}

.left-top {
  width: 80%;
  height: 50%;
  margin-left: 10%;
}

.left-bottom {
  width: 80%;
  height: 30%;
  margin-left: 10%;
}

.right-top {
  width: 80%;
  height: 40%;
}

.right-middle {
  width: 60%;
  height: 40%;
}

.right-bottom {
  width: 100%;
  height: 20%;
}

#profile {
  min-height: 31.25rem /* 500/16 */;
}

.warning {
  color: red;
  font-weight: bold;
}

.info {
  width: 60%;
  height: 80%;
  float: left;
}

.info p {
  font-weight: bold;
  margin-top: 5%;
  padding-left: 5%;
  font-size: 1.25rem /* 20/16 */;
}

.info-content {
  height: 70%;
}

.btn {
  display: flex;
  margin-left: 30%;
}

.btn button {
  margin-top: 2%;
  margin-left: 10%;
}

.image {
  width: 40%;
  height: 80%;
  float: right;
}

.image img {
  min-width: 12.5rem /* 200/16 */;
  width: 80%;
}

.right p {
  margin-left: 5%;
}

input {
  border: none;
  font-weight: bold;
}

.data_table {
  margin-left: 5%;
  width: 95%;
  height: 18.75rem /* 300/16 */;
  overflow: auto;
}

.in-content {
  width: 50rem /* 800/16 */;
  height: 31.25rem /* 500/16 */;
  overflow: auto;
}

.good {
  cursor: pointer;
}

.good:hover {
  font-weight: bold;
}

.transport {
  margin-top: 5rem /* 80/16 */;
}

.after {
  float: right;
  margin-right: .625rem /* 10/16 */;
  color: lightblue;
  cursor: pointer;
}

.available {
  cursor: pointer;
}
.available:hover {
  color: lightblue;
  font-weight: bold;
}
</style>
