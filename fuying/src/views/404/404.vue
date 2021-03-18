<!--Login组件-->

<template>
  <div class="homepage-hero-module">
    <div class="video-container">
      <video
        :style="fixStyle"
        autoplay
        loop
        muted
        class="fillWidth"
        v-on:canplay="canplay"
      >
        <source src="~assets/img/video/background.mp4" type="video/mp4" />
        浏览器不支持 video 标签，建议升级浏览器。
        <!-- <source src="PATH_TO_WEBM" type="video/webm" />
        浏览器不支持 video 标签，建议升级浏览器。 -->
      </video>
      <div class="poster hidden" v-if="!vedioCanPlay">
        <img
          :style="fixStyle"
          src="~assets/img/bg/video-loading-bg.jpg"
          alt=""
        />
      </div>
      <div class="window">
        <p>404 not found</p>
        <el-divider></el-divider>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "notfound",
  data() {
    return {
      vedioCanPlay: false,
      scan: false,
      fixStyle: ""
    };
  },
  methods: {
    canplay() {
      this.vedioCanPlay = true;
    },

    showScan() {
      this.scan = !this.scan;
    },

    forget() {
      this.$router.push("/forgetPass");
    }
  },
  mounted: function() {
    window.onresize = () => {
      const windowWidth = document.body.clientWidth;
      const windowHeight = document.body.clientHeight;
      const windowAspectRatio = windowHeight / windowWidth;
      let videoWidth;
      let videoHeight;
      if (windowAspectRatio < 0.5625) {
        videoWidth = windowWidth;
        videoHeight = videoWidth * 0.5625;
        this.fixStyle = {
          height: windowWidth * 0.5625 + "px",
          width: windowWidth + "px",
          "margin-bottom": (windowHeight - videoHeight) / 2 + "px",
          "margin-left": "initial"
        };
      } else {
        videoHeight = windowHeight;
        videoWidth = videoHeight / 0.5625;
        this.fixStyle = {
          height: windowHeight + "px",
          width: windowHeight / 0.5625 + "px",
          "margin-left": (windowWidth - videoWidth) / 2 + "px",
          "margin-bottom": "initial"
        };
      }
    };
    window.onresize();
  }
};
</script>

<style scoped>
.homepage-hero-module,
.video-container {
  position: relative;
  min-width: 62.5rem /* 1000/16 */;
  height: 68.75rem /* 1100/16 */;
  overflow: hidden;
  margin-bottom: -1.375rem /* 22/16 */;
}

.video-container .poster img,
.video-container video {
  z-index: 0;
  position: absolute;
}

.video-container .filter {
  z-index: 1;
  position: absolute;
  background: rgba(0, 0, 0, 0.4);
}

.window {
  background: #fff;
  position: relative;
  width: 27.5rem /* 440/16 */;
  height: 10rem;
  margin-left: auto;
  margin-right: auto;
  margin-top: 30rem;
  z-index: 2;
  opacity: 0.8;
  color: black;
}

.window p {
  font-size: 2.5rem;
  line-height: 2rem;
  padding-top: 2rem;
  margin-left: 1rem;
}
</style>
