<!--返回顶部组件-->

<template>
  <transition :name="transitionName">
    <button class="page-component-up"
      @click="backToTop"
      v-show="visible"
      :style="customStyle"
      :disabled="btnDisabled">
    <p class="tipText">TOP</p>
    </button>
  </transition>
</template>

<script>
export default {
  name: 'BackToTop',
  props: {
    transitionName: {
      type: String,
      default: 'fade'
    },
    customStyle: {
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
      btnDisabled: false,
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll)
    if(this.interval) {
      clearInterval(this.interval)
    }
  },
  methods: {
    handleScroll() {
      this.visible = window.pageYOffset > this.visibilityHeight
    },
    backToTop() {
      this.btnDisabled = true;
      let distanceY = window.pageYOffset
      let i = 0
      this.interval = setInterval(() => {
        let next = Math.floor(this.easeInOutQuad(10 * i, distanceY, -distanceY, 500))
        if(next <= this.backPosition) {
          window.scrollTo(0, this.backPosition)
          clearInterval(this.interval)
        } else{
          window.scrollTo(0, next)
        }
        i++
      }, 17)
      setTimeout(()=>{
        this.btnDisabled = false;
      },2000)
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
        return c / 2 * t * t + b
      } else {
        // 将总长度设置为一半，并且时间从当前开始递减，对窗口进行垂直向上平移
        return -c / 2 * (--t * (t - 2) - 1) + b
      }
    }
  }
}
</script>

<style scoped>
.page-component-up{
  width: 100px;
  height: 200px;
  position: fixed;
  cursor: pointer;
  text-align: center;
  transition: .3s;
  box-shadow: 0 0 6px rgba(0,0,0,.12);
  z-index: 99;
}

.tipText{
  margin-top:0px;
  font-weight: bold;
  font-size: 10px;
}
</style>