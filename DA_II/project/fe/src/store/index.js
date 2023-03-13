import Vue from 'vue'
import Vuex from 'vuex'

import auth from './modules/auth'
import Users from './modules/Users'

import MainNavigationBar from './modules/MainNavigationBar'

import ProjectManagement from './modules/ProjectManagement'
import message from './modules/message'
import admin from './modules/admin'

const debug = process.env.NODE_ENV !== 'production'

Vue.use(Vuex)

const state = {
  appName: 'Template'
}

const getters = {
  appName: state => state.appName
}

export default new Vuex.Store({
  strict: debug,
  state,
  getters,
  modules: {
    auth,
    Users,
    MainNavigationBar,
    ProjectManagement,
    message,
    admin,
  }
})
