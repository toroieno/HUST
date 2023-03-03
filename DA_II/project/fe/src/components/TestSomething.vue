<template>
  <div>
    <h1>something</h1>
    <!-- <ul>
      <router-link :to="{name: 'HomePage'}" tag="button">Home</router-link>
      <router-link :to="{name: 'AboutPage'}" tag="button">About</router-link>
    </ul>
    {{ data }}
    <v-btn color="primary">button by vuetify</v-btn>
    <v-icon>mdi-earth</v-icon>
    <button @click="increment()">click me</button> -->
    <v-btn @click="toLocalStorage()">localstorage</v-btn>
    <v-btn @click="toSessionStorage()">sessionstorage</v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: 20,
      HomePage: {
        name: 'HomePage',
        path: '/something',

      }
    }
  },
  methods: {
    toLocalStorage(){ 
      window.localStorage.setItem('test', '1234')
    },
    toSessionStorage(){
      window.sessionStorage.setItem('test', '1234')
    }
  },
  mounted() {
    // console.log(this.$store.state.count)
  },
}
</script>
