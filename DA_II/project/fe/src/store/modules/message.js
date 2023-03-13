export default {
  namespaced: true,
  state: {
    text: '',
    snackBar: false,
    color: 'red',
  },

  getter: {
    text (state) {
      return state.text
    },
    snackBar (state) {
      return state.snackBar
    },
    color (state) {
      return state.color
    }
  },

  mutations: {
    SHOW_SUCCESS (state, newValue) {
      state.text = newValue
      state.snackBar = true
      state.color = 'green'
    },
    SHOW_ERROR (state, newValue) {
      state.text = newValue
      state.snackBar = true
      state.color = 'red'
    },
    SHOW_WARNING (state, newValue) {
      state.text = newValue
      state.snackBar = true
      state.color = '#ffc101'
    }
  }
}