import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    count: 10,
    count2: 100,
  },
  mutations: {
    increment (state) {
      state.count++
    }
  },
})