<template>
  <div id="products">
    <button @click="handleDownload">PDF下载</button>
    <div id="report-div">
    <img-paper>
      <p slot="title1">1.1.1 生理年龄指数</p>
      <img src="~assets/img/temp/1.1.1.png" slot="img1">
      <p slot="text1">您的生理年龄指数预测结果为36.60,极高于您的口述年龄，
        您比同龄人整体更操劳，需注意日常保养，适当锻炼。</p>
      <p slot="title2">1.2.1 内脏脂肪率指数</p>
      <img src="~assets/img/temp/1.2.1.png" slot="img2">
      <p slot="text2">您的内脏脂肪率指数在万人队列中的位比为92.79%，处在极
        高位区，表示您的内脏脂肪率指数水平高于92.79%的人群，需注意日常生活及
        饮食情况，根据自身需求进行相应调整。若感不适请及时就医</p>
    </img-paper>
    <img-paper>
      <p slot="title1">1.2.2 身体脂肪率指数</p>
      <img src="~assets/img/temp/1.2.2.png" slot="img1">
      <p slot="text1">您的身体脂肪率指数在万人队列中的位比为36.35%，处在正
        常位区，表示您的身体脂肪率指数水平低于63.65%的人群，您的状态正常，请继续保持。</p>
      <p slot="title2">1.3.1 丙氨酸氨基转移酶指数</p>
      <img src="~assets/img/temp/1.3.1.png" slot="img2">
      <p slot="text2">您的丙氨酸氨基转移酶指数在万人队列中的位比为52.73%，处在正常位区，
        表示您的丙氨酸氨基转移酶指数水平低于47.27%的人群，您的状态正常，请继续保持。</p>
    </img-paper>
    <img-paper>
      <p slot="title1">1.3.2 天冬氨酸氨基转移酶指数</p>
      <img src="~assets/img/temp/1.3.2.png" slot="img1">
      <p slot="text1">您的天冬氨酸氨基转移酶指数在万人队列中的位比为69.69%，处在正常位区，
        表示您的天冬氨酸氨基转移酶指数水平低于30.31%的人群，您的状态正常，请继续保持。</p>
    </img-paper>
    </div>
  </div>
</template>

<script>
import ImgPaper from 'common/report/ImgPaper';
import downloadPDF from '@/common/downloadPDF';

export default {
  name: "Products",
  components: {
    ImgPaper,
  },
  methods: {
    handleDownload(){
      downloadPDF.downloadPDF(document.querySelector('#report-div'),'user-report');
    }
  }
}
</script>

<style scoped>
  #products{
    min-height:500px;
  }
</style>