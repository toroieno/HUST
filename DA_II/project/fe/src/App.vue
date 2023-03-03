<template>
  <v-app class="container">
    <HeaderLogo />
    <div class="header-bar pl-15 pr-15">
      <!-- <HeaderBar /> -->
      <HeaderBarStudent />
    </div>
    <v-main>
      <router-view></router-view>
    </v-main>
    <FooterMain />
  </v-app>
</template>

<script>
import { test_st } from '@/test'; 
// import HeaderBar from './components/HeaderBar.vue';
import HeaderLogo from './components/HeaderLogo.vue';
import FooterMain from './components/FooterMain.vue';
import HeaderBarStudent from './components/HeaderBarStudent.vue';


export default {
    name: "App",
    data: () => ({
      navbar: false,
      datas: [
      ],
    }),

    components: {
      // HeaderBar,
      HeaderLogo,
      FooterMain,
      HeaderBarStudent,
    },

    methods: {
      test(){
        test_st()
      },
      showNavbar(){
        this.navbar = !this.navbar
        console.log(this.navbar);
      }
    },  

    async mounted() {
    },
};
</script>
<style scoped>
.header-bar {
  border: 1px solid transparent;
}
</style>