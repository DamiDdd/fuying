<!--管理员上传用户信息用于建表-->

<template>
  <div id="report-edit">
    <div class="btn-div">
      <el-button class="pdfBtn" @click="handleUpload">数据上传</el-button>
    </div>
    <div id="report-div">
      <div class="main-div">
        <p style="text-align: center; line-height: 10px;">蛋白质组检测报告</p>
        <div class="profile-div">
          <div class="title-div-white"><p>用户信息</p></div>
          <div class="td-div">
            <div class="ss-div">姓名</div>
            <div class="m-div"><input type="text" v-model="dataForm.name"></div>
            <div class="ss-div">性别</div>
            <div class="m-div"><input type="text" v-model="dataForm.sex"></div>
            <div class="ss-div">年龄</div>            
            <div class="m-div"><input type="text" v-model="dataForm.age"></div>
          </div>
          <div class="td-div-long">
            <textarea type="text" v-model="dataForm.headlth_history"></textarea>
          </div>
          <div class="title-div-white"><p>样品信息</p></div>
          <div class="td-div">          
            <div class="s-div">送样日期</div>
            <div class="m-div"><input type="text" v-model="dataForm.sample_date"></div>
            <div class="s-div">样品编号</div>
            <div class="m-div"><input type="text" v-model="dataForm.sample_num"></div>
          </div>
          <div class="td-div">          
            <div class="s-div">样品来源</div>
            <div class="m-div"><input type="text" v-model="dataForm.resource"></div>
            <div class="s-div">样品类型</div>
            <div class="m-div"><input type="text" v-model="dataForm.type"></div>
          </div>
          <div class="title-div-white"><p>检测信息</p></div>
          <div class="td-div">
            <div class="s-div">检测项目</div>
            <div class="l-div"><input type="text" v-model="dataForm.subject"></div>            
          </div>
          <div class="td-div">            
            <div class="s-div">检测编号</div>
            <div class="l-div"><input type="text" v-model="dataForm.test_num"></div>  
          </div>
          <div class="td-div">          
            <div class="s-div">检测方法</div>
            <div class="l-div"><input type="text" v-model="dataForm.method"></div>
          </div>
          <div class="title-div-white"><p>结果解读</p></div>
          <div class="td-div-long"><textarea type="text" v-model="dataForm.explanation"></textarea></div>
          <div class="title-div-white"><p>细化检测结果</p></div>
          <div class="title-div"><p>一、实验室检测质控</p></div>
          <el-upload class="upload-demo" style="display: inline-block;" action="" :on-change="leading"
            :show-file-list="true" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel"
            :auto-upload="false">
            <el-button type="primary" icon="el-icon-upload" circle size="mini"></el-button>
          </el-upload>
        </div>
      </div>
      <div class="main-div">
        <div class="title-div"><p>二、质谱结果</p></div>
        <p>质谱图</p>
        <input class="upload-input" type="file" accept="image/gif,image/jpeg,image/jpg,image/png" @change="changeImage($event)" ref="avatarInput">
        <img class="tech-img" :src="dataForm.mass_spectrogram_img">
        <!-- <img src="~assets/img/report/temp/result.png" class="tech-img"> -->
        <p><textarea type="text" v-model="dataForm.ms_text"></textarea></p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "ReportEdit",
  components: {
  },
  data(){
    return{
      dataForm: {
        name: "",
        sex: "",
        age: "",
        headlth_history: "",
        report_date: "",
        sample_date: "",
        sample_num: "",
        resource: "",
        type: "",
        subject: "",
        test_num: "",
        method: "",
        explanation: "",
        // quality_report: "",
        mass_spectrogram_img: "",
        ms_text: "",
      },
    }
  },
  mounted(){
    //   init,waiting for modifying
    this.dataForm.name = "陈周";
    this.dataForm.sex = "男";
    this.dataForm.age = "32";
    this.dataForm.headlth_history = "病史或临床表现：（用户填写）";
    this.dataForm.report_date = "2020/07/29";
    this.dataForm.sample_date = "2020/07/20";
    this.dataForm.sample_num = "abc1234";
    this.dataForm.resource = "委托送检";
    this.dataForm.type = "手指血";
    this.dataForm.subject = "全套餐";
    this.dataForm.test_num = "Exp079824";
    this.dataForm.method = "次世代非数据依赖采集蛋白质组检测技术"
    this.dataForm.explanation = "（结果解读）本次检测结果，您的内脏脂肪、总胆固醇、少数代谢功能指数以及个别免疫功能指数存在明显异常，建议您在日常生活中注意健康饮食结构，适当进行运动，预防疾病的发生。若有不适请及时就医";
    this.dataForm.mass_spectrogram_img = require('../../assets/img/report/temp/result.png');
    this.dataForm.ms_text = "数据采集量1.5 G，谱图数81,220张，蛋白质鉴定总数2408。";
  },
  methods: {
    // 这个excel上传组件我还没弄明白，待查
    leading(file) { // 导入
      this.importfxx(file.raw)
    },
    importfxx(obj) { //导入方法
      // 通过DOM取文件数据
      // let _this = this
      let rABS = false; //是否将文件读取为二进制字符串
      let f = obj
      let reader = new FileReader();
      FileReader.prototype.readAsBinaryString = function(f) {
        let binary = "";
        let rABS = false; //是否将文件读取为二进制字符串
        // let pt = this;
        let wb; //读取完成的数据
        let outdata;
        let reader = new FileReader();
        reader.onload = function() {
          let bytes = new Uint8Array(reader.result);
          let length = bytes.byteLength;
          for (let i = 0; i < length; i++) {
          binary += String.fromCharCode(bytes[i]);
          }
          let XLSX = require('xlsx');
          if (rABS) {
            wb = XLSX.read(btoa(binary), { //手动转化
            // wb = XLSX.read(btoa(fixdata(binary)), { //手动转化
              type: 'base64'
            });
          } else {
            wb = XLSX.read(binary, {
              type: 'binary'
            });
          }
          outdata = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]]); //outdata就是res
          console.log(outdata)
        }
        reader.readAsArrayBuffer(f);
      }
      if (rABS) {
        reader.readAsArrayBuffer(f);
      } else {
        reader.readAsBinaryString(f);
      }
    },

    handleUpload(){
      console.log(this.dataForm.mass_spectrogram_img);
    },
    changeImage(e) {
      var file = e.target.files[0]
      var reader = new FileReader()
      var that = this
      reader.readAsDataURL(file)
      reader.onload = function() {
        that.dataForm.mass_spectrogram_img = this.result
      }
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
    max-height: 500px;
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
    height: 100px;
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

  input{
    width: 150px;
    border: none;
    margin-top: 2px;;
  }

  textarea{
    width: 520px;
    border: none;
    height: 80px;
  }

  .l-div input{
    width: 400px;
  }

  .upload-input{
    width: 400px;
    padding-left: 20px;
  }

  .upload-demo{
    padding-left: 20px;
    padding-top: 10px;
  }
</style>