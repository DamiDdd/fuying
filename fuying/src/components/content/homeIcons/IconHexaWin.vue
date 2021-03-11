<!--六边形icon组，呈现错落效果-->

<template>
  <div id="icon-hexa-win">
    <IconHexagon class="left-up"
      ><img src="~assets/img/home/enzyme.png" slot="img" />
      <p class="content-blue" slot="text">
        {{ $t("home.enzyme") }}
      </p></IconHexagon
    >
    <IconHexagon class="left-down"
      ><img src="~assets/img/home/DNA.png" slot="img" />
      <p class="content-blue" slot="text">{{ $t("home.DNA") }}</p></IconHexagon
    >
    <IconHexagon class="middle-up"
      ><img src="~assets/img/home/kinase.png" slot="img" />
      <p class="content-blue" slot="text">
        {{ $t("home.kinase") }}
      </p></IconHexagon
    >
    <IconHexagon class="middle-down"
      ><img src="~assets/img/home/antibody.png" slot="img" />
      <p class="content-blue" slot="text">
        {{ $t("home.antibody") }}
      </p></IconHexagon
    >
    <IconHexagon class="right"
      ><img src="~assets/img/home/receptor.png" slot="img" />
      <p class="content-blue" slot="text">
        {{ $t("home.receptor") }}
      </p></IconHexagon
    >
  </div>
</template>

<script>
import IconHexagon from "common/icon/IconHexagon";

export default {
  name: "IconHexaWin",
  components: {
    IconHexagon
  }
};
</script>

<style scoped>
#icon-hexa-win {
  display: flex;
  padding-top: 1.875rem /* 30/16 */;
}

#icon-hexa-win div {
  display: flex;
}

.left-up {
  margin-left: 7.5rem /* 120/16 */;
}

.left-down {
  margin-top: 12.5rem /* 200/16 */;
  margin-left: -10rem /* 160/16 */;
}

.middle-up {
  margin-top: 1.25rem /* 20/16 */;
}

.middle-down {
  margin-left: -8.75rem /* 140/16 */;
  margin-top: 13.75rem /* 220/16 */;
}

.right {
  margin-top: 6.25rem /* 100/16 */;
}

.right img {
  margin-left: -1.875rem /* 30/16 */;
  margin-top: 0rem /* 0/16 */;
}

.right p {
  margin-left: -.875rem /* 14/16 */;
  margin-top: -.3125rem /* 5/16 */;
}
</style>
