export const TOKEN_STORAGE_KEY = 'user-token'
export const TOKEN_REMEMBER_ME = 'remember-me'

export default class Token {
  constructor () {
    this._value = window.localStorage.getItem(TOKEN_STORAGE_KEY) || undefined
    this._rememberMe = Boolean(window.localStorage.getItem(TOKEN_REMEMBER_ME)) || true
  }

  /* Getters and Setters */
  get value () {
    return this._value
  }
  set value (value) {
    this._value = value
    // Only store to local storage if user select remember me
    if (this._rememberMe) window.localStorage.setItem(TOKEN_STORAGE_KEY, this._value)
  }

  get rememberMe () {
    return this._rememberMe
  }

  set rememberMe (value) {
    this._rememberMe = value
    window.localStorage.setItem(TOKEN_REMEMBER_ME, this._rememberMe)
  }

  /* Public methods */
  clear () {
    this._value = undefined
    window.localStorage.removeItem(TOKEN_STORAGE_KEY)
  }

  loggedIn () {
    return !!this._value
  }
}
