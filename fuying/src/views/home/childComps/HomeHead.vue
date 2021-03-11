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
  width: 37.5rem /* 600/16 */;
  height: 25rem /* 400/16 */;
  position: relative;
  margin-left: 15%;
  padding-top: 16.25rem /* 260/16 */;
}

.left-text .bigtext {
  color: black;
}

.bottom {
  padding-top: 6.25rem /* 100/16 */;
}

.bottom span {
  color: var(--theme-color);
}
</style>
