<template>
  <el-form size="mini" label-position="right" label-width="120px" >
    <el-form-item class="filter-group" label="Filters">
      <el-row :gutter="10">
        <el-col :span="7">
          <el-select
            size="mini"
            class="filter-item"
            :disabled="me.hasRole(4)"
            filterable
            :filter-method="filterDis"
            @focus="resetDis"
            :value="form.district"
            @change="getCircles"
            v-model="form.district"
            placeholder="District"
            clearable>
            <el-option
              v-for="item of districts"
              :key="item.dist_name"
              :label="item.dist_name"
              :value="item.dist_name">
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="7">
          <el-select
            size="mini"
            class="filter-item"
            filterable
            :filter-method="filterCir"
            @focus="resetCir"
            :value="form.circle"
            v-model="form.circle"
            @change="submitForm"
            placeholder="Circle" clearable>
            <el-option
              v-for="item of circles"
              :key="item.gid"
              :label="item.name"
              :value="item.name">
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="5">
          <div style="display: inline-flex; align-items: center">
          <label>Status  </label>
            <el-select
              style="margin-left: 4px"
              size="mini"
              class="filter-item"
              :value="form.status"
              v-model="form.status"
              @change="submitForm"
              placeholder="Status" clearable>
              <el-option
                v-for="item of status"
                :key="item"
                :label="item"
                :value="item">
              </el-option>
            </el-select>
          </div>
        </el-col>
        <el-col :span="4">
          <div style="display: inline-flex; align-items: center">
            <label style="width: 210px;">Unique Project ID</label>
            <el-input
              style="margin-left: 4px"
              size="mini"
              v-model="form.construction_id"
              @change="submitForm">
            </el-input>
          </div>
        </el-col>
      </el-row>
    </el-form-item>
    <el-form-item class="filter-group">
      <el-row :gutter="10">
        <el-col style="margin-left: 4px" :span="7">
          <el-select
            size="mini"
            class="filter-item"
            filterable
            :filter-method="filterAgen"
            @focus="resetAgen"
            v-model="form.funding_agency_id"
            @change="submitForm"
            placeholder="Source of Funding"
            clearable
            value="">
            <el-option
              v-for="item of agencies"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select></el-col>
        <el-col :span="7">
          <el-select
            size="mini"
            class="filter-item"
            filterable
            :filter-method="filterDep"
            @focus="resetDep"
            :disabled="me.hasRole(2) || me.hasRole(6)"
            :value="form.department_id"
            v-model="form.department_id"
            placeholder="Executing Department"
            @change="submitForm"
            clearable>
            <el-option
              v-for="item of departments"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="7">
          <div style="display: inline-flex; align-items: center">
            <label>Dates</label>
            <el-date-picker
              style="margin-left: 4px"
              size="mini"
              v-model="form.from_date"
              @change="submitForm"
              type="date"
              :picker-options="startDateOptions"
              placeholder="Start date">
            </el-date-picker>
            <el-date-picker
              style="margin-left: 4px"
              size="mini"
              v-model="form.to_date"
              @change="submitForm"
              type="date"
              :picker-options="toDateOptions"
              placeholder="End date">
            </el-date-picker>
          </div>
        </el-col>
      </el-row>

    </el-form-item>
    <el-form-item class="filter-group" v-if="isAdmin">
      <el-row :gutter="10">
        <el-col style="margin-left: 4px" :span="7">
          <el-select
            size="mini"
            class="filter-item"
            filterable
            :filter-method="filterUsername"
            @focus="resetAgen"
            v-model="form.username"
            @change="submitForm"
            placeholder="Username"
            clearable
            value="">
            <el-option
              v-for="item of users"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-col>
      </el-row>
    </el-form-item>
    <el-form-item class="filter-group"  label="Project Name">
      <el-input
          style="margin-left: 4px; width: 586px"
          size="mini"
          v-model="form.search"
          @blur="submitForm"
          placeholder="Search project (name)"
          @keyup.enter.native.prevent.stop="submitForm">
        </el-input>
        <el-button
          style="margin-left: 10px"
          size="mini"
          :autofocus="true"
          :loading="loading"
          type="primary"
          icon="el-icon-search"
          @click="submitForm"
          plain>Search</el-button>
        <el-button
          style="margin-left: 10px"
          size="mini"
          :loading="loading"
          type="primary"
          icon="el-icon-refresh"
          @click="$emit('reset')"
          plain>Reset</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
  import api from '@/api'
  import { mapGetters } from 'vuex'
  import { filterArr } from '@/utils/Array'

  export default {
    name: 'filter-form',
    data () {
      return {
        startDateOptions: {
          disabledDate: this.disabledFromDate
        },
        toDateOptions: {
          disabledDate: this.disabledToDate
        },
        users: [],
        _users: [],
        districts: [],
        _districts: [],
        departments: [],
        _departments: [],
        circles: [],
        _circles: [],
        status: ['Ongoing', 'Completed', 'Not Started'],
        _agencies: [],
        agencies: []
      }
    },
    created () {
      api.getFundingAgencies()
          .then(res => {
            this.agencies = res.data
            this._agencies = res.data
          })
      this.initData()
    },
    props: {
      loading: {
        type: Boolean,
        required: true
      },
      value: {
        type: Object,
        required: true
      }
    },
    computed: {
      ...mapGetters([
        'me'
      ]),
      form: {
        get () {
          return this.value
        },
        set (val) {
          this.$emit('input', val)
        }
      },
      isAdmin () { return this.me.roles[0].id === 1 }
    },
    mounted () {
      if (this.me.hasRole(4)) {
        this.form.district = this.me.district
        this.getCircles()
      }
    },
    methods: {
      resetAgen () {
        this.agencies = this._agencies
      },
      resetCir () {
        this.circles = this._circles
      },
      resetDep () {
        this.departments = this._departments
      },
      resetDis () {
        this.districts = this._districts
      },
      filterDis (value) {
        this.districts = filterArr(value, this._districts, 'dist_name')
      },
      filterCir (value) {
        this.circles = filterArr(value, this._circles, 'name')
      },
      filterAgen (value) {
        this.agencies = filterArr(value, this._agencies, 'name')
      },
      filterUsername (value) {
        this.users = filterArr(value, this._users, 'name')
      },
      filterDep (value) {
        this.departments = filterArr(value, this._departments, 'name')
      },
      initData () {
        api.getDistricts()
          .then(res => {
            this.districts = res.data
            this._districts = res.data
          })
        if (this.me.hasRole(2) || this.me.hasRole(6)) {
          this.departments = [this.me.department]
          this._departments = [this.me.department]
          this.form.department_id = this.me.department.id
        } else {
          api.getDepartments()
            .then(res => {
              this.departments = res.data
              this._departments = res.data
            })
        }
        if (this.me.hasRole(1)) {
          api.getUsers()
          .then(res => {
            this.users = res.data.data
            this._users = res.data.data
          })
        }
      },
      disabledFromDate (time) {
        if (this.form.to_date) {
          return time.getTime() > new Date(this.form.to_date)
        }
      },
      disabledToDate (time) {
        if (this.form.from_date) {
          return time.getTime() < new Date(this.form.from_date)
        }
      },
      getCircles () {
        this.form.circle = undefined
        this.circles = []
        this.submitForm()
        if (this.form.district) {
          api.getCircles(this.form.district)
            .then(res => {
              this.circles = res.data
              this._circles = res.data
            })
        }
      },
      submitForm () {
        this.$emit('search')
      }
    }
  }
</script>

<style scoped>
  .filter-group {
    width: 1200px;
  }
  .filter-item {
    width: 100%;
  }
</style>
