<template>
  <v-app class="container">
    <HeaderLogo />
    <div class="header-bar pl-15 pr-15">
      <HeaderBar />
    </div>
    <v-main>
      <router-view></router-view>
    </v-main>
    <FooterMain />
  </v-app>
</template>

<script>
import HeaderLogo from '@/layouts/student/HeaderLogo.vue';
import FooterMain from '@/layouts/student/FooterMain.vue';
import HeaderBar from '@/layouts/student/HeaderBar.vue';


export default {
    name: "App",
    data: () => ({
      navbar: false,
      datas: [
      ],
    }),

    components: {
      HeaderLogo,
      FooterMain,
      HeaderBar,
    },

    methods: {
    },  

    async mounted() {
    },
};
</script>