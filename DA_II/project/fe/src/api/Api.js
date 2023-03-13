import BaseApi from './BaseApi'
import store from '@/store' // eslint-disable-line
import { SET_TOKEN } from '@/store/mutation-types'

import toFormData from './utils/toFormData' // eslint-disable-line

import { HOST_POINT } from '@/config'

class Api extends BaseApi {
  /** Overide base methods **/
  getToken() {
    return localStorage.getItem('jwt_token')
  }

  setToken(token) {
    localStorage.setItem('jwt_token', token)
  }

  deleteToken() {
    localStorage.removeItem('jwt_token')
  }

  getConfigMethodGet(currentConfig) {
    let defaultConfig = {
      configHeader: {},
      notification: false,
      auth: true,
      callback: undefined
    }
    if (currentConfig) for (const key in currentConfig) {
      defaultConfig[key] = currentConfig[key]
    }
    return defaultConfig
  }

  getConfig(currentConfig) {
    let defaultConfig = {
      configHeader: {},
      notification: true,
      auth: true,
      callback: undefined
    }
    if (currentConfig) for (const key in currentConfig) {
      defaultConfig[key] = currentConfig[key]
    }
    return defaultConfig
  }

  get(url, params = {}, config = {}) {
    config = this.getConfigMethodGet(config)
    return this.submit('get', url, params, config)
  }

  post(url, data = {}, config = {}) {
    config = this.getConfig(config)
    return this.submit('post', url, data, config)
  }

  put(url, data = {}, config = {}) {
    config = this.getConfig(config)
    return this.submit('put', url, data, config)
  }

  patch(url, data = {}, config = {}) {
    config = this.getConfig(config)
    return this.submit('patch', url, data, config)
  }

  delete(url, data = {}, config = {}) {
    config = this.getConfig(config)
    return this.submit('delete', url, data, config)
  }

  /**
   * Normal http request
   *
   * @param {string} method http method
   * @param {string} url http url
   * @param {Object} data params for get or body data for post, put, patch
   * @param {Object} config axios config object. See https://github.com/mzabriskie/axios
   */
  submit (method, url, data, config = {}) {
    // url = END_POINT + url
    const subUrl = url.substring(0, 4)
    url = subUrl === 'http' ? url : (HOST_POINT + url)
    const submit = super.submit(method, url, data, config)
    return submit
  }

  /**
   * Submit http request with Authorization header
   *
   * @param {string} method http method
   * @param {string} url http url
   * @param {Object} data params for get or body data for post, put, patch
   * @param {Object} config axios config object. See https://github.com/mzabriskie/axios
   */
  authSubmit (method, url, data, config = {}) {
    // url = END_POINT + url
    const subUrl = url.substring(0, 4)
    url = subUrl === 'http' ? url : (HOST_POINT + url)
    const submit = super.authSubmit(method, url, data, config)
    return submit
  }

  /** Api methods **/
  login ({ username, password }) {
    return new Promise((resolve, reject) => {
      const req = {
        'username': username,
        'password': password
      }

      this.submit('post', '/login', req)
        .then(response => {
          store.commit(`authenticate.${SET_TOKEN}`, response.data.token)
          resolve(response)
        })
        .catch(error => reject(error))
    })
  }

  getMe() {
    return this.authSubmit('get', '/me')
  }

  getAllLecturers() {
    return this.authSubmit('get', `/lecturers`)
  }

}

export default Api
