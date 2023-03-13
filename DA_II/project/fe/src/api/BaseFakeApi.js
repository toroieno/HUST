import Api from './Api'
const LATENCY = 100

class BaseFakeApi extends Api {
  _getFakeError (status) { // eslint-disable-line no-unused-vars
    switch (status) {
      case 422:
        return {
          'message': '422 Unprocessable Entity',
          'status_code': 422,
          'errors': {
            'source': [
              'The source field is required.'
            ],
            'from_date': [
              'The from date field is required.'
            ],
            'to_date': [
              'The to date field is required.'
            ]
          }
        }
      default:
        return {
          'message': 'Fetch data fail',
          'status_code': status
        }
    }
  }

  _makePromise (req, res, error) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (error) {
          reject(error.data)
        } else {
          resolve(res)
        }
      }, LATENCY)
    })
  }

  _response (data = {}, status = 200, headers = {}, meta = {}) {
    return this._rawResponse({ data: data, meta: meta }, status, headers)
  }

  _rawResponse (data = {}, status = 200, headers = {}) {
    return {
      // `data` is the response that was provided by the server
      data: data,

      // `status` is the HTTP status code from the server response
      status: status,

      // `statusText` is the HTTP status message from the server response
      statusText: 'OK',

      // `headers` the headers that the server responded with
      headers: headers,

      // `config` is the config that was provided to `axios` for the request
      config: {}
    }
  }
}

export default BaseFakeApi
