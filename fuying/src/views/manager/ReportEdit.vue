<!--管理员上传用户信息用于建表-->

<template>
  <div id="report-edit">
    <div id="report-div">
      <div class="main-div">
        <p style="text-align: center; line-height: 10px;">蛋白质组检测报告</p>
        <div class="profile-div">
          <div class="title-div-white"><p>用户信息</p></div>
          <div class="td-div">
            <div class="ss-div">姓名</div>
            <div class="m-div">
              <input type="text" v-model="dataForm.name" />
            </div>
            <div class="ss-div">性别</div>
            <div class="m-div">
              <select v-model="dataForm.sex">
                <option v-for="(i, index) in sex" :key="index">{{
                  i.label
                }}</option>
              </select>
            </div>
            <div class="ss-div">年龄</div>
            <div class="m-div">
              <input type="text" v-model="dataForm.age" />
            </div>
          </div>
          <div class="td-div-long">
            <textarea
              type="text"
              v-model="dataForm.health_history"
              placeholder="健康历史"
            ></textarea>
          </div>
          <div class="title-div-white"><p>样品信息</p></div>
          <div class="td-div">
            <div class="s-div">送样日期</div>
            <div class="m-div">
              <!-- <input type="text" v-model="dataForm.sample_date"> -->
              <el-date-picker
                class="picker"
                v-model="dataForm.sample_date"
                type="date"
                format="yyyy-MM-dd"
                value-format="yyyy-MM-dd"
                placeholder="选择日期时间"
              >
              </el-date-picker>
            </div>
            <div class="s-div">样品编号</div>
            <div class="m-div">
              <input type="text" v-model="dataForm.sample_num" />
            </div>
          </div>
          <div class="td-div">
            <div class="s-div">样品来源</div>
            <div class="m-div">
              <input type="text" v-model="dataForm.resource" />
            </div>
            <div class="s-div">样品类型</div>
            <div class="m-div">
              <input type="text" v-model="dataForm.type" />
            </div>
          </div>
          <div class="title-div-white"><p>检测信息</p></div>
          <div class="td-div">
            <div class="s-div">检测项目</div>
            <div class="l-div">
              <input type="text" v-model="dataForm.subject" />
            </div>
          </div>
          <div class="td-div">
            <div class="s-div">检测编号</div>
            <div class="l-div">
              <input type="text" v-model="dataForm.exp" />
            </div>
          </div>
          <div class="td-div">
            <div class="s-div">检测方法</div>
            <div class="l-div">
              <input type="text" v-model="dataForm.method" />
            </div>
          </div>
          <div class="title-div-white"><p>结果解读</p></div>
          <div class="td-div-long">
            <textarea type="text" v-model="dataForm.explanation"></textarea>
          </div>
          <div class="title-div-white"><p>细化检测结果</p></div>
          <div class="title-div"><p>一、实验室检测质控</p></div>
          <!-- <el-upload class="upload-demo" style="display: inline-block;" action="" :on-change="leading"
            :show-file-list="true" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel"
            :auto-upload="false">
            <el-button type="primary" icon="el-icon-upload" circle size="mini"></el-button>
          </el-upload> -->
          <table class="short-input" border="1">
            <tr>
              <th rowspan="2">血液样本</th>
              <th>全血总量(μL)</th>
              <th>血浆总量(μL)</th>
              <th>血浆颜色</th>
              <th>是否合格</th>
              <th>操作平台</th>
              <th>质控标准</th>
            </tr>
            <tr height="40">
              <td><input type="text" v-model="dataForm.total_blood" /></td>
              <td><input type="text" v-model="dataForm.total_plasma" /></td>
              <td><input type="text" v-model="dataForm.plasma_color" /></td>
              <!-- <td><input type="text" v-model="dataForm.qualify_1"></td> -->
              <td>
                <select v-model="dataForm.qualify_1">
                  <option v-for="(i, index) in judge" :key="index">{{
                    i.label
                  }}</option>
                </select>
              </td>
              <td><input type="text" v-model="dataForm.platform_1" /></td>
              <td><input type="text" v-model="dataForm.standard_1" /></td>
            </tr>
            <tr>
              <th rowspan="2">蛋白提取</th>
              <th>血浆上样量(μL)</th>
              <th>蛋白质量(μg)</th>
              <th>高丰度去除</th>
              <th>是否合格</th>
              <th>操作平台</th>
              <th>质控标准</th>
            </tr>
            <tr height="40">
              <td><input type="text" v-model="dataForm.plasma_sample" /></td>
              <td><input type="text" v-model="dataForm.protein_q" /></td>
              <td>
                <select v-model="dataForm.high_abundance_removal">
                  <option v-for="(i, index) in judge" :key="index">{{
                    i.label
                  }}</option>
                </select>
              </td>
              <td>
                <select v-model="dataForm.qualify_2">
                  <option v-for="(i, index) in judge" :key="index">{{
                    i.label
                  }}</option>
                </select>
              </td>
              <td><input type="text" v-model="dataForm.platform_2" /></td>
              <td><input type="text" v-model="dataForm.standard_2" /></td>
            </tr>
            <tr>
              <th rowspan="2">蛋白检测</th>
              <th>上样量(μg)</th>
              <th>蛋白鉴定量(μg)</th>
              <th>质量偏差</th>
              <th>是否合格</th>
              <th>操作平台</th>
              <th>质控标准</th>
            </tr>
            <tr height="40">
              <td><input type="text" v-model="dataForm.sample_amount" /></td>
              <td>
                <input
                  type="text"
                  v-model="dataForm.protein_identification_q"
                />
              </td>
              <td><input type="text" v-model="dataForm.bias" /></td>
              <td>
                <select v-model="dataForm.qualify_3">
                  <option v-for="(i, index) in judge" :key="index">{{
                    i.label
                  }}</option>
                </select>
              </td>
              <td><input type="text" v-model="dataForm.platform_3" /></td>
              <td><input type="text" v-model="dataForm.standard_3" /></td>
            </tr>
          </table>
        </div>
      </div>
      <div class="main-div">
        <div class="title-div"><p>二、质谱结果</p></div>
        <p>质谱图</p>
        <input
          class="upload-input"
          type="file"
          accept="image/gif,image/jpeg,image/jpg,image/png"
          @change="changeImage($event)"
          ref="avatarInput"
        />
        <img class="tech-img" :src="dataForm.mass_spectrogram_img" />
        <!-- <img src="~assets/img/report/temp/result.png" class="tech-img"> -->
        <p>
          <textarea
            type="text"
            v-model="dataForm.ms_text"
            placeholder="质谱分析"
          ></textarea>
        </p>
      </div>
    </div>
    <div class="btn-div">
      <el-button class="pdfBtn" @click="handleUpload">数据上传</el-button>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import GLOBAL from "@/common/const";

export default {
  name: "ReportEdit",
  components: {},
  data() {
    return {
      uploadurl: GLOBAL.urlHead2 + "update_report/",
      sex: [{ label: "男" }, { label: "女" }],
      judge: [{ label: "是" }, { label: "否" }],
      dataForm: {
        name: "",
        sex: "",
        age: "",
        health_history: "",
        // report_date: "",
        sample_date: "",
        sample_num: "",
        resource: "委托送检",
        type: "指尖血",
        subject: "全套餐",
        exp: "Exp000000",
        method: "次世代非数据依赖采集蛋白质组检测技术",
        explanation: "",
        // quality_report: "",
        mass_spectrogram_img: "",
        ms_text: "",
        total_blood: "",
        total_plasma: "",
        plasma_color: "淡黄色",
        qualify_1: "是",
        platform_1: "Thermo",
        standard_1: "血浆总量>5μL",
        plasma_sample: "",
        protein_q: "",
        high_abundance_removal: "是",
        qualify_2: "是",
        platform_2: "Thermo",
        standard_2: "蛋白质量>30μg",
        sample_amount: "",
        protein_identification_q: "",
        bias: "",
        qualify_3: "是",
        platform_3: "Thermo",
        standard_3: "蛋白测定量>2000个；质量偏差<5ppm"
      }
    };
  },
  mounted() {
    let date = new Date();
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let day = date.getDate();
    this.dataForm.sample_date = year + "-" + month + "-" + day;
  },
  methods: {
    // excel上传组件,停用
    leading(file) {
      // 导入
      this.importfxx(file.raw);
    },
    importfxx(obj) {
      //导入方法
      // 通过DOM取文件数据
      let rABS = false; //是否将文件读取为二进制字符串
      let f = obj;
      let reader = new FileReader();
      FileReader.prototype.readAsBinaryString = function(f) {
        let binary = "";
        let rABS = false; //是否将文件读取为二进制字符串
        let wb; //读取完成的数据
        let outdata;
        let reader = new FileReader();
        reader.onload = function() {
          let bytes = new Uint8Array(reader.result);
          let length = bytes.byteLength;
          for (let i = 0; i < length; i++) {
            binary += String.fromCharCode(bytes[i]);
          }
          let XLSX = require("xlsx");
          if (rABS) {
            wb = XLSX.read(btoa(binary), {
              //手动转化
              // wb = XLSX.read(btoa(fixdata(binary)), { //手动转化
              type: "base64"
            });
          } else {
            wb = XLSX.read(binary, {
              type: "binary"
            });
          }
          outdata = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]]); //outdata就是res
          console.log(outdata);
        };
        reader.readAsArrayBuffer(f);
      };
      if (rABS) {
        reader.readAsArrayBuffer(f);
      } else {
        reader.readAsBinaryString(f);
      }
    },

    // 上传数据接口
    handleUpload() {
      let that = this;
      // console.log(this.dataForm);
      // console.log(this.uploadurl);
      let params = new URLSearchParams();
      for (let key of Object.keys(this.dataForm)) {
        params.append(key, this.dataForm[key]);
      }
      Axios.post(this.uploadurl, params, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      })
        .then(function(response) {
          console.log(response);
          that.$message({
            type: "success",
            message: "上传成功"
          });
        })
        .catch(function(error) {
          console.log(error);
          that.$message({
            type: "warning",
            message: "请检查上传信息"
          });
        });
    },
    // 改变image
    changeImage(e) {
      var file = e.target.files[0];
      var reader = new FileReader();
      var that = this;
      reader.readAsDataURL(file);
      reader.onload = function() {
        that.dataForm.mass_spectrogram_img = this.result;
      };
    }
  }
};
</script>

<style scoped>
#report-div {
  width: var(--paper-width);
  margin-left: auto;
  margin-right: auto;
  padding-right: 10px;
}

.btn-div {
  width: 300px;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  padding-bottom: 10px;
}

.main-div {
  width: var(--paper-width);
  height: calc(var(--paper-height) + 1px);
  margin-bottom: 10.6px;
  overflow: hidden;
  border: 1px solid var(--theme-color);
}

.main-div p {
  margin-left: 30px;
  margin-right: 30px;
}

.logo-div {
  text-align: center;
}

.logo {
  width: 300px;
  margin-top: 50px;
  margin-bottom: 20px;
}

.logo-div .bigtext-blue {
  margin-bottom: 150px;
}

.main-text {
  text-indent: 2rem;
}

.product-div {
  line-height: 30px;
}

.tech-img {
  width: 550px;
  max-height: 500px;
  margin-left: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
}

.title-div {
  background: skyblue;
  height: 27px;
}

.title-div-white {
  background: var(--theme-color);
  color: white;
  height: 27px;
  text-align: center;
}

.title-div p,
.title-div-white p {
  margin-top: 0;
}

.profile-div {
  border: 1px solid var(--theme-color);
  width: 580px;
  height: 790px;
  margin-left: 4px;
}

.td-div {
  height: 30px;
  border: 0.1px solid #000;
  display: flex;
}

.td-div-long {
  height: 80px;
  border: 0.1px solid #000;
  text-indent: 2rem;
  padding-top: 10px;
}

.td-div-long textarea {
  height: 60px;
}

.s-div,
.ss-div,
.m-div {
  text-align: center;
}
.s-div,
.ss-div {
  background: skyblue;
  border: 0.1px solid gray;
}
.ss-div {
  width: 50px;
}
.s-div {
  width: 80px;
}
.m-div {
  width: 200px;
  font-weight: bold;
}
.l-div {
  width: 400px;
}

input {
  width: 150px;
  border: none;
  margin-top: 2px;
}

textarea {
  width: 520px;
  border: none;
  height: 80px;
}

.l-div input {
  width: 400px;
}

.upload-input {
  width: 400px;
  padding-left: 20px;
}

.upload-demo {
  padding-left: 20px;
  padding-top: 10px;
}

.short-input input {
  width: 76px;
}

.picker {
  width: 200px;
  /* height: 10px; */
  font-size: 10px;
  margin-top: -10px;
}
</style>
