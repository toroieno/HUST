import Store from '@/store'
import api from '@/api'

export default async function checkAuth(to, from, next) {
  try {
    console.log('check auth')
    if (to.query.token) {
      const token = to.query.token
      Store.commit('authenticate/SET_TOKEN', token)
      api.setToken("Bearer" + JSON.parse(window.atob(token)).access_token)
      next(to.path)
    }
    const token = api.getToken()
    if (!token) {
      throw "token"
    }
    console.log(token);    
    // let result = await api.post(`${config.backend}/me`, {token})
    let result = await api.getMe()
    console.log('result get me', result);
    Store.commit('authenticate/SET_USER', result.data.user)
    // next()
    // if (to.meta.roles === '*' || to.meta.roles.some(val => val === result.data.user.role.code)) next()
    // else location.href = `${location.origin}/401`
  } catch (e) {
    api.deleteToken()
    console.log('error');
    // location.href = `${location.origin}/login`
  } finally {
    next()
  }
}