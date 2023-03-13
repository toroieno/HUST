import api from '@/api'
import store from '@/store'

import { merge } from 'lodash'

import Error from './Error'

const STATUS_REQUESTING = 'STATUS_REQUESTING'
const STATUS_SUCCESS = 'STATUS_SUCCESS'
const STATUS_FAILURE = 'STATUS_FAILURE'

class Request {
  /* Private properties */

  constructor (name, method, url, config) {
    this._method = method
    this._status = undefined
    this._progress = 0
    this._error = new Error()
    this._cancelToken = undefined

    this._name = '' // Unique name
    this._method = 'get'

    this._url = url
    this._config = merge({
      auth: false, // request should add token to header?
      progress: false, // request should handle progress?
      cancel: false // request could be cancel?
    }, config)
  }

  /* Getters and Setters */
  get status () { return this._status }
  set status (val) { this._status = val }

  get error () { return this._error }
  set error (val) { this._error = val }

  get progress () { return this._progress }
  set progress (val) { this._progress = val }

  get cancelToken () { return this._cancelToken }
  set cancelToken (val) { this._cancelToken = val }

  get requestMutationType () { return this._name + '_REQUEST' }
  get successMutationType () { return this._name + '_SUCCESS' }
  get failureMutationType () { return this._name + '_FAILURE' }
  get progressMutationType () { return this._name + '_PROGRESS' }

  /* Public properties */
  isRequesting () { return this.status === STATUS_REQUESTING }
  isSuccess () { return this.status === STATUS_SUCCESS }
  isFailure () { return this.status === STATUS_FAILURE }

  request (data) {
    const submit = this._config.auth ? api.authSubmit : api.submit

    store.commit(this.requestMutationType)

    submit(this._method, this._url, data, {
      onUploadProgress: e => store.commit(this.uploadingMutation, e)
    })
      .then(res => store.commit(this.successMutationType, res.data))
      .catch(error => store.commit(this.failureMutationType, error))
  }

  requesting () {
    this.status = STATUS_REQUESTING
    this.error.clear()
  }

  success () {
    this.status = STATUS_SUCCESS
  }

  failure (error) {
    this.status = STATUS_FAILURE
    this.error.value = error
  }

  cancel (message) {
    this._cancelToken(message)
  }

  onUploadProgress (progressEvent) {
    this._progress = Math.round((progressEvent.loaded * 100) / progressEvent.total)
  }
}

export default Request
