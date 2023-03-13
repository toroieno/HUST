<template>
    <v-app class="pa-6">
        <HeaderView />
        <SidebarView />
        <v-main class="content">
            <router-view />
            <FooterView />
        </v-main>
    </v-app>
</template>

<script>
    import HeaderView from '@/layouts/admin/Header/HeaderView';
    import SidebarView from '@/layouts/admin/Sidebar/SidebarView';
    import FooterView from "@/layouts/admin/Footer/FooterView";
    import './Layout.scss';

    export default {
        name: 'LayoutBar',
        components: {FooterView, HeaderView, SidebarView },
    };
</script>

<style src="./Layout.scss" lang="scss" />
