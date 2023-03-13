import api from '@/api'
import * as types from '../mutation-types'
import Request from '@/api/core/Request'

const state = {
  users: {
    web: [],
    mobile: [],
    register: []
  },
  getUserRegistrationRequest: new Request(),
  indexRequest: new Request(),
  addRequest: new Request(),
  editRequest: new Request(),
  deleteRequest: new Request(),
  approveRequest: new Request(),
  // filterManage: {
  //   page_size: 10,
  //   page: 1,
  //   search: undefined
  // },
  filters: {
    page_size: 10,
    page: 1,
    search: undefined
  }
}
const getters = {
  webUsers: state => state.users.web,
  mobileUsers: state => state.users.mobile,
  registrationUsers: state => state.users.register,
  indexUsersRequest: state => state.indexRequest,
  addUserRequest: state => state.addRequest,
  editUserRequest: state => state.editRequest,
  deleteUserRequest: state => state.deleteRequest,
  approveUserRequest: state => state.approveRequest,
  userFilters: state => state.filters
  // userFilterManage: state => state.filterManage
}
const actions = {
  getUsers ({ commit }) {
    commit(types.GET_USERS_REQUEST)
    api.getUsers()
      .then(res => {
        commit(types.GET_USERS_SUCCESS, res.data)
      })
      .catch(error => commit(types.GET_USERS_FAILURE, error))
  },
  addUser ({ commit, dispatch }, req) {
    commit(types.UPLOAD_USER_REQUEST)
    api.addUser(req)
      .then(() => {
        commit(types.UPLOAD_USER_SUCCESS)
        dispatch('getUsers')
      })
      .catch(err => {
        commit(types.UPLOAD_USER_FAILURE, err)
      })
  },
  updateUser ({ commit, dispatch }, user) {
    commit(types.UPDATE_USER_REQUEST)

    api.updateUser(user)
      .then(() => {
        commit(types.UPDATE_USER_SUCCESS)
        dispatch('getUsers')
      })
      .catch(err => {
        commit(types.UPDATE_USER_FAILURE, err)
      })
  },
  deleteUser ({ commit, dispatch }, user) {
    commit(types.DELETE_USER_REQUEST)

    api.deleteUser(user)
      .then(() => {
        commit(types.DELETE_USER_SUCCESS)
        dispatch('getUsers')
      })
      .catch(error => commit(types.DELETE_USER_FAILURE, error))
  },
  approveUser ({ commit, dispatch }, user) {
    commit(types.APPROVE_USER_REQUEST)
    api.approveUser(user.confirmation_code)
      .then(() => {
        commit(types.APPROVE_USER_SUCCESS)
        dispatch('getUsers')
      })
      .catch(error => commit(types.APPROVE_USER_FAILURE, error))
  }
}
const mutations = {
  [types.GET_USERS_REQUEST]: (state) => (state.indexRequest.requesting()),
  [types.GET_USERS_FAILURE]: (state, error) => (state.indexRequest.failure(error)),
  [types.GET_USERS_SUCCESS]: (state, users) => {
    state.indexRequest.success()
    state.users = users
  },

  [types.UPLOAD_USER_REQUEST]: (state) => (state.addRequest.requesting()),
  [types.UPLOAD_USER_FAILURE]: (state, error) => (state.addRequest.failure(error)),
  [types.UPLOAD_USER_SUCCESS]: (state) => (state.addRequest.success()),

  [types.UPDATE_USER_REQUEST]: (state) => (state.editRequest.requesting()),
  [types.UPDATE_USER_FAILURE]: (state, error) => (state.editRequest.failure(error)),
  [types.UPDATE_USER_SUCCESS]: (state) => (state.editRequest.success()),

  [types.DELETE_USER_REQUEST]: (state) => (state.deleteRequest.requesting()),
  [types.DELETE_USER_FAILURE]: (state, error) => (state.deleteRequest.failure(error)),
  [types.DELETE_USER_SUCCESS]: (state) => (state.deleteRequest.success()),

  [types.APPROVE_USER_REQUEST]: (state) => (state.approveRequest.requesting()),
  [types.APPROVE_USER_FAILURE]: (state, error) => (state.approveRequest.failure(error)),
  [types.APPROVE_USER_SUCCESS]: (state) => (state.approveRequest.success()),
  [types.USER_FILTERS]: (state, filters) => {
    state.filters = filters
  },
  [types.USER_FILTERS_RESET]: (state) => {
    state.filters = {
      page_size: 10,
      page: 1,
      search: undefined
    }
  }
  // [types.USER_FILTER_MANAGE]: (state, filters) => {
  //   state.filterManage = filters
  // }
}
export default {
  state,
  getters,
  actions,
  mutations
}
