// Login组件

<template>
<div id="login-win">
	<p class="login">
		<!-- <el-tabs v-model="activeName" @tab-click="handleClick"> -->
		<el-tabs v-model="activeName">
			<el-tab-pane label="登录" name="first">
				<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
					<el-form-item label="手机号" prop="phone"><el-input v-model="ruleForm.phone"></el-input></el-form-item>
					<el-form-item label="密码" prop="pass"><el-input type="password" v-model="ruleForm.pass" auto-complete="off"></el-input></el-form-item>
					<el-form-item>
						<el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
						<el-button @click="resetForm('ruleForm')">重置</el-button>
					</el-form-item>
				</el-form>
			</el-tab-pane>
			<el-tab-pane label="注册" name="second">
				<register></register>
			</el-tab-pane>
		</el-tabs>
	</p>
</div>
</template>
 
<script>
import Register from 'views/login/childComps/Register';
import Axios from 'axios'
 
export default {
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

		var validatePhone = (rule, value, callback) => {
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
        };
 
		return {
			activeName: 'first',
			regMobile: /^1\d{10}$/,
			loginUrl: "https://phenomics.fudan.edu.cn/firmiana/healthprogram/WebLogin/",
			ruleForm: {
				phone: '',
				pass: '',
				checkPass: ''
			},
			rules: {
				phone: [{required: true, validator: validatePhone, trigger: 'blur'}],
				pass: [{ required: true, validator: validatePass, trigger: 'blur' }]
			}
		};
	},
 
	methods: {
		//选项卡切换
		// handleClick(tab, event) {},
		//重置表单
		resetForm(formName) {
			this.$refs[formName].resetFields();
		},
		//提交表单
		submitForm(formName) {
			// console.log(this.$store.state.isLogin);
			this.$refs[formName].validate(valid => {
				if (valid) {
					var url = this.loginUrl + "?phone=" + this.ruleForm["phone"] + "&password="+this.ruleForm["pass"];
					console.log(url);
					Axios.get(url).then((response) => {
						console.log(response);
						if(response.status === 200){
							// console.log(response.data)
							let data = response.data;
							if(data["success"]){
								this.$message({
									type: 'success',
									message: '登陆成功'
								});
								this.$store.dispatch("setUser",true);
								console.log(this.$store.state.isLogin);
								// 本地存储登录信息
								localStorage.setItem("userPhone",this.ruleForm["phone"]);
								this.$router.push("/home");
							}
							else{
								if(!data["registered"]){
									this.$message({
										type: 'warning',
										message: '手机号未注册'
									});
								}
								else if(data["msg"] === "Wrong Password"){
									this.$message({
										type: 'warning',
										message: '密码错误'
									});
								}
							}
						}
					}).catch((error)=>{
						console.log(error);
					})
				} else {
					console.log('error submit!!');
					return false;
				}
			});
		}
	},
	components: {
		Register
	}
};
</script>
 
<style scoped>
#login-win{
	width: var(--screen-width);
	height: 700px;
	background: url("~assets/img/bg/index1-bg.png") no-repeat top right;
}

.login {
	width: 400px;
	padding-top: 40px;
	margin: 0 300px;
}
 
.el-tabsitem {
	text-align: center;
	width: 60px;
}
</style>