<!--cart条目view-->

<template>
  <div v-if="countExist" id="cart-view" :style="chooseStyle">
    <div class="flag"><input type="checkbox" v-model="good.flag" /></div>
    <div class="img"><img :src="good.product_img" /></div>
    <div class="title1" @click="jump2detail">{{ good.product }}</div>
    <div class="title2">{{ good.detail }}</div>
    <div class="price-single">{{ good.price }}</div>
    <div class="num-control">
      <div class="reduce" @click="reduceCart">
        <img src="~assets/img/common/delete.jpg" />
      </div>
      <div class="num">{{ good.num }}</div>
      <div class="add" @click="addCart">
        <img src="~assets/img/common/add.jpg" />
      </div>
    </div>
    <div class="price-sum">{{ good.priceSum }}</div>
    <div class="delete">
      <el-button class="el-btn" @click="deleteReverse">{{
        $t("public.delete")
      }}</el-button>
      <div v-show="this.deleteBtn" class="answer">
        <button class="btn" @click="deleteConfirmed">
          {{ $t("public.confirm") }}
        </button>
        <button class="btn" @click="deleteReverse">
          {{ $t("public.cancel") }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import GLOBAL from "@/common/const";
import Axios from "axios";

export default {
  name: "CartView",
  props: {
    good: Object
  },
  data() {
    return {
      deleteBtn: false,
      counturl: GLOBAL.urlHead + "updateCartWeb/",
      phone: localStorage.getItem("userPhone")
    };
  },
  computed: {
    // 数目是否为0
    countExist() {
      return this.good.num > 0;
    },
    // 控制focus样式
    chooseStyle() {
      if (this.good.flag) {
        return "border: .0625rem /* 1/16 */ solid black";
      } else {
        return "";
      }
    }
  },
  methods: {
    // 确认按钮的开启关闭
    deleteReverse() {
      this.deleteBtn = !this.deleteBtn;
    },
    // 跳转至详情页
    jump2detail() {
      this.$router.push({
        path: "/detail",
        query: { goodId: this.good.product_id }
      });
    },
    // 更新购物车数目状态
    changeNum() {
      let url =
        this.counturl +
        "?id=" +
        this.phone +
        "&detail_id=" +
        this.good.detail_id +
        "&num=" +
        this.good.num;
      Axios.get(url).then(response => {
        if (!response.status === 200) {
          this.$message({
            type: "warning",
            message: "后台出错"
          });
        }
      });
    },
    // 添加数量
    addCart() {
      this.good.num++;
      this.good.priceSum = parseFloat(this.good.num * this.good.price).toFixed(
        2
      );
      // 向后台传输最新数据
      this.changeNum();
    },
    // 减少数量
    reduceCart() {
      if (this.good.num > 1) {
        this.good.num--;
        this.good.priceSum = parseFloat(
          this.good.num * this.good.price
        ).toFixed(2);
        // 向后台传输最新数据
        this.changeNum();
      }
    },
    // 删除购物车条目
    deleteConfirmed() {
      this.good.num = 0;
      this.good.flag = false;
      // 向后台传输数据
      this.changeNum();
    }
  }
};
</script>

<style scoped>
#cart-view {
  width: 60%;
  min-width: 50rem /* 800/16 */;
  height: 7.5rem /* 120/16 */;
  border: 0.0625rem /* 1/16 */ solid mediumaquamarine;
  margin-left: 25rem /* 400/16 */;
  display: flex;
  margin-bottom: 0.625rem /* 10/16 */;
  text-align: center;
}
.flag,
.title1,
.title2,
.price-single,
.num-control,
.price-sum,
.delete {
  padding-top: 2.5rem /* 40/16 */;
}
.flag {
  width: 10%;
}
.img {
  width: 16%;
}
.img img {
  height: 7.5rem /* 120/16 */;
}
.title1 {
  width: 14%;
  cursor: pointer;
}
.title1:hover {
  font-weight: bold;
}
.title2 {
  width: 12%;
}
.price-single {
  width: 12%;
}
.num-control {
  width: 12%;
}
.price-sum {
  width: 12%;
}
.delete {
  width: 12%;
  cursor: pointer;
}
.delete span:hover {
  text-decoration: line-through;
}
.reduce,
.add {
  cursor: pointer;
}
.reduce,
.num,
.add {
  float: left;
  width: 33%;
}
.reduce img,
.add img {
  width: 1.25rem /* 20/16 */;
}
.answer {
  width: 100%;
  margin-left: 0.625rem /* 10/16 */;
  margin-top: 0.3125rem /* 5/16 */;
}
.btn {
  float: left;
  width: 3.75rem /* 60/16 */;
  cursor: pointer;
}
.el-btn {
  margin-left: 0.2rem;
  margin-top: -0.35rem;
}
</style>
