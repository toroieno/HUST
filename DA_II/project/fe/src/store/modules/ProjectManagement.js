import * as types from '../mutation-types'

const state = {
  filters: {
    district: undefined,
    circle: undefined,
    department_id: undefined,
    funding_agency_id: undefined,
    search: undefined,
    year: undefined,
    dates: undefined,
    page_size: 10,
    page: 1
  }
}
const getters = {
  projectFilters: state => state.filters
}

const mutations = {
  [types.PROJECT_FILTERS]: (state, filters) => {
    state.filters = filters
  }
}

export default {
  state,
  getters,
  mutations
}
