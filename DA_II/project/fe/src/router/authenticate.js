function checkAuth () {
  return new Promise((resolve, reject) => {
    const token = store.state.auth.token
    if (!token) {
      reject(new Error('Not login yet'))
    } else {
      // Refresh browser or open new will have only token in localStorage but not state.auth.me
      // So it should fetch user info from server

      // Always check token before go into page
      // Because token maybe has expired
      store.dispatch('getMe')
        .then(() => resolve())
        .catch(error => reject(error instanceof Error ? error : new Error(error.message)))
    }
  })
}

export default function requireAuth (to, from, next) {
  checkAuth()
    .then(() => next())
    .catch(error => {
      console.error(error)
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    })
}