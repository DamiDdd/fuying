const mutations = {
  userStatus(state, flag) {
    state.isLogin = flag;
  },
  admin(state, flag) {
    state.isAdmin = flag;
  }
};

export default mutations;
