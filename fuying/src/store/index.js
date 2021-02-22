import Vue from "vue";
import Vuex from "vuex";

import mutations from "./mutations";
import actions from "./actions";
import getters from "./getters";

Vue.use(Vuex);

const state = {
  isLogin: false, // 登录状态
  isAdmin: false // 管理员权限状态
};

const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});

export default store;
