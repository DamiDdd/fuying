<!--register组件-->
 
<template>
	<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
		<el-form-item label="用户名" prop="name"><el-input v-model="ruleForm.name"></el-input></el-form-item>
        <el-form-item label="手机号" prop="phone"><el-input v-model="ruleForm.phone"></el-input></el-form-item>
        <el-form-item label="电子邮箱" prop="email"><el-input v-model="ruleForm.email"></el-input></el-form-item>        
		<el-form-item label="密码" prop="pass"><el-input type="password" v-model="ruleForm.pass" auto-complete="off"></el-input></el-form-item>
		<el-form-item label="确认密码" prop="checkPass"><el-input type="password" v-model="ruleForm.checkPass" auto-complete="off"></el-input></el-form-item>
		<el-form-item label="图片验证码" prop="verifycode">
            <el-input v-model="ruleForm.verifycode" auto-complete="off" class="identifyinput">
            </el-input>
            <div  class="identifybox" @click="refreshCode">
                <identify :identifyCode="identifyCode"></identify>
            </div>
        </el-form-item>
        <el-form-item v-show="isReady(ruleForm,['email','phoneVerifycode'])" label="短信验证码" prop="phoneVerifycode">
            <el-input v-model="ruleForm.phoneVerifycode" auto-complete="off" class="identifyinput">
            </el-input>
            <div class="identifybox">
                <el-button class="verifyBtn" v-if="btnTitle" @click="btnClick(ruleForm.phone)" :disabled="btnDisabled">{{btnTitle}}</el-button>
            </div>
        </el-form-item>
		<el-form-item>
			<el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
			<el-button @click="resetForm('ruleForm')">重置</el-button>
		</el-form-item>
	</el-form>
</template>
 
<script>
import Identify from 'common/identify/Identify'
// 待修改
import Axios from 'axios'
import GLOBAL from '@/common/const'


export default {
    name: "Register",
    components: {
        Identify
    },
	data() {
		return {
            regPassword: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{8,16}$/,
            regEmail: /^\w+@\w+(\.[a-zA-Z]{2,3}){1,2}$/,
            regMobile: /^1\d{10}$/,
            phoneUrl: GLOBAL.urlHead+"sendValidateCode/?phone=",
            registerUrl: GLOBAL.urlHead+"register/",
            activeName: 'second',
            identifyCodes: '1234567890ABCDEFGHIGKLMNoPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
            identifyCode: '',
            btnDisabled: false,
            btnTitle: "获得验证码",
			ruleForm: {
                name: '',
                phone: '',
				pass: '',
                checkPass: '',
                email: '',
                verifycode: '',
                phoneVerifycode: '',
            },
			rules: {
                name: [{ required: true, validator: this.validateName, trigger: 'blur' }],
                phone: [{required: true, validator: this.validatePhone, trigger: 'blur'}],
				pass: [{ required: true, validator: this.validatePass, trigger: 'blur' }],
				checkPass: [{ required: true, validator: this.validatePass2, trigger: 'blur' }],
                email: [{ required: false, validator: this.validateEmail, trigger: 'blur' }],
                verifycode: [{ required: true, validator: this.validateVerifycode, trigger: 'blur' }],
                phoneVerifycode: [{required: true, validator: this.validatePhoneVC, trigger: 'blur'}]
            },
            dataForm: {
                name: 'pending',
                phone: '',
                mail: '',
                openID: 'newUser',
                validatecode: '',
                password: '',
                userName: '',
            }
		};
	},
 
    mounted() {
        this.identifyCode = '';
        this.makeCode(this.identifyCodes, 4);
    },

	methods: {
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
        
        // 验证手机号合理性
		validatePhone(rule, value, callback){
			if (value === '') {
                callback(new Error('请输入手机号'));
                return false;
			} else if (this.regMobile.test(value) === false) {
                callback(new Error('手机号输入有误'));
                return false;
			} else {
                callback();
                return true;
			}
        },
        
        // 验证电子邮箱合理性
        validateEmail(rule, value, callback){
			if (value === '') {
                callback();
			} else if (this.regEmail.test(value) === false) {
				callback(new Error('电子邮箱输入有误'));
			} else {
				callback();
			}
        },

        // 验证码合理性
        validateVerifycode(rule, value, callback){
            let val = value.toLowerCase();
            let idcodeStr = this.identifyCode.toLowerCase();
			if (value === '') {
                callback(new Error('请输入验证码'));
                return false;
			} else if (val !== idcodeStr) {
                callback(new Error('验证码不正确'));
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

        // 用户名合理性
        validateName(rule, value, callback){
			if (value === '') {
                callback(new Error('请输入用户名'));
            } else if(value.length < 2 || value.length > 5) {
				callback(new Error('长度在 2 到 5 个字符之间'));
            } else{
                callback();
            }
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

        // 处理获取验证码按钮点击事件
        btnClick(phone) {
            this.validateBtn();
            this.getPhoneVariftcode(phone);
        },

        // 获取验证码
        getPhoneVariftcode(phone) {
            var url = this.phoneUrl + phone;
            Axios.get(url).then((response) =>{
                console.log(response);
            }).catch((error) => {
                console.log(error);
            })
        },

        // 控制时延
        validateBtn() {
            let time = 60;
            let timer = setInterval(() => {
                if(time == 0) {
                    clearInterval(timer);
                    this.btnDisabled = false;
                    this.btnTitle = "获取验证码";
                } else {
                    this.btnTitle = time + '秒后重试';
                    this.btnDisabled = true;
                    time--;
                }
            },1000)
        },

        // 提交注册表单 
		submitForm(formName) {
			this.$refs[formName].validate(valid => {
				if (valid) {
                    let that = this
                    this.packDataForm();
                    // console.log(this.dataForm);
                    // 数据封装成后台可解析dict
                    let params = new URLSearchParams();
                    for(let key of Object.keys(this.dataForm)){
                        params.append(key,this.dataForm[key]);
                    }
                    Axios.post(this.registerUrl, params,
                        {headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        }}
                    )
                    .then(function(response){
                        console.log(response);
                        if(response.status === 200){
							let data = response.data;
							if(data["success"]){
								that.$message({
									type: 'success',
									message: '注册成功,请登录'
                                });
                                // 自动登录代码因为接口不返回是否为管理员，暂时停用，需手动登录
								// that.$store.dispatch("setUser",true);
								// // 本地存储登录信息
								// localStorage.setItem("userPhone",that.ruleForm["phone"]);
							}
							else{
								if(data["msg"] === "验证码错误"){
									that.$message({
										type: 'warning',
										message: '验证码错误'
									});
                                }
                                else if(data["msg"] === "此手机号已注册"){
									that.$message({
										type: 'warning',
										message: that.ruleForm["phone"]+'已注册'
									});
								}
							}
						}
                    })
                    .catch(function (error){
                        console.log(error);
                    });

					// this.$message({
					// 	type: 'success',
					// 	message: '注册成功'
                    // });
                    
					// this.activeName = 'first';
				} else {
					console.log('error submit!!');
					return false;
				}
			});
        },
        
        // 打包数据
        packDataForm() {
            this.dataForm['userName'] = this.ruleForm['name'];
            this.dataForm['phone'] = this.ruleForm['phone'];
            this.dataForm['mail'] = this.ruleForm['email'];
            this.dataForm['validatecode'] = this.ruleForm['phoneVerifycode'];
            this.dataForm['password'] = this.ruleForm['pass'];
            // console.log(this.dataForm);
        },
 
        // 重置表单
		resetForm(formName) {
            this.$refs[formName].resetFields();
            this.refreshCode();
        },

        // 控制手机验证码是否显示的函数
        isReady(form,except){
            for(let i in form){
                if(except && except.indexOf(i) !== -1) continue;
                if(!form[i]) return false;
            }
            if(form['verifycode'].toLowerCase() !== this.identifyCode.toLowerCase()){
                return false;
            }
            if(this.regMobile.test(form['phone']) === false){
                return false;
            }
            return true;
        },
	}
};
</script>

<style scoped> 
    .identifyinput{
        width: 120px;
    }
    .identifybox{
        float: right;
        width: 113px;
        height: 40px;
        overflow: hidden;
        /* background: gray; */
    }
</style>