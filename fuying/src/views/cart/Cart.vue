<!--购物车页面-->

<template>
  <div id="cart">
    <p class="title">我的购物车</p>
    <div class="tips" v-if="!emptyCart">
      <div class="flag"><input type="checkbox" v-model="all" @click="chooseAll"> 全选</div>
      <div class="img"></div>
      <div class="title1">套餐</div>
      <div class="title2">服务内容</div>
      <div class="price-single">单价</div>
      <div class="num-control">数目</div>
      <div class="price-sum">总价</div>
      <div class="delete"></div>
    </div>
    <div v-for="(item,index) in goods" :key="index">
      <cart-view :good="goods[index]"></cart-view>
    </div>
    <div class="tips" v-if="!emptyCart">
      <div class="price-tag">总价：</div>
      <div class="price">{{sum}}</div>
      <button id="purchase" @click="submitPurchase">结算</button>
    </div>
    <div v-if="emptyCart" class="empty" @click="jump2mall">您的购物车空空如也,去商城看看吧！</div>
    <modal :show="modal" :title="titleM" v-on:hideModal="hideModal" v-on:submit="solveMsg">
      <div class="in-content">
        <table class="el-table el-table--fit el-table--border table-detail">
          <thead>
            <tr>
              <th width="200px">套餐</th>
              <th width="200px">服务内容</th>
              <th width="200px">单价</th>
              <th width="200px">数目</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item,index) in goods" :key="index" v-show="item.flag">
              <td v-text="item.product"></td>
              <td v-text="item.detail"></td>
              <td v-text="item.price"></td>
              <td v-text="item.num"></td>
            </tr>
            <tr>
              <td colspan="4" v-text="'总价：'+this.sum" class="sp"></td>
            </tr>
          </tbody>
        </table>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="姓名" prop="user_name"><el-input v-model="ruleForm.user_name"></el-input></el-form-item>
          <el-form-item label="手机号" prop="user_phone"><el-input v-model="ruleForm.user_phone"></el-input></el-form-item>
          <el-form-item label="地址" prop="user_address"><el-input v-model="ruleForm.user_address"></el-input></el-form-item>
        </el-form>  
      </div>
    </modal>
  </div>
</template>

<script>
import CartView from 'components/content/cart/CartView'
import Modal from 'components/common/modal/Modal'
import GLOBAL from '@/common/const'
import Axios from 'axios'

export default {
  name: 'Cart',
  inject: ['reload'],
  components:{
    CartView,
    Modal,
  },
  computed:{
    // 判断是否为空购物车
    emptyCart(){
      let sign = true;
      if(this.goods.length == 0){
        return sign;
      }
      else{
        this.goods.forEach(element => {
          if(element.num > 0){
            sign = false;
          }
        });
      }
      return sign;
    },
    // 求选中的总价
    sum(){
      let sum = 0;
      sum = parseFloat(sum);
      this.goods.forEach(element => {
        if(element.flag){
          sum = parseFloat(sum + parseFloat(element.priceSum));
        }
      });
      return sum.toFixed(2);
    }
  },
  data(){
    return{
      phone: localStorage.getItem("userPhone"),
      carturl: GLOBAL.urlHead+"getCartweb/",
      uploadUrl: GLOBAL.urlHead+"payCartWeb/",
      all: false,
      modal: false,
      titleM: "完善您的订单信息",
      goods:[
        // 数据样例
        // {
        //   product_id: "00001",
        //   product: "生理刻画基本套餐",
        //   detail_id: "2",
        //   detail: "升级版",
        //   product_img: lab,
        //   price: 200,
        //   num: 1,
        // },
      ],
      ruleForm: {
        user_name: '',
        user_phone: localStorage.getItem("userPhone"),
				user_address: '',
      },
			rules: {
        user_name: [{ required: true, validator: this.validateName, trigger: 'blur' }],
        user_phone: [{required: true, validator: this.validatePhone, trigger: 'blur'}],
				user_address: [{ required: true, validator: this.validateAddress, trigger: 'blur' }],
      },
      dataForm: {
        id: '',
        user_name: '',
        user_phone: '',
        user_address: '',
        pay_list: [],
        tot_num: 0,
      }
    }
  },
  mounted(){
    // 在这里拿到cart数据
    this.carturl +=  "?id=" + this.phone;
    Axios.get(this.carturl).then((response) => {
      if(response.status === 200){
        let data = response.data;
        // console.log(data);
        data.forEach(element => {
          this.$set(this.goods,this.goods.length,element);
        });
        // 初始化flag参数, !pending--重置下priceSum
        this.goods.forEach(element => {
          // 保留两位小数
          this.$set(element,"price",parseFloat(element.price).toFixed(2));
          this.$set(element,"flag",false);
          this.$set(element,"priceSum",parseFloat(element.num * element.price).toFixed(2))
        });
      }
    }).catch((error)=>{
      this.$message({
        type: 'warning',
        message: '后台出错',
      });
      console.log(error);
      return false;
    });
  },
  methods:{
    validatePhone(rule, value, callback){
      let regMobile = /^1\d{10}$/;
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
    },
    validateName(rule, value, callback){
			if (value === '') {
        callback(new Error('请输入姓名'));
        return false;
			} else {
        callback();
        return true;
			}
    },
    validateAddress(rule, value, callback){
			if (value === '') {
        callback(new Error('请输入地址'));
        return false;
			} else {
        callback();
        return true;
			}
    },
    // 全选or全部取消
    chooseAll(){
      this.goods.forEach(element => {
        if(element.num > 0){
          // 在all改变前执行
          element.flag = !this.all;
        }
    });
    },
    // 跳转至商城
    jump2mall(){
      this.$router.push('/products');
    },
    // 提交订单第一步，唤出弹窗
    submitPurchase(){
      let flag = false;
      this.goods.forEach(element => {
        if(element.flag){
          flag = true;
        }
      })
      if(!flag){
        this.$message({
          type: 'warning',
          message: '请选择至少一项服务',
        });
      }
      else{
        this.modal = true;
      }
    },
    // 重置地址信息
    resetdata(){
      this.$refs['ruleForm'].resetFields();
      this.dataForm['pay_list'] = [];
    },
    // 隐藏蒙版
    hideModal(){
      // 重置已填写内容
      this.resetdata();
      this.modal = false;
    },
    // 提交地址相关信息
    solveMsg(){
      let that = this;
      this.$refs['ruleForm'].validate(valid => {
				if (valid) {
          // let that = this
          this.packDataForm();
          // 数据封装成后台可解析dict
          let params = new URLSearchParams();
          for(let key of Object.keys(this.dataForm)){
            params.append(key,this.dataForm[key]);
          }
          // 衔接出现问题，waiting for debug
          Axios.post(this.uploadUrl, params,
            {headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
            }}
          ).then(function(response){
            if(response.status === 200){
              let data = response.data;
              console.log(data);
              if(data['success']){
                // that.reload();
                that.$router.push({path:'/payment',query:{id:data['paymentID']}});
              }
            }
          }).catch(function (error){
            console.log(error);
          });
          this.$refs['ruleForm'].resetFields();
          this.modal = false;
				} else {
					console.log('error submit!!');
					return false;
				}
			});
    },
    // 打包函数 
    packDataForm() {
      this.dataForm['id'] = localStorage.getItem("userPhone");
      this.dataForm['user_name'] = this.ruleForm['user_name'];
      this.dataForm['user_phone'] = this.ruleForm['user_phone'];
      this.dataForm['user_address'] = this.ruleForm['user_address'];
      this.dataForm['tot_num'] = this.sum;
      this.dataForm['pay_list'] = [];
      this.goods.forEach(element => {
        if(element.flag){
          let temp = {
            "detail_id": element.detail_id,
            "num": element.num,
          }
          this.dataForm['pay_list'][this.dataForm['pay_list'].length]=temp;
        }
      })
      // 字符串化数组
      this.dataForm['pay_list'] = JSON.stringify(this.dataForm['pay_list']);
    },
    
  },
}
</script>

<style scoped>
  #cart{
    min-height:800px;
  }
  .title{
    margin-left: 400px;
  }
  .empty{
    margin-left: 400px;
  }
  .tips{
    width: 60%;
    min-width: 800px;
    height: 40px;
    margin-left: 400px;
    text-align: center;
    display: flex;
  }
  .flag{
    width: 10%;
    margin-left: 20px;
  }
  .img{
    width: 16%;
  }
  .title1{    
    width: 14%;
  }
  .title2{
    width: 12%;
  }
  .price-single{
    width: 12%;
  }
  .num-control{
    width: 12%;
  }
  .price-sum{
    width: 12%;
  }
  .delete{
    width: 12%;
  }
  .price-tag{
    width: 70%;
    text-align: right;
    font-weight: bold;
    font-size: 20px;
    padding-top: 10px;
    /* color: red; */
  }
  .price{
    width: 18%;
    text-align: center;
    font-weight: bold;
    font-size: 30px;
    padding-top: 5px;
    color: red;
  }
  #purchase{
    width: 12%;
    border: none;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 24px;
    font-weight: bold;
    cursor: pointer;
    border-radius: 15px;
    outline: none;
    background-color: #ffce6b;
  }
  .empty{
    cursor: pointer;
  }
  .empty:hover{
    color:red;
  }
  .in-content{
    width: 800px;
  }
  .sp{
    text-align: right;
    padding-right: 10%;
  }
  .demo-ruleForm{
    margin-top: 20px;
  }
</style>