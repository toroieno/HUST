export const s = function (state, arr) {
  if (arr.length === 2) {
    state[arr[0]] = arr[1]
  } else {
    let obj = state[arr[0]]
    for (let i = 1; i < arr.length - 2; i++) {
      obj = obj[arr[i]]
    }
    obj[arr[arr.length - 2]] = arr[arr.length - 1]
  }
}
export const mapState = function (p1, p2) {
  let obj = {}
  if (Array.isArray(p1)) {
    for (let i of p1) {
      obj[i] = {
        get() {
          return this.$store.state[i]
        },
        set(val) {
          this.$store.commit('s', [i, val])
        }
      }
    }
    return obj
  } else {
    for (let i of p2) {
      obj[i] = {
        get() {
          return this.$store.state[p1][i]
        },
        set(val) {
          this.$store.commit('s', [p1, i, val])
        }
      }
    }
    return obj
  }
}