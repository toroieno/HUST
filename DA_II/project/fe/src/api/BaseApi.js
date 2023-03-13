import axios from 'axios'
import store from '@/store'

import { SET_TOKEN, CLEAR_TOKEN } from '@/store/mutation-types'
import { merge } from 'lodash'
import { HTTP_UNAUTHORIZED } from './core/Error'

class BaseApi {

  get source () { return this._source }
  set source (value) { this._source = value }

  constructor () {
    this._source = axios.CancelToken.source()
  }

  /** Public Methods **/

  /**
   * Cancel all requesting http requests
   *
   * @param {String} message Message will be pass throw a error object in catch function
   */
  cancelAll (message) {
    this._source.cancel(message)
  }

  /**
   * Make a cancel token to cancel a http request
   *
   * @param {Function} callback
   * @return {axios.CancelToken} cancelToken pass this object to axios config
   */
  makeCancelToken (callback) {
    return new axios.CancelToken(callback)
  }

  /** Common api **/
  // login ({ username, password }) {
  //   return new Promise((resolve, reject) => {
  //     const req = {
  //       'username': username,
  //       'password': password
  //     }

  //     this.submit('post', '/login', req)
  //       .then(response => {
  //         store.commit(SET_TOKEN, response.data.token)
  //         resolve(response)
  //       })
  //       .catch(error => reject(error))
  //   })
  // }

  logout () {
    return new Promise((resolve, reject) => { // eslint-disable-line
      const token = store.state.auth.token
      const req = {
        'token': token
      }

      this.submit('get', '/logout', req)
        .then(response => {
          store.commit(CLEAR_TOKEN)
          resolve(response)
        })
        .catch(error => {
          // Token may has expired when logout
          // So it's ok to treat it as success case
          console.error(error)
          store.commit(CLEAR_TOKEN)
          resolve(error)
        })
    })
  }

  register (req) {
    return this.submit('post', '/register', req)
  }

  getMe () {
    return this.authSubmit('get', '/me')
  }

  refreshToken () {
    return this._submitWithToken('get', '/api/token')
  }

  checkToken () {
    return this.authSubmit('get', '/check')
  }

  changePassword (data) {
    return this.authSubmit('post', '/changePassword', data)
  }

  /** Base methods **/

  /**
   * Normal http request
   *
   * @param {string} method http method
   * @param {string} url http url
   * @param {Object} data params for get or body data for post, put, patch
   * @param {Object} config axios config object. See https://github.com/mzabriskie/axios
   */
  submit (method, url, data, config = {}) {
    return new Promise((resolve, reject) => {
      this._submit(method, url, data, config)
        .then(response => resolve(response))
        .catch(error => reject(this._handleError(error)))
    })
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
    let currentTime = new Date()
    if (!this._oldTime) {
      this._oldTime = new Date()
    }
    let diff = (currentTime.getTime() - this._oldTime.getTime()) / 1000
    this._oldTime = currentTime
    if (diff > 30 * 60 * 60) {
      this.logout()
    }
    return new Promise((resolve, reject) => {
      this._authSubmit(method, url, data, config)
        .then(response => resolve(response))
        .catch(error => reject(this._handleError(error)))
    })
  }

  /** Private Methods */

  /**
   * Handle error for all errors (from server or local error)
   *
   * @param {Object} error
   */
  _handleError (error) {
    let formatError = {
      /*
        "message": "422 Unprocessable Entity", // required
        "status_code": 422, // required
        "code": "unprocessable_entity",
        "errors": { // option
          "source": [
            "The source field is required."
          ],
          "from_date": [
            "The from date field is required."
          ],
          "to_date": [
            "The to date field is required."
          ]
        }
      */
    }

    // const req = error.config
    // console.log('Request', req)

    if (error.response) {
      const status = error.response.status

      switch (status) {
        default:
          formatError = error.response.data
      }
    } else {
      console.error(error)
      formatError = {
        'message': error.message,
        'status_code': 404,
        'data': error
      }
    }

    return formatError
  }

  /**
   * Handle all response from axios
   *
   * @param {Object} response response object return by axios
   */
  _handleResponse (response) {
    // console.log(response.request)

    return response
  }

  /**
   * Handle refresh token use case
   *
   */
  _authSubmit (method, url, data, config = {}) {
    return new Promise((resolve, reject) => {
      this._submitWithToken(method, url, data, config)
        .then(response => resolve(response))
        .catch(error => {
          // Check if token has expired
          if (this._shouldRefreshToken(error)) {
            this.refreshToken()
              .then(response => {
                // Store new token from refresh
                store.commit(SET_TOKEN, response.data.token)

                // Continues submit current request
                this._submitWithToken(method, url, data, config)
                  .then(response => resolve(response))
                  .catch(error => reject(error))
              })
              .catch(error => {
                // Token refresh's time to live is over, so it can not be refreshed, user need to re-authenticate
                reject(error)
                this._handleTokenExpired()
              })
          } else {
            reject(error)
          }
        })
    })
  }

  _shouldRefreshToken (error) {
    return error.response && error.response.status === HTTP_UNAUTHORIZED && !error.config.url.includes('/authenticate')
  }

  _handleTokenExpired () {
    const token = store.state.auth.token
    if (token) {
      store.commit(CLEAR_TOKEN)
      // Should be refresh cancelToken after token has expired and cancel All request
      // this.cancelAll('Your token has expired. Please login again!')
      alert('Your token has expired. Please login again!')
      window.location.replace('/#/login')
    } else {
      console.log('Token do not exists in local storage')
    }
  }

  _submitWithToken (method, url, data, config = {}) {
    const token = store.state.auth.token
    if (token) {
      config = merge({
        headers: {
          'Authorization': `Bearer ${token}`
        }
      }, config)
    }

    return this._submit(method, url, data, config)
  }

  _submit (method, url, data, config = {}) {
    // transformRequest for get method
    if (method === 'get') {
      data = this._transformGetData(config, data)
    }

    config = merge({
      method: method,
      url: url,
      cancelToken: this._source.token,
      params: method === 'get' ? data : {},
      data: method !== 'get' ? data : {},
      headers: {
        'Accept': 'application/json',
        'Content-Type': data instanceof window.FormData ? 'multipart/form-data' : 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      }
    }, config)

    return axios(config)
  }

  _transformGetData (config, data) {
    if (this._needToTransform(config, data)) {
      data = JSON.parse(config.transformRequest[0](data))
      config.transformRequest = [] // Must call after call transformRequest
      return data
    } else {
      return data
    }
  }

  _needToTransform (config) {
    return config.transformRequest && config.transformRequest.length > 0 && typeof config.transformRequest[0] === 'function'
  }
}

export default BaseApi
