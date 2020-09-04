<template>
  <div id="slider">
    <div class="window" :style="{width:imgWidth+'px'}" @mouseover="stop" @mouseleave="play">
      <ul class="container" :style="containerStyle">
        <li>
          <img :style="{width:imgWidth+'px'}" :src="sliders[sliders.length - 1].img" alt="">
        </li>
        <li  v-for="(item, index) in sliders" :key="index">
          <img :style="{width:imgWidth+'px'}" :src="item.img" alt="">
        </li>
        <li>
          <img :style="{width:imgWidth+'px'}" :src="sliders[0].img" alt="">
        </li>
      </ul>
      <ul class="direction">
        <li class="left" @click="move(imgWidth, 1, speed)">
          <svg class="icon" width="30px" height="30.00px" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path fill="#ffffff" d="M481.233 904c8.189 0 16.379-3.124 22.628-9.372 12.496-12.497 12.496-32.759 0-45.256L166.488 512l337.373-337.373c12.496-12.497 12.496-32.758 0-45.255-12.498-12.497-32.758-12.497-45.256 0l-360 360c-12.496 12.497-12.496 32.758 0 45.255l360 360c6.249 6.249 14.439 9.373 22.628 9.373z"  /></svg>
        </li>
        <li class="right" @click="move(imgWidth, -1, speed)">
          <svg class="icon" width="30px" height="30.00px" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path fill="#ffffff" d="M557.179 904c-8.189 0-16.379-3.124-22.628-9.372-12.496-12.497-12.496-32.759 0-45.256L871.924 512 534.551 174.627c-12.496-12.497-12.496-32.758 0-45.255 12.498-12.497 32.758-12.497 45.256 0l360 360c12.496 12.497 12.496 32.758 0 45.255l-360 360c-6.249 6.249-14.439 9.373-22.628 9.373z"  /></svg>
        </li>
      </ul>
      <ul class="dots" v-show="morethanone">
        <li v-for="(dot, i) in sliders" :key="i"
        :class="{dotted: i === (currentIndex-1)}"
        @click = jump(i+1)
        >
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import notfound from '../../../assets/img/common/notfound.png'

export default {
  name: 'slider',
  props: {
    initialSpeed: {
      type: Number,
      default: 30
    },
    initialInterval: {
      type: Number,
      default: 3
    },
    // 传入imgWidth大小
    imgWidth:{
      type: Number,
      default: 600,
    },
    // 传入图片URL数组
    sliders:{
      type: Array,
      default(){
        return [
        // {
        //   img:'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1599128436987&di=fb96b4b13f8107675eb1e46ec461535d&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Fa1098535f9b8bde03b5cfcfec48627320d1f12a15100f-o1IY9b_fw658'
        // },
        // {
        //   img:'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1599128436986&di=8771b1e83895e6cd2b3ac15d83adda55&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F1%2F57bd44387447f.jpg'
        // },
        {
          img: notfound
        }]  
      }
    }
  },
  data () {
    return {
    //   sliders:[
    //     {
    //       img:'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1599128436987&di=fb96b4b13f8107675eb1e46ec461535d&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Fa1098535f9b8bde03b5cfcfec48627320d1f12a15100f-o1IY9b_fw658'
    //     },
    //     {
    //       img:'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1599128436986&di=8771b1e83895e6cd2b3ac15d83adda55&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F1%2F57bd44387447f.jpg'
    //     },
    //   ],
      currentIndex:1,
      distance:-1*this.imgWidth,
      transitionEnd: true,
      speed: this.initialSpeed
    }
  },
  computed:{
    containerStyle() {
      return {
        transform:`translate3d(${this.distance}px, 0, 0)`
      }
    },
    interval() {
      return this.initialInterval * 1000
    },
    morethanone(){
      return this.sliders.length > 1
    }
  },
  mounted() {
    this.init()
  },
  methods:{
    init() {
      this.play()
      window.onblur = function() { this.stop() }.bind(this)
      window.onfocus = function() { this.play() }.bind(this)
    },
    move(offset, direction, speed) {
    //   console.log(speed)
      if (!this.transitionEnd) return
      this.transitionEnd = false
      direction === -1 ? this.currentIndex += offset/this.imgWidth : this.currentIndex -= offset/this.imgWidth
      if (this.currentIndex > this.sliders.length) this.currentIndex = 1
      if (this.currentIndex < 1) this.currentIndex = this.sliders.length
    //   console.log(this.currentIndex)
      const destination = this.distance + offset * direction
      this.animate(destination, direction, speed)
    },
    animate(des, direc, speed) {
      if (this.temp) {
        window.clearInterval(this.temp);
        this.temp = null ;
      }
      this.temp = window.setInterval(() => {
        if ((direc === -1 && des < this.distance) || (direc === 1 && des > this.distance)) {
          this.distance += speed * direc
        } else {
          this.transitionEnd = true
          window.clearInterval(this.temp)
          this.distance = des
          if (des < -1*(this.sliders.length * this.imgWidth)) this.distance = -1 * this.imgWidth
          if (des > -this.imgWidth) this.distance = -1*(this.sliders.length * this.imgWidth)
        }
      }, 20)
    },
    jump(index) {
      const direction = (index - this.currentIndex) >= 0 ? -1 : 1;
      const offset = Math.abs(index - this.currentIndex) * this.imgWidth;
      const jumpSpeed = Math.abs(index - this.currentIndex) === 0 ? this.speed : Math.abs(index - this.currentIndex) * this.speed ;
      this.move(offset, direction, jumpSpeed)
    },
    play() {
      if (this.timer) {
        window.clearInterval(this.timer)
        this.timer = null
      }
      this.timer = window.setInterval(() => {
        this.move(this.imgWidth, -1, this.speed)
      }, this.interval)
    },
    stop() {
      window.clearInterval(this.timer)
      this.timer = null
    }
  }
}
</script>

<style scoped>
  *{
    box-sizing: border-box;
    margin:0;
    padding:0;
  }
  ol,ul{
    list-style: none;
  }
  #slider{
    text-align: center;
  }
  .window{
    position:relative;
    /* width: imgWidth; */
    height:400px;
    margin:0 auto;
    overflow:hidden;
  }
  .container{
    display:flex;
    position:absolute;
  }
  .left, .right{
    position:absolute;
    top:50%;
    transform:translateY(-50%);
    width:50px;
    height:50px;
    background-color:rgba(0,0,0,.3);
    border-radius:50%;
    cursor:pointer;
  }
  .left{
    left:3%;
    padding-left:12px;
    padding-top:10px;
  }
  .right{
    right:3%;
    padding-right:12px;
    padding-top:10px;
  }
  img{
    user-select: none;
  }
  .dots{
    position:absolute;
    bottom:10px;
    left:50%;
    transform:translateX(-50%);
  }
  .dots li{
    display:inline-block;
    width:15px;
    height:15px;
    margin:0 3px;
    border:1px solid white;
    border-radius:50%;
    background-color:#333;
    cursor:pointer;
  }
  .dots .dotted{
    background-color:orange;
  }
</style>