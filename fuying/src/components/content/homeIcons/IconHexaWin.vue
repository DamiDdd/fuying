<!--六边形icon组，呈现错落效果-->

<template>
  <div id="icon-hexa-win">
    <IconHexagon class="left-up"><img src="~assets/img/home/enzyme.png" slot="img"><p class="content-blue" slot="text">酶</p></IconHexagon>
    <IconHexagon class="left-down"><img src="~assets/img/home/DNA.png" slot="img"><p class="content-blue" slot="text">DNA-结合</p></IconHexagon>
    <IconHexagon class="middle-up"><img src="~assets/img/home/kinase.png" slot="img"><p class="content-blue" slot="text">激酶</p></IconHexagon>
    <IconHexagon class="middle-down"><img src="~assets/img/home/antibody.png" slot="img"><p class="content-blue" slot="text">抗体</p></IconHexagon>
    <IconHexagon class="right"><img src="~assets/img/home/receptor.png" slot="img"><p class="content-blue" slot="text">受体</p></IconHexagon>
  </div>
</template>

<script>
import IconHexagon from 'common/icon/IconHexagon'

export default {
  name: "IconHexaWin",
  components: {
    IconHexagon
  }
}
</script>

<style scoped>
  #icon-hexa-win{
    display: flex;
    padding-top: 30px;
  }

  #icon-hexa-win div{
    display: flex;
  }
  
  .left-up{
    margin-left: 120px;
  }

  .left-down{
    margin-top: 200px;
    margin-left: -160px;
  }

  .middle-up{
    margin-top: 20px;
  }

  .middle-down{    
    margin-left: -140px;
    margin-top: 220px;
  }

  .right{
    margin-top: 100px;
  }

  .right img{
    margin-left: -30px;
    margin-top: 0px;
  }

  .right p{
    margin-left: -14px;
    margin-top: -5px;  }

</style>