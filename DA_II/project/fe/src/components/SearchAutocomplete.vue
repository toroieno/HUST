<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-autocomplete
            v-model="dataSelected"
            :items="datas"
            filled
            chips
            color="blue-grey lighten-2"
            label="Select"
            item-text="name"
            item-value="name"
            multiple
            clearable
        >
          <template v-slot:selection="data">
            <v-chip
                v-bind="data.attrs"
                :input-value="data.selected"
                v-if="data.item.name !== '_Search'"
                close
                @click="data.select"
                @click:close="remove(data.item)"
            >
              {{ data.item.name }}
            </v-chip>
          </template>
          <template v-slot:prepend-item>
            <v-container>
              <v-text-field
                id="search-element"
                v-model="searchInfo"
                placeholder="Search"
              >
              </v-text-field>
            </v-container>
          </template>
          <template v-slot:item="data">
            <template v-if="(typeof data.item !== 'object')">
              <v-list-item-content v-text="data.item"></v-list-item-content>
            </template>
            <template v-else>
              <v-list-item-content >
                <v-list-item-title v-html="data.item.name"></v-list-item-title>
              </v-list-item-content>
            </template>
          </template>
        </v-autocomplete>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      paginate: true,
      page: 1,
      itemsPerPage: 10,
      search: '',
      loading: true,
      skip: 0,
      take: 5,
      step: 5,
      dataToShow: [],
      index: 0,
      limit: 5,
      searchInfo: '',
      dataSelected: [],
      datas: [],
      // currentData: [],
      offsetScroll: 0,
      test_host: 'https://apsdi-admin.eofactory.ai/api/users',
    }
  },

  props: {
    func: Function,
  },

  methods: {
    remove (item) {
      const index = this.dataSelected.indexOf(item.name)
      if (index >= 0) this.dataSelected.splice(index, 1)
    },

    debounce(func, timeout = 1000){
      let timer;
      return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => { func.apply(this, args); }, timeout);
      };
    },

    saveInput(){
      console.log('Saving data');
    },

    async searchingData() {
      this.paginate = true
      this.page = 1
      const data = `?with=roles,createdBy&paginate=${this.paginate}&page=${this.page}&itemsPerPage=${this.itemsPerPage}&search=${this.search}`
      const result = await this.getData(data)

      console.log('result search: ', result.data);
      this.datas = [
        ...result.data,
      ]
    },

    async load() {
      if (this.loading){
        this.page = this.page + 1
        const data = `?with=roles,createdBy&paginate=${this.paginate}&page=${this.page}&itemsPerPage=${this.itemsPerPage}&search=${this.search}`
        
        const result = await this.getData(data)
        // console.log(result.data)
        if (result.data.length > 0){
          this.datas.push(...result.data)
        }else{
          this.paginate = false
        }
      }
    },

    async getData(data='') {
      // const result = await axios.get('http://127.0.0.1:8000/api/test'+ data)
      const result = await axios.get(this.test_host + data)
      return result
    }
  },

  watch: {
    searchInfo(){
      const _this = this
      this.debounce(() => _this.searchingData())()
    }
  },

  computed: {
    dataList() {
      let dL = []
      if (this.searchInfo !== ''){
        this.datas.forEach((data) => {
          if ('name' in data) {
            if (data.name.includes(this.searchInfo) || data.name.toLowerCase().includes(this.searchInfo) || data.name.toUpperCase().includes(this.searchInfo)){
              dL.push(data)
            }
          }else{
            dL.push(data)
          }
        })
      }else{
        dL = this.datas
      }
      return dL
    },
  },

  updated() {
    const elementSelect = document.querySelector('.v-list-item:has(#search-element)')
    if (elementSelect) {
      elementSelect.classList.forEach(e => {
        if (e === 'theme--light'){
          elementSelect.classList.remove('theme--light')
        }
      })
    }
  },

  async mounted() {
    this.func()
    const _this = this
    
    document.documentElement.addEventListener('DOMNodeInserted', function() {
      const scrollTarget = document.querySelector('div[role="listbox"]:has(#search-element)')
      if (scrollTarget !== null){
        const parentElement = scrollTarget.parentElement
        parentElement.addEventListener('scroll', function(el){
          const scrollToBottom = (el.target.scrollTop + el.target.offsetHeight) >= (el.target.scrollHeight - 1)
          if (scrollToBottom && _this.loading){
            _this.load()
            // _this.loading = false
          }
        })
      }
    })
    const data = `?with=roles,createdBy&paginate=${this.paginate}&page=${this.page}&itemsPerPage=${this.itemsPerPage}&search=${this.search}`
    const result = await this.getData(data)
    // console.log('get data: ', this.data);
    this.datas.push(
      ...result.data
    );
    // this.currentData = this.datas
    // console.log('data: ', this.currentData);
  },
}
</script>

<style>
  .v-list-item:has(#select-element) {
    background-color: transparent;
  }
</style>