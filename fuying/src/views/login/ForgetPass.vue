<template>
  <div id="fp-win">
    <div class="main">
      <el-steps :active="step" class="step">
          <el-step title="手机号"></el-step>
          <el-step title="验证码"></el-step>
          <el-step title="重置"></el-step>
          <el-step title="结果查询"></el-step>
      </el-steps>
      <el-tabs v-model="activeNames[step]">
        <el-tab-pane label="" name="first" :disabled="true">
            <div class="windows">
                <span class="right-text">请输入注册时的手机号：</span><el-input v-model="phone" class="input"></el-input>						
                <el-button type="primary" @click="submitPhone" :disabled="phoneCheck">验证</el-button>
            </div>
        </el-tab-pane>
        <el-tab-pane label="" name="second" :disabled="true">
            <div class="windows">
                <span class="right-text">请输入图片验证码：</span>
                <el-input v-model="icodeInput" auto-complete="off" class="identifyinput"></el-input>        
                <div class="identifybox" @click="refreshCode">
                    <identify :identifyCode="identifyCode"></identify>
                </div>
                <el-button type="primary" @click="getVerify" :disabled="icodeCheck" class="left-btn">验证</el-button>
            </div>
        </el-tab-pane>
        <el-tab-pane label="" name="third" :disabled="true">
            <div class="windows">
				<el-form :model="ruleForm" :rules="rules" ref="ruleForm" class="demo-ruleForm" label-width="200px">
					<el-form-item label="请输入手机上的验证码" prop="phoneVerifycode"><el-input v-model="ruleForm.phoneVerifycode"></el-input></el-form-item>
					<el-form-item label="输入新的密码" prop="pass"><el-input type="password" v-model="ruleForm.pass"></el-input></el-form-item>
					<el-form-item label="重复密码" prop="checkPass"><el-input type="password" v-model="ruleForm.checkPass"></el-input></el-form-item>
				</el-form>							
                <el-button type="primary" @click="submitForm('ruleForm')" class="bottom-btn">提交</el-button>
            </div>
        </el-tab-pane>
        <el-tab-pane label="" name="fourth" :disabled="true">
            <div class="windows">
                <p class="content-blue">{{msg}}</p>
            </div>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
import GLOBAL from '@/common/const'
import Identify from 'common/identify/Identify'
import Axios from 'axios'


export default {
    name: "ForgetPass",
    components: {
        Identify
    },
    data(){
        return{
            step: 0,
            activeNames: ["first","second","third","fourth"],
            validateUrl: GLOBAL.urlHead+"sendPasswordValidateCode/",
            resetUrl: GLOBAL.urlHead+"resetPassword/",
            phone: "",
            regMobile: /^1\d{10}$/,
            regPassword: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{8,16}$/,
            identifyCodes: '1234567890ABCDEFGHIGKLMNoPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
            identifyCode: '',
            icodeInput: '',
            ruleForm: {
				pass: '',
                checkPass: '',
                phoneVerifycode: '',
            },
			rules: {
				pass: [{ required: true, validator: this.validatePass, trigger: 'blur' }],
				checkPass: [{ required: true, validator: this.validatePass2, trigger: 'blur' }],
                phoneVerifycode: [{required: true, validator: this.validatePhoneVC, trigger: 'blur'}]
            },
            msg: "修改密码成功！4s后为您跳转至登录页",
        }
    },
    mounted() {
        this.identifyCode = '';
        this.makeCode(this.identifyCodes, 4);
    },
    computed:{
        phoneCheck(){
            if(this.phone === ""){
                return true;
            }
            else if(this.regMobile.test(this.phone) === false){
                return true;
            }
            else{
                return false;
            }
        },
        icodeCheck(){
            let val = this.icodeInput.toLowerCase();
            let idcodeStr = this.identifyCode.toLowerCase();
            return val !== idcodeStr;
        }
    },
    methods:{
        submitPhone(){
            console.log(this.phone);
			this.step++;
        },
        // 随机数
        random(min,max){
            return Math.floor(Math.random() * (max-min) + min);
        },

        // 刷新函数
        refreshCode() {
            this.identifyCode = '';
            this.makeCode(this.identifyCodes,4);
        },

        // 制作验证码(的数值部分)
        makeCode(o,length) {
            for(let i = 0; i < length; i++){
                this.identifyCode += this.identifyCodes[this.random(0,this.identifyCodes.length)];
            }
        },
        
        // 获取验证码
        getVerify(){
            let that = this;
            var url = this.validateUrl + "?phone=" + this.phone;
            Axios.get(url).then((response) =>{
                // console.log(response);
                if(response.status === 200){
                    that.step++;
                    that.$message({
						type: 'success',
						message: '短信验证码已经发送至'+that.phone,
                    });
                }
            }).catch((error) => {
                console.log(error);
            })
        },
        
        // 验证密码合理性
        validatePass(rule, value, callback){
			if (value === '') {
                callback(new Error('请输入密码'));
                return false;
            } else if(this.regPassword.test(value) === false){
                callback(new Error('8-16个字符，至少1个大写字母、1个小写字母、1个数字'));
                return false;
            } 
            else {
				if (this.ruleForm.checkPass !== '') {
					this.$refs.ruleForm.validateField('checkPass');
                }
                callback();
                return true;
			}
		},
 
         // 验证再次输入密码合理性
		validatePass2(rule, value, callback){
			if (value === '') {
                callback(new Error('请再次输入密码'));
                return false;
			} else if (value !== this.ruleForm.pass) {
                callback(new Error('两次输入密码不一致!'));
                return false;
			} else {
                callback();
                return true;
			}
        },

        // 手机验证码合理性
        validatePhoneVC(rule, value, callback){
			if (value === '') {
                callback(new Error('请输入验证码'));
            } else {
				callback();
			}
        },

        
        // 控制时延
        jumpControl() {
            let time = 3;
            let timer = setInterval(() => {
                if(time == 0) {
                    clearInterval(timer);
                    this.$router.push({path: '/login'});
                } else {
                    this.msg = "修改密码成功！" +  time + '秒后为您跳转至登录页';
                    time--;
                }
            },1000)
        },

         // 提交修改密码表单 
		submitForm(formName) {
			this.$refs[formName].validate(valid => {
				if (valid) {
                    let that = this;
                    // console.log(this.ruleForm);
                    // 数据封装成后台可解析dict
                    let params = new URLSearchParams();
                    params.append("phone",this.phone);
                    params.append("password",this.ruleForm["pass"]);
                    params.append("validatecode",this.ruleForm["phoneVerifycode"]);
                    Axios.post(this.resetUrl, params,
                        {headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        }}
                    )
                    .then(function(response){
                        // console.log(response);
                        if(response.status === 200){
                            let data = response.data;
                            console.log(data);
                            // 异常保护
                            that.step++;
                            if(data['success'] === true)
                            {
                                that.jumpControl();
                            }
                            else{
                                that.msg = data['msg'] + "！请刷新重试";
                            }
                        }
                        else{
                            that.$message({
                                type: 'warning',
                                message: '后台错误',
                            });
                        }
                    })
                    .catch(function (error){
                        console.log(error);
                    });             
                }
            });
        },
    }
}
</script>

<style scoped>
#fp-win{
	width: var(--screen-width);
	min-width: var(--min-width);
	height: 700px;
	background: url("~assets/img/bg/index1-bg.png") no-repeat top right;
}
.main {
	width: 600px;
	padding-top: 40px;
	margin: 0 10%;
}
.step{
    z-index: 1;
    height: 20px;
}
.windows{
    margin-top: 50px;
}
.right-text{
    float: left;
    margin-top: 10px;
}
.input{
    width: 200px;
}
.identifyinput{
    float: left;
    width: 120px;
}
.identifybox{
    width: 113px;
    height: 40px;
    overflow: hidden;
}
.left-btn{
    float: right;
    margin-top: -40px;
    margin-right: 100px;
}
.bottom-btn{
    float: right;
    margin-right: 20px;
}
</style>