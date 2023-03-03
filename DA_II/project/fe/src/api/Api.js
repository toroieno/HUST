import BaseApi from './BaseApi'
import store from '@/store' // eslint-disable-line

import toFormData from './utils/toFormData' // eslint-disable-line

import { END_POINT } from '@/config'

class Api extends BaseApi {
  /** Overide base methods **/

  /**
   * Normal http request
   *
   * @param {string} method http method
   * @param {string} url http url
   * @param {Object} data params for get or body data for post, put, patch
   * @param {Object} config axios config object. See https://github.com/mzabriskie/axios
   */
  submit (method, url, data, config = {}) {
    url = END_POINT + url
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
    url = END_POINT + url
    const submit = super.authSubmit(method, url, data, config)
    return submit
  }

  /** Api methods **/
  getAllLecturers() {
    return this.authSubmit('get', `/lecturers`)
  }
}

export default Api
