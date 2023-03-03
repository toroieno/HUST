<template>
  <div class="infinite-list-wrapper" style="overflow:auto">
    <InfiniteLoading 
      v-if="isLoad" 
      direction="bottom" 
      @infinite="infiniteHandler"
      :identifier="infiniteIndex"
    >
      <div slot="no-more"></div>
      <div slot="no-results"></div>
      <v-progress-circular width="3" slot="spinner" indeterminate color="navbar"></v-progress-circular>
    </InfiniteLoading>
    <InfiniteScroll>
      
    </InfiniteScroll>
  </div>
</template>

<script>
import {InfiniteLoading, InfiniteScroll} from 'vue-infinite-loading'
  export default {
    data () {
      return {
        isLoad: true,
      }
    },
    components: {
      InfiniteLoading,
      InfiniteScroll
    },
    computed: {
      
    },
    methods: {
      
    },
    mounted() {
      
    }
  }
</script>

