<!--返回顶部组件-->

<template>
  <transition :name="transitionName">
    <el-button
      class="page-component-up"
      @click="backToTop"
      v-show="visible"
      :style="customStyle"
      :disabled="btnDisabled"
    >
      <p class="tipText">TOP</p>
    </el-button>
  </transition>
</template>

<script>
export default {
  name: "BackToTop",
  props: {
    transitionName: {
      // 过渡样式
      type: String,
      default: "fade"
    },
    customStyle: {
      // 自设定icon样式
      type: Object
    },
    visibilityHeight: {
      // 纵向滑动出现滚动条的距离
      type: Number
    },
    backPosition: {
      // 返回顶部时，滚动到达位置距离顶部的距离
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      visible: false,
      interval: null,
      btnDisabled: false
    };
  },
  mounted() {
    // 监听滚动事件
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeDestroy() {
    // 重置计时器
    window.removeEventListener("scroll", this.handleScroll);
    if (this.interval) {
      clearInterval(this.interval);
    }
  },
  methods: {
    // 控制icon是否可见
    handleScroll() {
      this.visible = window.pageYOffset > this.visibilityHeight;
    },

    // 滚动
    backToTop() {
      // 加锁，避免重复点击timer出错
      this.btnDisabled = true;
      let distanceY = window.pageYOffset;
      let i = 0;
      this.interval = setInterval(() => {
        let next = Math.floor(
          this.easeInOutQuad(10 * i, distanceY, -distanceY, 500)
        );
        if (next <= this.backPosition) {
          window.scrollTo(0, this.backPosition);
          clearInterval(this.interval);
        } else {
          window.scrollTo(0, next);
        }
        i++;
      }, 17);
      setTimeout(() => {
        this.btnDisabled = false;
      }, 2000);
    },
    /*
      缓动公式（Tween算法）
       t: 动画已经执行的时间（实际上执行多少次/帧数）
       b: 起始位置
       c: 终止位置
       d: 从起始位置到终止位置的经过时间（实际上执行多少次/帧数）
    */
    easeInOutQuad(t, b, c, d) {
      // 判断当前时间是否总在总时间的一半以内，是的话执行缓入函数，否则的话执行缓出函数
      if ((t /= d / 2) < 1) {
        return (c / 2) * t * t + b;
      } else {
        // 将总长度设置为一半，并且时间从当前开始递减，对窗口进行垂直向上平移
        return (-c / 2) * (--t * (t - 2) - 1) + b;
      }
    }
  }
};
</script>

<style scoped>
.page-component-up {
  width: 6.25rem /* 100/16 */;
  height: 12.5rem /* 200/16 */;
  position: fixed;
  cursor: pointer;
  text-align: center;
  transition: 0.3s;
  box-shadow: 0 0 0.375rem /* 6/16 */ rgba(0, 0, 0, 0.12);
  z-index: 99;
}

.tipText {
  margin-top: -0.75rem /* 12/16 */;
  margin-left: -0.75rem /* 12/16 */;
  font-weight: bold;
  font-size: 0.625rem /* 10/16 */;
}
</style>
