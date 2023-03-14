<template>
  <v-card color="basil">
    <v-tabs
      v-model="tab"
      background-color="transparent"
      color="basil"
      grow
    >
      <v-tab
        v-for="(item, i) in navbars"
        :key="i"
        @click="toRouter(item.path)"
      >
        <v-menu
          transition="slide-y-transition"
        >
          <template v-slot:activator="{ props }">
            {{ item.name }}
            {{ props }}
            <v-icon v-if="item.items">
              mdi-triangle-small-down
            </v-icon>
          </template>
          <v-list>
            <v-list-item
              v-for="(item, i) in item.items"
              :key="i"
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
              <router-link :to="item.path" class="navbar">{{ item.title }}</router-link>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-tab>
    </v-tabs>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
        tab: null,
        navbars: [
          {name: 'Trang chủ', path: '/home'},
          {name: 'Thông tin cá nhân', path: '/student/informations'},
          {name: 'Tạo CV', path: '/cv'},
          {name: 'Đồ án', path: '/project_register', items: [{title: 'Thông tin đề tài đồ án'}, {title: 'Điền form đăng ký'}]},
          {name: 'Thực tập', path: '/intern_register', items: [{title: 'Thông tin thực tập'}, {title: 'Điền form đăng ký'}]},
          {name: 'Liên hệ giảng viên', path: '/contact_lecturer'},
          {name: 'Tư vấn học tập', path: '/advise_learning'},
        ]     
      }
    },

    methods: {
      toRouter(path){
        this.$router.push({path}).catch(error => {
          if (
            error.name !== 'NavigationDuplicated' &&
            !error.message.includes('Avoided redundant navigation to current location')
          ) {
            console.log(error)
          }
        })
      }
    },
  }
</script>

<style>
/* Helper classes */
.basil {
  background-color: transparent !important;
}
.basil--text {
  color: #2e2d29 !important;
}
.navbar {
  text-decoration: none;
  color: #2e2d29 !important;
}
</style>