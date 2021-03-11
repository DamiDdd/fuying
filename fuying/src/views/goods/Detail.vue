<!--详情页面-->

<template>
  <div id="detail">
    <cart-icon :iconStyle="cartIconStyle"></cart-icon>
    <div class="num-control">
      <!-- slider未传入图片参数时，默认显示没有相关信息图样 -->
      <div class="left"><slider :imgWidth="600"></slider></div>
      <div class="right"><good-view :item="good"></good-view></div>
    </div>
    <div class="img-window">
      <!-- <div class="label">
        <div
          class="type"
          v-for="(i, index) in good.imgs"
          :key="index"
          @click="tagChoose(index)"
          :class="judgeActive(index)"
        >
          <div @mouseenter="changeFocus" @mouseleave="removeFocus">
            {{ i.name }}
          </div>
        </div>
      </div> -->
      <div>
        <div class="left-window">
          <p v-for="(i, index) in good.imgs" :key="index" @click="jump(index)">
            {{ i.name }}
          </p>
        </div>
        <div
          v-for="(i, index2) in good.imgs"
          :key="index2"
          :index="i"
          class="imgs d_jump"
        >
          <el-image
            v-for="img in good.imgs[index2].imgs"
            :key="img"
            :src="img"
            lazy
            style="width:80%; margin-left: 5%; padding-top: 0.5%;"
          >
          </el-image>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import GoodView from "components/content/detail/GoodView";
import Slider from "components/common/slide/Slider";
import CartIcon from "components/common/cart/CartIcon";
import Axios from "axios";
import GLOBAL from "@/common/const";

export default {
  name: "Detail",
  components: {
    GoodView,
    Slider,
    CartIcon
  },
  data() {
    return {
      detailUrl: GLOBAL.urlHead + "getproductsdetail/?id=",
      goodId: 0,
      index: 0,
      // 关于iconStyle的细节设定
      cartIconStyle: {
        right: "5.875rem /* 94/16 */",
        bottom: "12.5rem /* 200/16 */",
        background: "#fff",
        "border-radius": "1.5625rem /* 25/16 */"
      },
      // 传参
      good: {
        title: "",
        count: 1,
        desc: "",
        index: 0,
        type: [
          // 数据样例
          {
            id: "1",
            name: "基础生理刻画套餐",
            tip: "包括基础",
            price: 10000
          }
        ],
        imgs: [
          // 数据样例
          {
            name: "等待填充",
            imgs: [
              "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1020757406,2710278676&fm=26&gp=0.jpg",
              "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1020757406,2710278676&fm=26&gp=0.jpg"
            ]
          }
        ]
      }
    };
  },
  mounted() {
    this.goodId = this.$route.query.goodId;
    this.good["count"] = 1;
    this.detailUrl += this.goodId;
    //  在这里申请拿到商品数据
    Axios.get(this.detailUrl).then(response => {
      if (response.status === 200) {
        console.log(response.data);
        // 不需要双向绑定
        let data = response.data;
        this.good.desc = data.desc;
        if (data.imgs.imgs !== []) {
          this.good.imgs = data.imgs;
        }
        if (data.imgs.imgs !== []) {
          this.good.type = data.type;
        }
        this.good.title = data.title;
      } else {
        this.$message({
          type: "warning",
          message: this.$t("tips.servererror")
        });
      }
    });
  },
  methods: {
    tagChoose(index) {
      this.index = index;
    },
    judgeActive(index) {
      if (this.index === index) {
        return "active";
      } else {
        return "";
      }
    },
    changeFocus(e) {
      e.currentTarget.className = "focus";
    },
    removeFocus(e) {
      e.currentTarget.className = "";
    },
    jump(index) {
      // 用 class="d_jump" 添加锚点
      let jump = document.querySelectorAll(".d_jump");
      let total = jump[index].offsetTop;
      let distance =
        document.documentElement.scrollTop || document.body.scrollTop;
      // 平滑滚动，时长500ms，每10ms一跳，共50跳
      let step = total / 50;
      if (total > distance) {
        smoothDown();
      } else {
        let newTotal = distance - total;
        step = newTotal / 50;
        smoothUp();
      }
      function smoothDown() {
        if (distance < total) {
          distance += step;
          document.body.scrollTop = distance;
          document.documentElement.scrollTop = distance;
          setTimeout(smoothDown, 10);
        } else {
          document.body.scrollTop = total;
          document.documentElement.scrollTop = total;
        }
      }
      function smoothUp() {
        if (distance > total) {
          distance -= step;
          document.body.scrollTop = distance;
          document.documentElement.scrollTop = distance;
          setTimeout(smoothUp, 10);
        } else {
          document.body.scrollTop = total;
          document.documentElement.scrollTop = total;
        }
      }
    }
  }
};
</script>

<style scoped>
#detail {
  min-height: var(--screen-height);
  width: var(--screen-width);
  min-width: var(--min-width);
  background: -webkit-linear-gradient(top, white, lightblue, white);
}
.num-control {
  min-height: 37.5rem /* 600/16 */;
  width: 80%;
  margin-left: 12.5rem /* 200/16 */;
  padding-top: 6.25rem /* 100/16 */;
}
.left {
  float: left;
  width: 37.5rem /* 600/16 */;
  min-height: 28.125rem /* 450/16 */;
  margin-top: 5rem /* 80/16 */;
}
.right {
  float: left;
  position: absolute;
  margin-left: 43.75rem /* 700/16 */;
  width: 37.5rem /* 600/16 */;
  min-height: 37.5rem /* 600/16 */;
}
.cartcontrol {
  height: 43.75rem /* 700/16 */;
  margin-left: 6.25rem /* 100/16 */;
}
.img-window {
  margin-top: 8.125rem /* 130/16 */;
  margin-left: 19%;
  min-height: 37.5rem /* 600/16 */;
  width: 70%;
}
.label {
  margin-left: 5%;
}
.type {
  float: left;
  width: 10%;
  height: 1.875rem /* 30/16 */;
  text-align: center;
  border: .0625rem /* 1/16 */ solid #ccc;
  border-style: none solid;
  padding-top: .5rem /* 8/16 */;
  cursor: pointer;
}
/* 设定图片菜单选中样式 */
.active {
  background: url("~assets/img/common/topbar-bt-bg.png") no-repeat top center;
  background-size: 90% 10%;
  font-weight: 600;
}
.left-window {
  /* background: #000; */
  width: 6.25rem /* 100/16 */;
  height: 6.25rem /* 100/16 */;
  left: 15.625rem /* 250/16 */;
  float: left;
  position: fixed;
}
.left-window p {
  cursor: pointer;
  color: var(--theme-color);
}

.left-window p:hover {
  font-weight: bold;
}
.focus {
  font-weight: 600;
}
.windows {
  width: 80%;
  min-width: 50rem /* 800/16 */;
  margin-left: auto;
  margin-right: auto;
  /* background: #000; */
}
</style>
