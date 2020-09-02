<template>
  <div id="report">
    <div class="btn-div">
      <el-button class="pdfBtn" @click="handleDownload">PDF下载</el-button>
    </div>
    <div id="report-div">
      <div class="main-div logo-div">
        <img class="logo" src="~assets/img/report/logo.png">
        <p class="bigtext-blue">蛋白质组学生理刻画<br>检测报告</p>
        <p class="smalltext">检测编号: {{number}}</p>
        <p class="smalltext">报告日期: {{date}}</p>
      </div>
      <div class="main-div">
        <p class="bigtext-blue">致受检者书</p>
        <p class="content">尊敬的 {{name}} 女士/先生</p>
        <p class="content">您好！</p>
        <p class="main-text">
          复瑛健康（上海复瑛生物科技有限公司）是生命健康领域的新兴企业，坚持自主创新和成果转化，立足新一代蛋白质
          组技术，基于数据驱动、健康评估的检测服务公司，旨在将生命科学、临床医学及数据挖掘等创新技术融为一体，推
          出全新的健康评估模式服务于人类健康。</p>
        <p class="main-text">
          蛋白质组学生理刻画产品是利用次世代蛋白质组技术配合机器学习的大数据精准分型，1滴指尖血为样本可获得2000+
          蛋白质检测指标，涵盖100+项生理功能，完成40+大类的生理刻画，检测数据量为常规体检的近百倍，提供更加完备的
          个人全景生理刻画。
        </p>
        <p class="main-text">
          在此我们也特别提醒您注意：受检者委托复瑛健康开展蛋白质组学生理刻画检测服务，系基于受检者生理功能相关评估结
          果，预测无明显症状的受检者是否存在生理状态不佳的情况，该检测不是一种诊断过程，而是一种简便快速的评估方法，
          以便提高客户的生活质量。检测结果不作为临床诊断和治疗的依据。
        </p>
        <p class="main-text">
          本检测的意义在于通过较完备的个人全景式生理刻画，助您掌握健康状态，希望您对此给予充分的理解与信任，我们愿意
          与您一同积极面对可能出现的结果。由于技术发展的局限性，个体间存在的生物学差异等原因，本报告仅对本次送检样本负责。
        </p>
        <p class="main-text">
          希望您能将您的宝贵意见与建议及时反馈给我们。我们免费的服务电话是{{phone}}（工作日，8:30-17:30），我们将竭诚
          为您服务！祝您健康！
        </p>
        <p class="main-text">此致</p>
        <p class="main-text" style="text-indent: 0;">敬礼!</p>
        <p class="main-text" style="text-align: right;">上海复瑛生物科技有限公司</p>
      </div>
      <div class="main-div product-div">
        <p class="bigtext-blue">产品简介</p>
        <p class="main-text">蛋白质作为生命活动的执行者，直接反映着一个个体的生理、病理
          情况。随着人类基因组计划的实施和推进，生命科学研究已进入了后基因组时代。蛋白质组
          研究是后基因组时代生命科学研究的核心内容之一。蛋白质组学以细胞内全部蛋白质及其活
          动方式为研究对象。在早期诊断、疾病预防、分型、判断预后等诸多方面都具有巨大的潜力。
        </p>
        <p class="main-text">现阶段，本检测平台总原始数据量达到1G；谱图数达到10万张，肽段
          数达到5.000个以上，检测体液样本的蛋白质鉴定数可达2,000种以上。
        </p>
        <p class="main-text">根据上万组正常人蛋白质组数据，建立基准数据训练集。通过机器学
          习将蛋白质组数据同临床表型进行管理关联，建立包含一百种特征的训练模型。将用户样本
          进行蛋白质组分析后与训练集比对，可对样本进行分类或分型，并据此提供较为可靠的临床辅助结论。
        </p>
      </div>
      <div class="main-div">
        <p class="content-blue"  style="margin-bottom: 40px;">技术路线</p>
        <img class="tech-img" src="~assets/img/report/rout.png">
        <p class="content-blue" style="margin-bottom: 40px;">技术原理</p>
        <img class="tech-img" src="~assets/img/report/principle.png">
      </div>
      <div class="main-div">
        <p style="text-align: center; line-height: 10px;">蛋白质组检测报告</p>
        <div class="profile-div">
          <div class="title-div-white"><p>用户信息</p></div>
          <div class="td-div">
            <div class="ss-div">姓名</div>
            <div class="m-div">{{name}}</div>
            <div class="ss-div">性别</div>
            <div class="m-div">{{sex}}</div>
            <div class="ss-div">年龄</div>            
            <div class="m-div">{{age}}</div>
          </div>
          <div class="td-div-long">
            病史或临床表现：（用户填写）
          </div>
          <div class="title-div-white"><p>样品信息</p></div>
          <div class="td-div">          
            <div class="s-div">送样日期</div>
            <div class="m-div">{{sendDate}}</div>
            <div class="s-div">样品编号</div>
            <div class="m-div">{{sampleNumber}}</div>
          </div>
          <div class="td-div">          
            <div class="s-div">样品来源</div>
            <div class="m-div">{{resource}}</div>
            <div class="s-div">样品类型</div>
            <div class="m-div">{{type}}</div>
          </div>
          <div class="title-div-white"><p>检测信息</p></div>
          <div class="td-div">
            <div class="s-div">检测项目</div>
            <div class="l-div">{{subject}}</div>            
          </div>
          <div class="td-div">            
            <div class="s-div">检测编号</div>
            <div class="l-div">{{number}}</div>  
          </div>
          <div class="td-div">          
            <div class="s-div">检测方法</div>
            <div class="l-div">{{way}}</div>
          </div>
          <div class="title-div-white"><p>结果解读</p></div>
          <div class="td-div-long">{{explanation}}</div>
          <div class="title-div-white"><p>细化检测结果</p></div>
          <div class="title-div"><p>一、实验室检测质控</p></div>

        </div>
      </div>
      <div class="main-div">
        <div class="title-div"><p>二、质谱结果</p></div>
        <p>质谱图</p>
        <img class="tech-img" :src="resultImg">
        <!-- <img src="~assets/img/report/temp/result.png" class="tech-img"> -->
        <p>数据采集量1.5 G，谱图数81,220张，蛋白质鉴定总数2408。</p>
      </div>
      <div class="main-div table-div">
        <div class="title-div"><p>三、生理刻画结果</p></div>
        <table-paper><span slot="title">基础套餐评估结果</span></table-paper>
      </div>
      <img-paper>
        <p slot="title1">1.1.1 生理年龄指数</p>
        <img src="~assets/img/report/temp/1.1.1.png" slot="img1">
        <p slot="text1">您的生理年龄指数预测结果为36.60,极高于您的口述年龄，
          您比同龄人整体更操劳，需注意日常保养，适当锻炼。</p>
        <p slot="title2">1.2.1 内脏脂肪率指数</p>
        <img src="~assets/img/report/temp/1.2.1.png" slot="img2">
        <p slot="text2">您的内脏脂肪率指数在万人队列中的位比为92.79%，处在极
          高位区，表示您的内脏脂肪率指数水平高于92.79%的人群，需注意日常生活及
          饮食情况，根据自身需求进行相应调整。若感不适请及时就医</p>
      </img-paper>
      <img-paper>
        <p slot="title1">1.2.2 身体脂肪率指数</p>
        <img src="~assets/img/report/temp/1.2.2.png" slot="img1">
        <p slot="text1">您的身体脂肪率指数在万人队列中的位比为36.35%，处在正
          常位区，表示您的身体脂肪率指数水平低于63.65%的人群，您的状态正常，请继续保持。</p>
        <p slot="title2">1.3.1 丙氨酸氨基转移酶指数</p>
        <img src="~assets/img/report/temp/1.3.1.png" slot="img2">
        <p slot="text2">您的丙氨酸氨基转移酶指数在万人队列中的位比为52.73%，处在正常位区，
          表示您的丙氨酸氨基转移酶指数水平低于47.27%的人群，您的状态正常，请继续保持。</p>
      </img-paper>
      <img-paper>
        <p slot="title1">1.3.2 天冬氨酸氨基转移酶指数</p>
        <img src="~assets/img/report/temp/1.3.2.png" slot="img1">
        <p slot="text1">您的天冬氨酸氨基转移酶指数在万人队列中的位比为69.69%，处在正常位区，
          表示您的天冬氨酸氨基转移酶指数水平低于30.31%的人群，您的状态正常，请继续保持。</p>
      </img-paper>
    </div>
  </div>
</template>

<script>
import ImgPaper from 'common/report/ImgPaper';
import DownloadPDF from '@/common/downloadPDF';
import TablePaper from 'common/report/TablePaper';

export default {
  name: "Report",
  components: {
    ImgPaper,
    TablePaper
  },
  data(){
    return{
      number: "",
      name: "",
      date: "",
      phone: "",
      sex: "",
      age: "",
      sendDate: "",
      sampleNumber: "",
      resource: "",
      type: "",
      subject: "",
      way: "",
      explanation: "",
      resultImg: "", 
    }
  },
  mounted(){
    this.number = "123";
    this.name = "???";
    this.date = "??/??/??";
    this.phone = "???????";
    this.sex = "男";
    this.age = "22";
    this.sendDate = "??/??";
    this.sampleNumber = "??????";
    this.resource = "???";
    this.type = "???";
    this.subject = "???";
    this.way = "???";
    this.explanation = "......";
    this.resultImg = require('../../assets/img/report/temp/result.png');
  },
  methods: {
    handleDownload(){
      DownloadPDF.downloadPDF(document.querySelector('#report-div'),'user-report');
    },
  }
}
</script>

<style scoped>
  #report-div{
    width: var(--paper-width);
    margin-left: auto;
    margin-right: auto;
    padding-right: 10px;
  }

  .btn-div{
    width: 300px;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
    padding-bottom: 10px;
  }

  .main-div{
    width: var(--paper-width);
    height: calc(var(--paper-height) + 1px);
    margin-bottom: 10.6px;
    overflow: hidden;
    border: 1px solid var(--theme-color);
  }

  .main-div p{
    margin-left: 30px;
    margin-right: 30px;
  }

  .logo-div{
    text-align: center;
  }

  .logo{
    width: 300px;
    margin-top: 50px;
    margin-bottom: 20px;
  }

  .logo-div .bigtext-blue{
    margin-bottom: 150px;
  }
  
  .main-text{
    text-indent: 2rem;
  }

  .product-div{
    line-height: 30px;
  }

  .tech-img{
    width: 550px;
    margin-left: 20px;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .title-div{
    background: skyblue;
    height: 27px;
  }

  .title-div-white{
    background: var(--theme-color);
    color: white;
    height: 27px;
    text-align: center;
  }

  .title-div p, .title-div-white p{
    margin-top: 0;
  }

  .profile-div{
    border: 1px solid var(--theme-color);
    width:580px;
    height: 790px;
    margin-left: 4px;
  }

  .td-div{
    height: 30px;
    border: 0.1px solid #000;
    display: flex;
  }

  .td-div-long{
    height: 60px;
    border: 0.1px solid #000;
    text-indent: 2rem;
    padding-top: 10px;
  }

  .s-div, .ss-div, .m-div{
    text-align: center;
  }
  .s-div, .ss-div{
    background: skyblue;
    border: 0.1px solid gray;
  }
  .ss-div{
    width:50px;
  }
  .s-div{
    width: 80px;
  }
  .m-div{
    width: 200px;
    font-weight: bold;
  }
  .l-div{
    width: 400px;
  }
</style>