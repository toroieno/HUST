export default class User {

  get permissions () { return this.roles.reduce((permissions, role) => permissions.concat(role.permissions), []) }
  get isAdmin () {
    for (const role of this.roles) {
      if (role.all) return true
    }

    return false
  }

  constructor (data) {
    this.id = -1
    this.name = 'Guest'
    this.email = 'guest@skymapglobal.com'
    this.created_at = '2017-06-08 00:00:00'
    this.updated_at = '2017-06-08 00:00:00'
    // this.mobile = 'Default Guest'
    this.roles = [{
      'id': 100,
      'name': 'Guest',
      'all': false,
      'sort': 100,
      'created_at': '2017-06-08 07:10:22',
      'updated_at': '2017-06-08 07:10:22'
    }]

    if (data) this.update(data)
  }

  update (data) {
    this.id = data['id']
    this.name = data['username']
    this.email = data['email']
    this.created_at = data['created_at']
    this.updated_at = data['updated_at']
    // this.mobile = data['mobile']
    this.roles = data['role']
    // this.department = data['department']
    // this.district = data['district']
  }

  hasRole (role) {
    let valid = false

    for (const r of this.roles) {
      if (r.id === role) {
        valid = true
        break
      }
    }

    return valid
  }

  hasRoles (roles) {
    let valid = false

    for (const role of roles) {
      if (this.hasRole(role)) {
        valid = true
        break
      }
    }

    return valid
  }

  hasAllRoles (roles) {
    let valid = true

    for (const role of roles) {
      if (!this.hasRole(role)) {
        valid = false
        break
      }
    }

    return valid
  }

  hasPermission (permission) {
    if (this.isAdmin) return true

    let valid = false

    for (const p of this.permissions) {
      if (p.name === permission) {
        valid = true
        break
      }
    }

    return valid
  }

  hasPermissions (permissions) {
    if (this.isAdmin) return true

    let valid = false

    for (const permission of permissions) {
      if (this.hasPermission(permission)) {
        valid = true
        break
      }
    }

    return valid
  }

  hasAllPermissions (permissions) {
    if (this.isAdmin) return true

    let valid = true

    for (const permission of permissions) {
      if (!this.hasPermission(permission)) {
        valid = false
        break
      }
    }

    return valid
  }
}
