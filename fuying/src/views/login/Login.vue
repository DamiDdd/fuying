<!--Login组件-->

<template>
  <div class="homepage-hero-module">
    <div class="video-container">
      <div :style="fixStyle" class="filter"></div>
      <video
        :style="fixStyle"
        autoplay
        loop
        muted
        class="fillWidth"
        v-on:canplay="canplay"
      >
        <source src="~assets/img/video/Shanghai.mp4" type="video/mp4" />
        浏览器不支持 video 标签，建议升级浏览器。
        <!-- <source src="PATH_TO_WEBM" type="video/webm" />
        浏览器不支持 video 标签，建议升级浏览器。 -->
      </video>
      <div class="poster hidden" v-if="!vedioCanPlay">
        <img
          :style="fixStyle"
          src="~assets/img/bg/video-loading-bg.png"
          alt=""
        />
      </div>
      <div class="login-window">
        <el-tabs class="login-control" v-model="activeName">
          <el-tab-pane :label="$t('login.login')" name="first">
            <el-form
              :model="ruleForm"
              :rules="rules"
              ref="ruleForm"
              label-width="100px"
              class="demo-ruleForm"
            >
              <el-form-item :label="$t('public.phone')" prop="phone"
                ><el-input v-model="ruleForm.phone"></el-input
              ></el-form-item>
              <el-form-item :label="$t('public.password')" prop="pass"
                ><el-input
                  type="password"
                  v-model="ruleForm.pass"
                  auto-complete="off"
                ></el-input
              ></el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">{{
                  $t("login.login")
                }}</el-button>
                <el-button @click="resetForm('ruleForm')">{{
                  $t("login.reset")
                }}</el-button>
                <!-- <span class="after-text" @click="showScan">{{
                  $t("login.scan")
                }}</span> -->
                <span class="after-text" @click="forget">{{
                  $t("login.forgetpass")
                }}</span>
                <div id="weixin" v-show="scan">
                  <!-- <wxLogin></wxLogin> -->
                  <div>test</div>
                </div>
                <div id="temp" v-show="!scan">
                  <img src="~assets/img/bg/temp.jpg" />
                </div>
              </el-form-item>
            </el-form>
          </el-tab-pane>
          <!-- <el-tab-pane label="注册" name="second" :disabled=true> -->
          <el-tab-pane :label="$t('login.register')" name="second">
            <register></register>
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import Register from "views/login/childComps/Register";
import Axios from "axios";
import GLOBAL from "@/common/const";

export default {
  name: "Login",
  data() {
    return {
      vedioCanPlay: false,
      fixStyle: "",
      activeName: "first",
      regMobile: /^1\d{10}$/,
      loginUrl: GLOBAL.urlHead + "WebLogin/",
      scan: false,
      ruleForm: {
        phone: "",
        pass: ""
      },
      rules: {
        phone: [
          { required: true, validator: this.validatePhone, trigger: "blur" }
        ],
        pass: [
          { required: true, validator: this.validatePass, trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    canplay() {
      this.vedioCanPlay = true;
    },

    showScan() {
      this.scan = !this.scan;
    },

    forget() {
      this.$router.push("/forgetPass");
    },

    // 验证密码
    validatePass(rule, value, callback) {
      if (value === "") {
        callback(new Error(this.$t("tips.emptypassword")));
      } else {
        if (this.ruleForm.checkPass !== "") {
          this.$refs.ruleForm.validateField("checkPass");
        }
        callback();
      }
    },

    // 验证手机号
    validatePhone(rule, value, callback) {
      if (value === "") {
        callback(new Error(this.$t("tips.emptyphone")));
        return false;
      } else if (this.regMobile.test(value) === false) {
        callback(new Error(this.$t("tips.errorphone")));
        return false;
      } else {
        callback();
        return true;
      }
    },
    //选项卡切换,弃用
    // handleClick(tab, event) {},
    //重置表单
    resetForm(formName) {
      this.$refs[formName].resetFields();
      this.scan = false;
    },
    //提交表单
    submitForm(formName) {
      // console.log(this.$store.state.isLogin);
      this.$refs[formName].validate(valid => {
        if (valid) {
          var url =
            this.loginUrl +
            "?phone=" +
            this.ruleForm["phone"] +
            "&password=" +
            this.ruleForm["pass"];
          // console.log(url);
          Axios.get(url)
            .then(response => {
              // console.log(response);
              if (response.status === 200) {
                // console.log(response.data)
                let data = response.data;
                if (data["success"]) {
                  this.$message({
                    type: "success",
                    message: this.$t("tips.login") + this.ruleForm["phone"]
                  });
                  this.$store.dispatch("setUser", true);
                  // console.log(this.$store.state.isLogin);
                  // 本地存储登录信息
                  localStorage.setItem("userPhone", this.ruleForm["phone"]);
                  localStorage.setItem("userEmail", data["user_email"]);
                  localStorage.setItem("userName", data["user_name"]);
                  if (data["admin"]) {
                    this.$store.dispatch("setAdmin", true);
                    localStorage.setItem("admin", this.ruleForm["phone"]);
                  }
                  this.$router.push("/home");
                } else {
                  // 可以改进，后台直接返回汉语错误信息，前台通过msg展示即可
                  if (!data["registered"]) {
                    this.$message({
                      type: "warning",
                      message: this.$t("tips.notregister")
                    });
                  } else if (data["msg"] === "Wrong Password") {
                    this.$message({
                      type: "warning",
                      message: this.$t("tips.errorpassword")
                    });
                  }
                }
              }
            })
            .catch(error => {
              console.log(error);
            });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    }
  },
  mounted: function() {
    window.onresize = () => {
      const windowWidth = document.body.clientWidth;
      const windowHeight = document.body.clientHeight;
      const windowAspectRatio = windowHeight / windowWidth;
      let videoWidth;
      let videoHeight;
      if (windowAspectRatio < 0.5625) {
        videoWidth = windowWidth;
        videoHeight = videoWidth * 0.5625;
        this.fixStyle = {
          height: windowWidth * 0.5625 + "px",
          width: windowWidth + "px",
          "margin-bottom": (windowHeight - videoHeight) / 2 + "px",
          "margin-left": "initial"
        };
      } else {
        videoHeight = windowHeight;
        videoWidth = videoHeight / 0.5625;
        this.fixStyle = {
          height: windowHeight + "px",
          width: windowHeight / 0.5625 + "px",
          "margin-left": (windowWidth - videoWidth) / 2 + "px",
          "margin-bottom": "initial"
        };
      }
    };
    window.onresize();
  },
  components: {
    Register
    // WxLogin,
  }
};
</script>

<style scoped>
.homepage-hero-module,
.video-container {
  position: relative;
  height: 1100px;
  overflow: hidden;
  margin-bottom: -22px;
}

.video-container .poster img,
.video-container video {
  z-index: 0;
  position: absolute;
}

.video-container .filter {
  z-index: 1;
  position: absolute;
  background: rgba(0, 0, 0, 0.4);
}

.login-window {
  background: #fff;
  position: relative;
  width: 440px;
  height: 550px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 250px;
  z-index: 2;
  opacity: 80%;
}

.after-text {
  color: gray;
  padding-left: 4%;
}

.after-text:hover {
  color: lightblue;
  font-weight: bold;
  cursor: pointer;
}

.login-control {
  margin-left: 20px;
  width: 80%;
}

#temp img {
  margin-top: 30px;
  width: 200px;
}
</style>
