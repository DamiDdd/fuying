<!--详情视图-->

<template>
  <div class="cartcontrol">
    <div class="main">{{ item.title }}</div>
    <div class="text">{{ item.desc }}</div>
    <div class="label">
      <div
        class="type"
        v-for="(i, index) in item.type"
        :key="index"
        @click="typeChoose(index)"
        :class="active(index)"
      >
        {{ i.name }} / {{ i.tip }}
        <span>￥{{ i.price }}</span>
      </div>
    </div>
    <!-- <div class="text">
      {{ item.type[this.index].tip }}
    </div> -->
    <!-- <div class="price">
      <span class="price-1">{{ $t("good.price") }}</span>
      <span class="price-2">¥</span>
      <span class="price-3">{{ sumPrice }}</span>
    </div> -->
    <div class="reduce" @click="reduceCart">
      <img src="~assets/img/common/delete.jpg" />
    </div>
    <div class="num">{{ item.count }}</div>
    <div class="add" @click="addCart">
      <img src="~assets/img/common/add.jpg" />
    </div>
    <button class="btn" id="add2cart" title="开启健康检测之旅">
      {{ $t("good.add2cart") }}
    </button>
    <button
      class="btn"
      id="purchase"
      @click="jump2cart"
      title="即可畅享优质服务！"
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
    }
  }
};
</script>

<style scoped>
.cartcontrol {
  width: 34.375rem /* 550/16 */;
  overflow: hidden;
  /* background: #000; */
}
.cartcontrol div {
  margin-top: 1.25rem /* 20/16 */;
}
.main {
  font-size: 2.5rem /* 40/16 */;
}
.text {
  height: 3.125rem /* 50/16 */;
  padding-top: 2rem;
  font-size: 1.125rem /* 18/16 */;
  line-height: 1.4375rem /* 23/16 */;
  color: gray;
  overflow: auto;
}
.reduce {
  padding-left: 2rem;
}
.reduce,
.add,
.type {
  cursor: pointer;
  padding-bottom: 1rem;
}
.reduce,
.num {
  float: left;
}
.label {
  width: 37.5rem /* 600/16 */;
  min-height: 10rem /* 80/16 */;
  /* display: flex; */
  overflow: auto;
}
.type {
  /* height: 3rem; */
  border: 0.0625rem /* 1/16 */ solid silver;
  width: 16rem;
  margin-left: 1.25rem /* 20/16 */;
  padding-top: 0.6rem;
  padding-bottom: 0.6rem;
  padding-left: 0.625rem /* 10/16 */;
  padding-right: 0.625rem /* 10/16 */;
  font-size: 1rem;
}
/* .type:first-of-type {
  margin-left: 0rem;
} */
.price {
  color: red;
  font-weight: bold;
}
.price-1 {
  font-size: 1.25rem /* 20/16 */;
}
.price-2 {
  font-size: 1.25rem /* 20/16 */;
  margin-left: 1.25rem /* 20/16 */;
}
.price-3 {
  font-size: 2.5rem /* 40/16 */;
  margin-left: 0.625rem /* 10/16 */;
}
.reduce img,
.add img {
  width: 1.5rem /* 40/16 */;
}
.num {
  font-size: 1.2rem /* 30/16 */;
  margin-left: 1.875rem /* 30/16 */;
  margin-right: 1.875rem /* 30/16 */;
  text-align: center;
  width: 5rem /* 80/16 */;
}
.active {
  border: 0.0625rem /* 1/16 */ solid black;
  background: url("~assets/img/common/bingo.jpg") no-repeat bottom right;
  background-size: 0.75rem /* 12/16 */ 0.75rem /* 12/16 */;
  font-weight: 600;
}
button {
  border: none;
  padding: 0.9375rem /* 15/16 */ 3.125rem /* 50/16 */;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 1.5rem /* 24/16 */;
  /* font-weight: bold; */
  cursor: pointer;
  border-radius: 0.9375rem /* 15/16 */;
  outline: none;
}
#add2cart {
  color: #6b6b6b;
  margin-right: 2%;
  border: 0.05rem solid silver;
}
#purchase {
  margin-top: 1.25rem;
  color: #6b6b6b;
  border: 0.05rem solid silver;
}

.btn {
  width: 14rem;
  background: sliver;
  opacity: 0.8;
}
.btn:hover {
  font-weight: bold;
  opacity: 1;
}
</style>
