import * as types from '../mutation-types'
import tokenManager from '@/api/token'
import api from '@/api'
import Request from '@/api/core/Request'
import User from '@/api/models/User'

const state = {
  me: new User(),
  token: tokenManager.value,
  rememberMe: tokenManager.rememberMe,

  loginRequest: new Request(),
  registerRequest: new Request(),
  logoutRequest: new Request(),
  getMeRequest: new Request(),
  getTokenRequest: new Request(),
  checkTokenRequest: new Request(),
  changePasswordRequest: new Request()
}

const getters = {
  loginRequest: state => state.loginRequest,
  logoutRequest: state => state.logoutRequest,
  registerRequest: state => state.registerRequest,
  getMeRequest: state => state.getMeRequest,
  getTokenRequest: state => state.getTokenRequest,
  checkTokenRequest: state => state.checkTokenRequest,
  me: state => state.me,
  myRoles: state => state.me.roles,
  myPermissions: state => state.me.permissions,
  token: state => state.token,
  rememberMe: state => state.rememberMe,
  changePasswordRequest: state => state.changePasswordRequest
}

const actions = {
  login ({ commit }, req) {
    commit(types.LOGIN_REQUEST)

    api.login(req)
      .then(() => {
        commit(types.LOGIN_SUCCESS)
      })
      .catch(error => commit(types.LOGIN_FAILURE, error))
  },

  logout ({ commit }) {
    commit(types.LOGOUT_REQUEST)

    api.logout()
      .then(() => commit(types.LOGOUT_SUCCESS))
      .catch(error => commit(types.LOGOUT_FAILURE, error))
  },

  register ({ commit }, req) {
    commit(types.REGISTER_REQUEST)

    api.register(req)
      .then(res => commit(types.REGISTER_SUCCESS, res.data))
      .catch(error => commit(types.REGISTER_FAILURE, error))
  },

  getMe ({ commit }) {
    commit(types.GET_ME_REQUEST)

    return new Promise((resolve, reject) => {
      api.getMe()
        .then(res => {
          commit(types.GET_ME_SUCCESS, res.data)
          resolve(res.data)
        })
        .catch(error => {
          commit(types.GET_ME_FAILURE, error)
          reject(error)
        })
    })
  },

  checkToken ({ commit }, type) {
    commit(types.CHECK_TOKEN_REQUEST)

    return new Promise((resolve, reject) => {
      api.checkToken()
        .then(() => {
          commit(types.CHECK_TOKEN_SUCCESS)
          resolve(type)
        })
        .catch(error => {
          commit(types.CHECK_TOKEN_FAILURE, error)
          reject(error)
        })
    })
  },

  changePassword ({ commit }, req) {
    commit(types.CHANGE_PASSWORD_REQUEST)

    api.changePassword(req)
      .then(res => commit(types.CHANGE_PASSWORD_SUCCESS, res.data))
      .catch(error => commit(types.CHANGE_PASSWORD_FAILURE, error))
  }
}

const mutations = {
  [types.LOGIN_REQUEST]: (state) => (state.loginRequest.requesting()),
  [types.LOGIN_FAILURE]: (state, error) => (state.loginRequest.failure(error)),
  [types.LOGIN_SUCCESS]: (state) => (state.loginRequest.success()),

  [types.LOGOUT_REQUEST]: (state) => (state.logoutRequest.requesting()),
  [types.LOGOUT_FAILURE]: (state, error) => (state.logoutRequest.failure(error)),
  [types.LOGOUT_SUCCESS]: (state) => {
    state.me = new User()
    state.logoutRequest.success()
  },

  [types.REGISTER_REQUEST]: (state) => (state.registerRequest.requesting()),
  [types.REGISTER_FAILURE]: (state, error) => (state.registerRequest.failure(error)),
  [types.REGISTER_SUCCESS]: (state) => (state.registerRequest.success()),

  [types.CHECK_TOKEN_REQUEST]: (state) => (state.checkTokenRequest.requesting()),
  [types.CHECK_TOKEN_FAILURE]: (state, error) => (state.checkTokenRequest.failure(error)),
  [types.CHECK_TOKEN_SUCCESS]: (state) => (state.checkTokenRequest.success()),

  [types.GET_ME_REQUEST]: (state) => (state.getMeRequest.requesting()),
  [types.GET_ME_FAILURE]: (state, error) => (state.getMeRequest.failure(error)),
  [types.GET_ME_SUCCESS]: (state, data) => {
    state.getMeRequest.success()
    state.me.update(data)
  },

  [types.CHANGE_PASSWORD_REQUEST]: (state) => (state.changePasswordRequest.requesting()),
  [types.CHANGE_PASSWORD_FAILURE]: (state, error) => (state.changePasswordRequest.failure(error)),
  [types.CHANGE_PASSWORD_SUCCESS]: (state) => (state.changePasswordRequest.success()),

  [types.SET_TOKEN]: (state, token) => {
    state.token = token
    tokenManager.value = token
  },

  [types.CLEAR_TOKEN]: (state) => {
    state.token = undefined
    tokenManager.clear()
  },

  [types.REMEMBER_ME]: (state, remember) => {
    state.rememberMe = remember
    tokenManager.rememberMe = remember
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
