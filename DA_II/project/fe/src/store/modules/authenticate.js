import User from '@/api/models/User'

export default {
  namespaced: true,
  state: {
    token: '',
    currentUser: undefined,
  },
  getters: {
    currentUser(state) {
      return state.currentUser;
    },
  },
  mutations: {
    SET_USER(state, newValue) {
      state.currentUser = new User(newValue);
    },
    SET_TOKEN(state, newValue) {
      state.token = newValue
    }
  },
};
