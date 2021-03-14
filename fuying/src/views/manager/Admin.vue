<template>
  <div>
    <div class="nav-bg"></div>
    <div class="menu">
      <div class="btn-window" @click="jump('/reportEdit')">
        <div class="icon">
          <img src="~assets/img/common/microscope.png" alt="" />
          <h3>上传报告</h3>
        </div>
      </div>
      <div class="btn-window" @click="jump('/manager')">
        <div class="icon">
          <img src="~assets/img/common/find.png" alt="" />
          <h3>报告查询</h3>
        </div>
      </div>
      <div class="btn-window" @click="jump('/uploadGood')">
        <div class="icon">
          <img src="~assets/img/common/cart.png" alt="" />
          <h3>上架商品</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Admin",
  methods: {
    jump(path) {
      this.$router.push({ path: path });
    }
  }
};
</script>

<style scoped>
.nav-bg {
  width: 100%;
  min-width: 75rem /* 1200/16 */;
  height: 12.5rem /* 200/16 */;
  background: -webkit-linear-gradient(top, white, black);
}
.menu {
  margin-top: 0rem /* 0/16 */;
  width: 100%;
  min-width: 65rem /* 1000/16 */;
  height: 56.25rem /* 900/16 */;
  background: url("~assets/img/bg/intro-bg.jpg") no-repeat center;
  background-size: cover;
}

.btn-window {
  width: 33.1%;
  /* min-width: calc(25%-1rem); */
  height: 100%;
  float: left;
  background: #000;
  opacity: 0.8;
  border: 0.0625rem /* 1/16 */ solid white;
  color: white;
  cursor: pointer;
}

.icon {
  width: 13.75rem /* 220/16 */;
  height: 13.75rem /* 220/16 */;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20rem /* 320/16 */;
}

.icon img {
  height: 12.5rem /* 200/16 */;
  width: 12.5rem /* 200/16 */;
  margin-left: 0.625rem /* 10/16 */;
}

.icon h3 {
  padding-left: 3.5rem /* 20/16 */;
}

.btn-window:hover {
  opacity: 0.6;
}
</style>
