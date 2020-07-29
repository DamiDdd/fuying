<template>
  <div id="home-menu">
    <p class="title">复瑛健康——探索人类健康的专家</p>
    <p class="content">选择复瑛，我们将会定期给你发送检测报告，实时监测您的健康状态。根据蛋白信息为您定制更系统的生活方案。让肌体保持青春，让生活更加舒适。</p>
    <div>
      <icon></icon>
    </div>
  </div>
</template>

<script>
import Icon from 'common/icon/Icon'

export default {
  name: "HomeMenu",
  components: {
    Icon,
  }
}
</script>

<style scoped>
  #home-menu{
    width: var(--screen-width);
    text-align: center;
  }
</style>