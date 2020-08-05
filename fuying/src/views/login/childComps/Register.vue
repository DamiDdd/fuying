//register组件
 
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
                <el-button class="verifyBtn" v-if="btnTitle" @click="btnClick" :disabled="btnDisabled">{{btnTitle}}</el-button>
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

export default {
    name: "Register",
    components: {
        Identify
    },
	data() {
		var validatePass = (rule, value, callback) => {
            var regPassword =  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{8,16}$/;
			if (value === '') {
                callback(new Error('请输入密码'));
                return false;
            } else if(regPassword.test(value) === false){
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
		};
 
		var validatePass2 = (rule, value, callback) => {
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
        };
        
         
		var validatePhone = (rule, value, callback) => {
            var regMobile=/^1\d{10}$/;
			if (value === '') {
                callback(new Error('请输入手机号'));
                return false;
			} else if (regMobile.test(value) === false) {
                callback(new Error('手机号输入有误'));
                return false;
			} else {
                callback();
                return true;
			}
        };
        
        var validateEmail = (rule, value, callback) => {
            var regEmail=/^\w+@\w+(\.[a-zA-Z]{2,3}){1,2}$/;
			if (value === '') {
                callback();
			} else if (regEmail.test(value) === false) {
				callback(new Error('电子邮箱输入有误'));
			} else {
				callback();
			}
        };
        
        var validateVerifycode = (rule, value, callback) => {
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
                // console.log(true);
                return true;
			}
        };

        var validatePhoneVC = (rule, value, callback) => {
			if (value === '') {
                callback(new Error('请输入验证码'));
            } else {
				callback();
			}
        };

        
        var validateName = (rule, value, callback) => {
			if (value === '') {
                callback(new Error('请输入用户名'));
            } else if(value.length < 2 || value.length > 5) {
				callback(new Error('长度在 2 到 5 个字符之间'));
            } else{
                callback();
            }
        };

		return {
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
                name: [{ required: true, validator: validateName, trigger: 'blur' }],
                phone: [{required: true, validator: validatePhone, trigger: 'blur'}],
				pass: [{ required: true, validator: validatePass, trigger: 'blur' }],
				checkPass: [{ required: true, validator: validatePass2, trigger: 'blur' }],
                email: [{ required: false, validator: validateEmail, trigger: 'blur' }],
                verifycode: [{ required: true, validator: validateVerifycode, trigger: 'blur' }],
                phoneVerifycode: [{required: true, validator: validatePhoneVC, trigger: 'blur'}]
			}
		};
	},
 
    mounted() {
        this.identifyCode = '';
        this.makeCode(this.identifyCodes, 4);
    },

	methods: {
        isReady(form,except){     
            for(let i in form){
                if(except && except.indexOf(i) !== -1) continue;
                if(!form[i]) return false;
            }
            return true;
        },

        random(min,max){
            return Math.floor(Math.random() * (max-min) + min);
        },

        refreshCode() {
            this.identifyCode = '';
            this.makeCode(this.identifyCodes,4);
        },

        makeCode(o,length) {
            for(let i = 0; i < length; i++){
                this.identifyCode += this.identifyCodes[this.random(0,this.identifyCodes.length)];
            }
        },

        // pending
        btnClick() {
            this.validateBtn();
        },

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

		submitForm(formName) {
			this.$refs[formName].validate(valid => {
				if (valid) {
					this.$message({
						type: 'success',
						message: '注册成功'
					});
					// this.activeName = 'first';
				} else {
					console.log('error submit!!');
					return false;
				}
			});
		},
 
		resetForm(formName) {
            this.$refs[formName].resetFields();
		}
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