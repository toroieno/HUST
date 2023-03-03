<template>
  <v-navigation-drawer
    permanent
    absolute
    temporary
  >
    <v-list>
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <v-img :src="user.img"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            {{ user.name }}
          </v-list-item-title>
          <v-list-item-subtitle>{{ user.email }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list
      nav
      dense
    >
      <v-list-item
        link
        v-for="(item, i) in navbars"
        :key="i"
        :to="item.path"
      >
        <v-list-item-icon>
          <v-icon>{{item.icon}}</v-icon>
        </v-list-item-icon>
        <v-list-item-title>{{item.name}}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
  export default {
    data() {
      return {
        user: {
          name: 'Sandra Adams',
          email: 'sandra_a88@gmail.com',
          img: 'https://randomuser.me/api/portraits/women/85.jpg'
        },
        navbars: [
          {name: 'Home', icon: 'mdi-home', path: '/'},
          {name: 'About', icon: 'mdi-information', path: '/about'},
          {name: 'Contact', icon: 'mdi-account-box', path: '/contact'},
          {name: 'Help', icon: 'mdi-help-circle', path: '/help'},
        ],
        showBar: false,    
      }
    },

    methods: {
      showNavbar(){
        this.showBar = !this.showBar
      }
    },
  }
</script>

<style>
.navbar {
  text-decoration: none;
  color: #000 !important;
}
</style>