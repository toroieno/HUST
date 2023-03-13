const state = {
  tab: null,
}

const mutations = {
  // toggleDrawer: state => {state.drawer = !state.drawer},
}

const actions = {
  // TOGGLE_DRAWER: ({commit}) => {commit('toggleDrawer');},
}

const getters = {
  TAB_STATE: state => state.tab,
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}