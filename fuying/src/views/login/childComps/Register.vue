//register组件
 
<template>
	<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
		<el-form-item label="用户名" prop="name"><el-input v-model="ruleForm.name"></el-input></el-form-item>
        <el-form-item label="手机号" prop="phone"><el-input v-model="ruleForm.phone"></el-input></el-form-item>
        <el-form-item label="电子邮箱" prop="email"><el-input v-model="ruleForm.email"></el-input></el-form-item>        
		<el-form-item label="密码" prop="pass"><el-input type="password" v-model="ruleForm.pass" auto-complete="off"></el-input></el-form-item>
		<el-form-item label="确认密码" prop="checkPass"><el-input type="password" v-model="ruleForm.checkPass" auto-complete="off"></el-input></el-form-item>
		<el-form-item>
			<el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
			<el-button @click="resetForm('ruleForm')">重置</el-button>
		</el-form-item>
	</el-form>
</template>
 
<script>
export default {
    name: "Register",
	data() {
		var validatePass = (rule, value, callback) => {
			if (value === '') {
				callback(new Error('请输入密码'));
			} else {
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
 
		return {
			activeName: 'second',
			ruleForm: {
                name: '',
                phone: '',
				pass: '',
                checkPass: '',
                email: '',
			},
			rules: {
                name: [{ required: true, message: '请输入您的名称', trigger: 'blur' }, { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }],
                phone: [{required: true, validator: validatePhone, trigger: 'blur'}],
				pass: [{ required: true, validator: validatePass, trigger: 'blur' }],
				checkPass: [{ required: true, validator: validatePass2, trigger: 'blur' }],
				email: [{ required: false, validator: validateEmail, trigger: 'blur' }]
			}
		};
	},
 
	methods: {
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