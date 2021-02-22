<!--首页第一个页面-->

<template>
  <div id="home-head">
    <div class="left-text">
      <p class="bigtext">{{ $t("home.title3") }}</p>
      <p class="bigtext">{{ $t("home.title4") }}</p>
      <p class="bigtext bottom">
        {{ $t("home.title5") }}<span>{{ $t("home.title6") }}</span>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeHead"
};
</script>

<style scoped>
#home-head {
  width: var(--screen-width);
  height: var(--screen-height);
  background: url("~assets/img/bg/index1-bg.png") no-repeat top right;
}

.left-text {
  width: 600px;
  height: 400px;
  position: relative;
  margin-left: 15%;
  /* margin-left: 300px; */
  padding-top: 260px;
}

.left-text .bigtext {
  color: black;
}

.bottom {
  padding-top: 100px;
}

.bottom span {
  color: var(--theme-color);
}
</style>
