<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="login">
      <el-form :model="ruleForm" :rules="rules" v-show="nologin" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="Email" prop="email"><el-input class="input" v-model="ruleForm.email"></el-input></el-form-item>        
      <el-form-item label="密码" prop="password"><el-input class="input" type="password" v-model="ruleForm.password" auto-complete="off"></el-input></el-form-item>
			<el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
      </el-form>
      <a v-show="!nologin" @click="refresh">refresh token</a>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'

export default {
  name: 'Login',
  data(){
    return {
      msg: "Please login to get token.",
      regEmail: /^\w+@\w+(\.[a-zA-Z]{2,3}){1,2}$/,
      token: "",
      nologin: true,
      registerUrl: "https://phenomics.fudan.edu.cn/firmiana/API/logins/?",
      getUrl: "https://phenomics.fudan.edu.cn/firmiana/API/getToken/",
      updateUrl:"https://phenomics.fudan.edu.cn/firmiana/API/updateToken/",
      ruleForm:{
        email: '',
        password: '',
      },
      rules:{
				password: [{ required: true, trigger: 'blur' }],
        email: [{ required: true, validator: this.validateEmail, trigger: 'blur' }],
      },
    }
  },
  methods:{
    validateEmail(rule, value, callback){
			if (value === '') {
        callback(new Error('email is required.'));
			} else if (this.regEmail.test(value) === false) {
				callback(new Error('Format error.'));
			} else {
				callback();
			}
    },
    submitForm(formName){
      let that = this;
      this.$refs[formName].validate(valid => {
        if(valid){
          let params = new URLSearchParams();
          let dataform = {
            email: this.ruleForm["email"],
            password: this.ruleForm["password"],
          }
          for(let key of Object.keys(dataform)){
            params.append(key,dataform[key]);
          }
          Axios.post(this.registerUrl, params,
            {headers:{
              'Content-Type': 'application/x-www-form-urlencoded'
            }}
          )
          .then(function(response){
            console.log(response);
            let data = response.data;
            console.log(data);
            if(data["success"] === 1){
              that.nologin = false;
              that.getToken(that.getUrl);
            }
          })
          .catch(function (error){
            console.log(error);
          })
        }
      })
    },
    refresh(){
      console.log(1);
      this.getToken(this.updateUrl);
    },
    getToken(url){
      let that = this;
      this.msg = "Token:"
      Axios.get(url,
      // {
      //   withCredentials:true
      // },
        {headers:{
          'Content-Type': 'application/x-www-form-urlencoded'
        }}
      )
      .then(function(response){
        console.log(response);
        that.msg += response;
        that.token = response;
      })
      .catch(function (error){
        console.log(error)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  margin-left: 50px;
  color: #42b983;
  cursor: pointer;
}
.login{
  width: 400px;
  margin-left: 38%;
  padding-top: 60px;
}

</style>
