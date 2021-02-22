<!--详情视图-->

<template>
  <div class="cartcontrol">
    <div class="main title">{{ item.title }}</div>
    <div class="text">{{ item.desc }}</div>
    <div class="label">
      <div
        class="type"
        v-for="(i, index) in item.type"
        :key="index"
        @click="typeChoose(index)"
        :class="active(index)"
      >
        {{ i.name }}
      </div>
    </div>
    <div class="text">
      {{ item.type[this.index].tip }}
    </div>
    <div class="price">
      <span class="price-1">{{ $t("good.price") }}</span>
      <span class="price-2">¥</span>
      <span class="price-3">{{ sumPrice }}</span>
    </div>
    <div class="reduce" @click="reduceCart">
      <img src="~assets/img/common/delete.jpg" />
    </div>
    <div class="num">{{ item.count }}</div>
    <div class="add" @click="addCart">
      <img src="~assets/img/common/add.jpg" />
    </div>
    <button
      id="add2cart"
      @click="changeNum()"
      @mouseenter="changeFocus"
      @mouseleave="removeFocus"
    >
      {{ $t("good.add2cart") }}
    </button>
    <button
      id="purchase"
      @click="jump2cart"
      @mouseenter="changeFocus"
      @mouseleave="removeFocus"
    >
      {{ $t("good.buy") }}
    </button>
  </div>
</template>

<script>
import GLOBAL from "@/common/const";
import Axios from "axios";

export default {
  name: "GoodView",
  // inject: ['reload'],
  data() {
    return {
      index: 0,
      counturl: GLOBAL.urlHead + "updateCartWeb/",
      phone: localStorage.getItem("userPhone")
    };
  },
  props: {
    item: {
      type: Object,
      //  默认赋值count为1
      default() {
        return {
          count: 1
        };
      }
    }
  },
  computed: {
    // 计算选中的总价
    sumPrice() {
      let price = this.item.count * this.item.type[this.index].price;
      price = parseFloat(price).toFixed(2);
      return price;
    }
  },
  methods: {
    // 加入购物车，再跳转至购物车页面
    jump2cart() {
      if (this.phone === null) {
        this.$message({
          type: "warning",
          message: "请先登录"
        });
        return 0;
      } else {
        // 此处设置2s时延用于后台更新数据，
        // 在自动跳转时有数据更新不及时导致显示错误的问题
        this.changeNum("正在跳转，请稍后...");
        const TIME_COUNT = 1;
        if (!this.timer) {
          this.count = TIME_COUNT;
          this.timer = setInterval(() => {
            if (this.count > 0 && this.count <= TIME_COUNT) {
              this.count--;
            } else {
              clearInterval(this.timer);
              this.timer = null;
              this.$router.push("/cart");
            }
          }, 1000);
        }
      }
    },
    active(index) {
      if (this.index == index) return "active";
      else {
        return "";
      }
    },
    // 改变购物车数目，传入参数msg成功提示信息
    changeNum(msg = "加入购物车成功") {
      if (this.phone === null) {
        this.$message({
          type: "warning",
          message: "请先登录"
        });
        return 0;
      }
      let url =
        this.counturl +
        "?id=" +
        this.phone +
        "&detail_id=" +
        this.item.type[this.index].id +
        "&num=" +
        this.item.count;
      Axios.get(url)
        .then(response => {
          if (response.status === 200) {
            this.$message({
              type: "success",
              message: msg
            });
            return 1;
          }
        })
        .catch(error => {
          this.$message({
            type: "warning",
            message: "后台出错"
          });
          console.log(error);
          return 0;
        });
    },
    addCart() {
      this.item.count++;
    },
    reduceCart() {
      if (this.item.count > 1) this.item.count--;
    },
    typeChoose(index) {
      this.item.count = 1;
      this.index = index;
    },
    changeFocus(e) {
      e.currentTarget.className = "focus";
    },
    removeFocus(e) {
      e.currentTarget.className = "unfocus";
    }
  }
};
</script>

<style scoped>
.cartcontrol {
  width: 550px;
  overflow: hidden;
}
.cartcontrol div {
  margin-top: 20px;
}
.main {
  font-size: 40px;
}
.text {
  height: 50px;
  font-size: 18px;
  line-height: 23px;
  color: gray;
  overflow: auto;
}
.reduce,
.add,
.type {
  cursor: pointer;
}
.reduce,
.num {
  float: left;
}
.label {
  width: 600px;
  height: 80px;
  display: flex;
  overflow: auto;
}
.type {
  height: 30px;
  border: 1px solid wheat;
  margin-left: 20px;
  padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px;
}
.type:first-of-type {
  margin-left: 0px;
}
.price {
  color: red;
  font-weight: bold;
}
.price-1 {
  font-size: 20px;
}
.price-2 {
  font-size: 20px;
  margin-left: 20px;
}
.price-3 {
  font-size: 40px;
  margin-left: 10px;
}
.reduce img,
.add img {
  width: 40px;
}
.num {
  font-size: 30px;
  margin-left: 30px;
  margin-right: 30px;
  text-align: center;
  width: 80px;
}
.active {
  border: 1px solid red;
  background: url("~assets/img/common/bingo.jpg") no-repeat bottom right;
  background-size: 12px 12px;
  font-weight: 600;
}
button {
  border: none;
  padding: 15px 50px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 24px;
  font-weight: bold;
  cursor: pointer;
  border-radius: 15px;
  outline: none;
}
#add2cart {
  background-color: #ffce6b;
  color: #6b6b6b;
  margin-right: 2%;
}
#purchase {
  margin-top: 20px;
  background-color: #ffb3a7;
  color: white;
}
.focus {
  border: 0.5px solid gray;
}
</style>
