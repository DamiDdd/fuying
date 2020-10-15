<template>
<div class="main">
  <div class="top"></div>
  <div class="register">
	<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
    <el-form-item label="Company" prop="company">
      <el-select class="input" v-model="ruleForm.company" placeholder="Your Company" filterable>
        <el-option v-for="item in all_company" :key="item.company" :value="item.company"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="Laboratory" prop="laboratory">
      <el-select class="input" v-model="ruleForm.laboratory" placeholder="Your Laboratory" filterable>
        <el-option v-for="item in all_lab" :key="item.lab" :value="item.lab"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="Name" prop="stuffName"><el-input class="input" v-model="ruleForm.stuffName"></el-input></el-form-item>
    <el-form-item label="Email" prop="email"><el-input class="input" v-model="ruleForm.email"></el-input></el-form-item>        
		<el-form-item label="密码" prop="password"><el-input class="input" type="password" v-model="ruleForm.password" auto-complete="off"></el-input></el-form-item>
		<el-form-item label="重复密码" prop="checkPass"><el-input class="input" type="password" v-model="ruleForm.checkPass" auto-complete="off"></el-input></el-form-item>
		<el-form-item>
			<el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
			<el-button @click="resetForm('ruleForm')">重置</el-button>
		</el-form-item>
	</el-form>
  </div>
</div>
</template>

<script>
import Axios from 'axios'

export default {
  name: 'Register',
  data(){
    return{
      regPassword: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{8,16}$/,
      regEmail: /^\w+@\w+(\.[a-zA-Z]{2,3}){1,2}$/,
      globalUrl:"https://phenomics.fudan.edu.cn/firmiana/experiments/ajax/",
      registerUrl: "https://phenomics.fudan.edu.cn/firmiana/register/",
      all_company:[],
      all_lab:[],
      last_choice: '',
      ruleForm:{
        company: '',
        laboratory: '',
        stuffName: '',
        email: '',
        password: '',
        checkPass: '',
      },
      rules:{
        company: [{required: true, validator: this.changeCompany, trigger: ['change']}],
        laboratory: [{required: true, validator: this.changeLab, trigger: ['change']}],
        stuffName: [{required: true, validator: this.validateName, trigger: 'blur'}],
				password: [{ required: true, validator: this.validatePass, trigger: 'blur' }],
				checkPass: [{ required: true, validator: this.validatePass2, trigger: 'blur' }],
        email: [{ required: true, validator: this.validateEmail, trigger: 'blur' }],
      },
      dataForm:{
        company: '',
        lab: '',
        stuffName: '',
        email: '',
        password: '',
      }
    }
  },
  methods:{
    changeCompany(rule, value, callback){
      if(this.ruleForm.company === ''){
        callback(new Error('请选择'));
        return false;
      }
      else if(this.last_choice !== value){
        this.last_choice = value;
        Axios.get(this.globalUrl+"all_lab/?id="+value).then((response) => {
          if(response.status === 200){
            this.all_lab = response.data.all_lab;
            this.ruleForm.laboratory = '';
          }
        });
        callback();
        return true;
      }
      else{
        callback();
        return true;
      }
    },

    changeLab(rule, value, callback){
      if(value === ''){
        callback(new Error("请选择"));
        return false;
      }
      else{
        callback();
        return true;
      }
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
			} else if (value !== this.ruleForm.password) {
        callback(new Error('两次输入密码不一致!'));
        return false;
			} else {
        callback();
        return true;
			}
    },

    validateName(rule,value,callback){
			if (value === '') {
        callback(new Error('请输入用户名'));
      } else{
        callback();
      }
    },

    validateEmail(rule, value, callback){
			if (value === '') {
        callback(new Error('请输入电子邮箱'));
			} else if (this.regEmail.test(value) === false) {
				callback(new Error('电子邮箱输入有误'));
			} else {
				callback();
			}
    },

    // 重置表单
		resetForm(formName) {
      this.all_lab = [];
      this.$refs[formName].resetFields();
    },

    submitForm(formName){
      this.$refs[formName].validate(valid => {
        if(valid){
          this.pack();
          let params = new URLSearchParams();
          for(let key of Object.keys(this.dataForm)){
            params.append(key,this.dataForm[key]);
          }
          console.log(this.dataForm);
          Axios.post(this.registerUrl, params,
            {headers:{
              'Content-Type': 'application/x-www-form-urlencoded'
            }}
          )
          .then(function(response){
            console.log(response);
          })
          .catch(function (error){
            console.log(error);
          })
        }
      })
    },

    pack(){
      this.dataForm['company'] = this.ruleForm['company'];
      this.dataForm['lab'] = this.ruleForm['laboratory'];
      this.dataForm['stuffName'] = this.ruleForm['stuffName'];
      this.dataForm['email'] = this.ruleForm['email'];
      this.dataForm['password'] = this.ruleForm['password'];
    }
  },

  mounted(){
    Axios.get(this.globalUrl+"all_company/").then((response) => {
      if(response.status === 200){
        this.all_company = response.data.all_company;
        this.$delete(this.all_company,0);
      }
    })
  },
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.register{
  width: 80%;
  min-width: 400px;
  padding-left: 20%;
  padding-top: 2%;
  padding-bottom: 2%;
  font-weight: bold;
}

.input{
  width: 20%;
  min-width: 400px;
}

.main{
	width: 100%;
	height: 969px;
  background: url("../assets/img/index1-bg.png") no-repeat top right;
  background-size: 100%;
}

.logo{
  margin-left: 100px;
  margin-top: 10px;
}

.top{
  height: 200px;
  width: 100%;
}
</style>
