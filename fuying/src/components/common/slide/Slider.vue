<!--轮播图片组件-->

<template>
  <div id="slider">
    <div
      class="window"
      :style="{ width: imgWidth + 'px' }"
      @mouseover="stop"
      @mouseleave="play"
    >
      <ul class="container" :style="containerStyle">
        <li>
          <img
            :style="{ width: imgWidth + 'px' }"
            :src="sliders[sliders.length - 1].img"
            alt=""
          />
        </li>
        <li v-for="(item, index) in sliders" :key="index">
          <img :style="{ width: imgWidth + 'px' }" :src="item.img" alt="" />
        </li>
      </ul>
      <ul class="direction">
        <li class="left" @click="move(imgWidth, 1, speed)">
          <svg
            class="icon"
            width="1.875rem /* 30/16 */"
            height="1.875rem /* 30/16 */"
            viewBox="0 0 1024 1024"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill="#ffffff"
              d="M481.233 904c8.189 0 16.379-3.124 22.628-9.372 12.496-12.497 12.496-32.759 0-45.256L166.488 512l337.373-337.373c12.496-12.497 12.496-32.758 0-45.255-12.498-12.497-32.758-12.497-45.256 0l-360 360c-12.496 12.497-12.496 32.758 0 45.255l360 360c6.249 6.249 14.439 9.373 22.628 9.373z"
            />
          </svg>
        </li>
        <li class="right" @click="move(imgWidth, -1, speed)">
          <svg
            class="icon"
            width="1.875rem /* 30/16 */"
            height="1.875rem /* 30/16 */"
            viewBox="0 0 1024 1024"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill="#ffffff"
              d="M557.179 904c-8.189 0-16.379-3.124-22.628-9.372-12.496-12.497-12.496-32.759 0-45.256L871.924 512 534.551 174.627c-12.496-12.497-12.496-32.758 0-45.255 12.498-12.497 32.758-12.497 45.256 0l360 360c12.496 12.497 12.496 32.758 0 45.255l-360 360c-6.249 6.249-14.439 9.373-22.628 9.373z"
            />
          </svg>
        </li>
      </ul>
      <ul class="dots" v-show="morethanone">
        <li
          v-for="(dot, i) in sliders"
          :key="i"
          :class="{ dotted: i === currentIndex - 1 }"
          @click="jump(i + 1)"
        ></li>
      </ul>
    </div>
  </div>
</template>

<script>
// 本地notfound图片
// import notfound from "../../../assets/img/common/notfound.png";
import temp1 from "../../../assets/img/bg/bgtemp1.jpg";
import temp2 from "../../../assets/img/bg/bgtemp2.jpg";

export default {
  name: "slider",
  props: {
    // 初始切换速度
    initialSpeed: {
      type: Number,
      default: 30
    },
    // timer
    initialInterval: {
      type: Number,
      default: 3
    },
    // 传入imgWidth大小
    imgWidth: {
      type: Number,
      default: 600
    },
    // 传入图片URL数组
    sliders: {
      type: Array,
      default() {
        return [
          // 用于测试
          {
            img: temp1
          },
          {
            img: temp2
          }
          // {
          //   img: notfound
          // }
        ];
      }
    }
  },
  data() {
    return {
      currentIndex: 1,
      distance: -1 * this.imgWidth,
      transitionEnd: true,
      speed: this.initialSpeed
    };
  },
  computed: {
    containerStyle() {
      return {
        transform: `translate3d(${this.distance}px, 0, 0)`
      };
    },
    interval() {
      return this.initialInterval * 1000;
    },
    morethanone() {
      return this.sliders.length > 1;
    }
  },
  mounted() {
    this.init();
  },
  methods: {
    // 初始化，绑定blue/focus事件
    init() {
      this.play();
      window.onblur = function() {
        this.stop();
      }.bind(this);
      window.onfocus = function() {
        this.play();
      }.bind(this);
    },
    // 移动图片
    move(offset, direction, speed) {
      //   console.log(speed)
      if (!this.transitionEnd) return;
      this.transitionEnd = false;
      direction === -1
        ? (this.currentIndex += offset / this.imgWidth)
        : (this.currentIndex -= offset / this.imgWidth);
      if (this.currentIndex > this.sliders.length) this.currentIndex = 1;
      if (this.currentIndex < 1) this.currentIndex = this.sliders.length;
      //   console.log(this.currentIndex)
      const destination = this.distance + offset * direction;
      this.animate(destination, direction, speed);
    },
    // 滑动
    animate(des, direc, speed) {
      if (this.temp) {
        window.clearInterval(this.temp);
        this.temp = null;
      }
      this.temp = window.setInterval(() => {
        if (
          (direc === -1 && des < this.distance) ||
          (direc === 1 && des > this.distance)
        ) {
          this.distance += speed * direc;
        } else {
          this.transitionEnd = true;
          window.clearInterval(this.temp);
          this.distance = des;
          if (des < -1 * (this.sliders.length * this.imgWidth))
            this.distance = -1 * this.imgWidth;
          if (des > -this.imgWidth)
            this.distance = -1 * (this.sliders.length * this.imgWidth);
        }
      }, 20);
    },
    // 点击数字跳转
    jump(index) {
      const direction = index - this.currentIndex >= 0 ? -1 : 1;
      const offset = Math.abs(index - this.currentIndex) * this.imgWidth;
      const jumpSpeed =
        Math.abs(index - this.currentIndex) === 0
          ? this.speed
          : Math.abs(index - this.currentIndex) * this.speed;
      this.move(offset, direction, jumpSpeed);
    },
    // 控制自动播放和暂停
    play() {
      if (this.timer) {
        window.clearInterval(this.timer);
        this.timer = null;
      }
      this.timer = window.setInterval(() => {
        this.move(this.imgWidth, -1, this.speed);
      }, this.interval);
    },
    stop() {
      window.clearInterval(this.timer);
      this.timer = null;
    }
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
ol,
ul {
  list-style: none;
}
#slider {
  text-align: center;
}
.window {
  position: relative;
  /* width作为传入参数更新 */
  /* width: imgWidth; */
  height: 25rem /* 400/16 */;
  margin: 0 auto;
  overflow: hidden;
}
.container {
  display: flex;
  position: absolute;
  align-self: center;
}
.left,
.right {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 3.125rem /* 50/16 */;
  height: 3.125rem /* 50/16 */;
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  cursor: pointer;
}
.left {
  left: 3%;
  padding-left: .75rem /* 12/16 */;
  padding-top: .625rem /* 10/16 */;
}
.right {
  right: 3%;
  padding-right: .75rem /* 12/16 */;
  padding-top: .625rem /* 10/16 */;
}
img {
  user-select: none;
}
.dots {
  position: absolute;
  bottom: .625rem /* 10/16 */;
  left: 50%;
  transform: translateX(-50%);
}
.dots li {
  display: inline-block;
  width: .9375rem /* 15/16 */;
  height: .9375rem /* 15/16 */;
  margin: 0 .1875rem /* 3/16 */;
  border: .0625rem /* 1/16 */ solid white;
  border-radius: 50%;
  background-color: #333;
  cursor: pointer;
}
.dots .dotted {
  background-color: orange;
}
</style>
