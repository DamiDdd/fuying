const actions = {
    setUser({commit}, flag){
        commit("userStatus",flag)
    },
    setAdmin({commit},flag){
        commit("admin",flag)
    },
}

export default actions

