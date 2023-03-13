const state = {
  drawer: true,
}

const mutations = {
  toggleDrawer: state => {state.drawer = !state.drawer},
}

const actions = {
  TOGGLE_DRAWER: ({commit}) => {commit('toggleDrawer');},
}

const getters = {
  DRAWER_STATE: state => state.drawer,
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}