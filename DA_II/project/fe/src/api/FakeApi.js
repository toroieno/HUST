import BaseFakeApi from './BaseFakeApi'
import store from '@/store'

import { SET_TOKEN, CLEAR_TOKEN } from '@/store/mutation-types'

const adminUser = {
  id: 1,
  email: 'admin@skymapglobal.com',
  password: 'admin',
  first_name: 'Default',
  last_name: 'Guest',
  created_at: '2017-06-08 00:00:00',
  updated_at: '2017-06-08 00:00:00',
  full_name: 'Default Guest',
  roles: [{
    'id': 1,
    'name': 'Admin',
    'all': true,
    'sort': 1,
    'created_at': '2017-06-08 07:10:22',
    'updated_at': '2017-06-08 07:10:22',
    'permissions': []
  }]
}

class FakeApi extends BaseFakeApi {
  login (req) {
    const resData = {
      token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsImlzcyI6Imh0dHA6XC9cL2xvY2FsaG9zdDo4MDAwXC9hcGlcL2xvZ2luIiwiaWF0IjoxNDkzMTA3MzI4LCJleHAiOjE0OTMxMTA5MjgsIm5iZiI6MTQ5MzEwNzMyOCwianRpIjoiVE9PZ1NBamNzQlQ3eXlUcCJ9.zVvWCFgVAP8jArLTIUix05-lj69_Ga6pG3OnJNr7ezc'
    }
    const success = this._rawResponse(resData)

    const invalidCredenTialsError = this._rawResponse({
      'code': 'invalid_credentials',
      'status_code': 401,
      'message': 'Invalid Credentials'
    }, 401)

    const unprocessableEntityError = this._rawResponse({
      'status_code': 422,
      'message': 'Unprocessable Entity',
      'errors': {
        'email': ['Email is invalid format'],
        'password': ['Password length need larger than 6']
      }
    })

    if (req.email === adminUser.email) {
      store.commit(SET_TOKEN, resData.token)
      return req.password === adminUser.password
        ? this._makePromise(req, success)
        : this._makePromise(req, success, invalidCredenTialsError)
    } else {
      return this._makePromise(req, success, unprocessableEntityError)
    }
  }

  register (req) {
    const success = this._rawResponse({
      'message': 'Your account have been created'
    })

    const error = this._rawResponse({
      'status_code': 422,
      'message': 'Unprocessable Entity',
      'errors': {
        'name': ['Field name is required'],
        'email': ['The email has already been taken.'],
        'password': ['Password length need larger than 6'],
        'password_confirmation': ['Password confirmation not match']
      }
    })

    if (req.email !== adminUser.email) {
      return this._makePromise(req, success)
    } else {
      return this._makePromise(req, success, error)
    }
  }

  logout (req) {
    store.commit(CLEAR_TOKEN)
    return this._makePromise(req, this._rawResponse({}))
  }

  getMe () {
    return this._makePromise({}, this._rawResponse({
      user: adminUser
    }))
  }
}

export default FakeApi
