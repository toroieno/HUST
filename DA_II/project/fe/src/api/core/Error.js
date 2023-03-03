
/* Error value format
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

export const HTTP_UNPROCESSABLE_ENTITY = 422
export const HTTP_UNAUTHORIZED = 401 // Login failed or token has expired

class Error {

  constructor () {
    this._value = undefined
  }

  get value () { return this._value }
  set value (val) { this._value = val }

  get statusCode () { return this.value && this.value.status_code }
  get message () { return this.value && this.value.message }
  get code () { return this.value && this.value.code }

  clear () {
    this.value = undefined
  }

  get (name) {
    return (this.value && this.value.errors && this.value.errors[name] && this.value.errors[name][0]) || ''
  }

  has (name) {
    return !!this.get(name)
  }

  isUnprocessableEntity () {
    return !!(this.statusCode === HTTP_UNPROCESSABLE_ENTITY)
  }

  isUnauthorized () {
    return !!(this.statusCode === HTTP_UNAUTHORIZED)
  }
}

export default Error
