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
            } else if(regPassword.test(value) === false){
                callback(new Error('8-16个字符，至少1个大写字母、1个小写字母、1个数字'));
            } 
            else {
				if (this.ruleForm.checkPass !== '') {
					this.$refs.ruleForm.validateField('checkPass');
				}
				callback();
			}
		};
 
		var validatePass2 = (rule, value, callback) => {
			if (value === '') {
				callback(new Error('请再次输入密码'));
			} else if (value !== this.ruleForm.pass) {
				callback(new Error('两次输入密码不一致!'));
			} else {
				callback();
			}
        };
        
         
		var validatePhone = (rule, value, callback) => {
            var regMobile=/^1\d{10}$/;
			if (value === '') {
				callback(new Error('请输入手机号'));
			} else if (regMobile.test(value) === false) {
				callback(new Error('手机号输入有误'));
			} else {
				callback();
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
			} else if (val !== idcodeStr) {
				callback(new Error('验证码不正确'));
			} else {
				callback();
			}
        };

		return {
            activeName: 'second',
            identifyCodes: '1234567890ABCDEFGHIGKLMNoPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
            identifyCode: '',
			ruleForm: {
                name: '',
                phone: '',
				pass: '',
                checkPass: '',
                email: '',
                verifycode: ''
			},
			rules: {
                name: [{ required: true, message: '请输入您的名称', trigger: 'blur' }, { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }],
                phone: [{required: true, validator: validatePhone, trigger: 'blur'}],
				pass: [{ required: true, validator: validatePass, trigger: 'blur' }],
				checkPass: [{ required: true, validator: validatePass2, trigger: 'blur' }],
                email: [{ required: false, validator: validateEmail, trigger: 'blur' }],
                verifycode: [{ required: true, validator: validateVerifycode, trigger: 'blur' }]
			}
		};
	},
 
    mounted() {
        this.identifyCode = '';
        this.makeCode(this.identifyCodes, 4);
    },

	methods: {
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

		submitForm(formName) {
			this.$refs[formName].validate(valid => {
				if (valid) {
					this.$message({
						type: 'success',
						message: '注册成功'
					});
					// this.activeName: 'first',
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
        /* display: flex; */
        float: right;
        width: 110px;
        height: 40px;
        overflow: hidden;
        background: gray;
    }
</style>