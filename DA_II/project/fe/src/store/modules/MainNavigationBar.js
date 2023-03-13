import * as types from '../mutation-types'

const state = {
  activeIndex: '1'
}

const getters = {
  activeIndex: state => state.activeIndex
}

const actions = {
  changeIndex ({commit}, id) {
    commit(types.CHANGE_INDEX, id)
  }
}

const mutations = {
  [types.CHANGE_INDEX]: (state, id) => {
    state.activeIndex = id
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
