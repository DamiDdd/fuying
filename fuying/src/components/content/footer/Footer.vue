<template>
  <div class="background-box">
    <vue-particles
      color="#fff"
      :particleOpacity="0.7"
      :particlesNumber="60"
      shapeType="circle"
      :particleSize="4"
      linesColor="#fff"
      :linesWidth="1"
      :lineLinked="true"
      :lineOpacity="0.4"
      :linesDistance="150"
      :moveSpeed="2"
      :hoverEffect="true"
      hoverMode="grab"
      :clickEffect="false"
      clickMode="push"
    >
    </vue-particles>
    <div class="center">
      <h5>
        <el-divider></el-divider>
        公安备案号100000000 ICP备10000000号 网文〔2021〕1000-1000号<br />
        版权信息版权信息版权信息版权信息版权信息版权信息<br />
        ©1999-2021复旦大学 版权与免责声明 版权申诉<br />
      </h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style>
#particles-js {
  width: 100%;
  height: 100%;
  position: absolute;
}

.background-box {
  width: 100%;
  min-width: 1000px;
  height: 200px;
  background: #000;
  position: relative;
}

.center {
  /* background: #fff; */
  text-align: center;
  height: 150px;
  width: 1000px;
  margin-left: auto;
  margin-right: auto;
  color: white;
  opacity: 60%;
}
.center h5 {
  padding-top: 80px;
}
</style>
