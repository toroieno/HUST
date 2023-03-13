<template>
    <v-app :theme="theme">
        <v-sheet class="pa-12" rounded height="840">
            <v-container>
                <div class="d-flex justify-center mb">
                    <p class="text-h1"><b>404</b></p>
                </div>
                <div class="d-flex justify-center mb">
                    <p class="text-h3"><span class="text-red">Oops!</span> Page Not Found</p>
                </div>
    
                <div class="d-flex justify-center">
                    <v-btn color="primary" prepend-icon="mdi-home" size="large" @click="home">Back to Home</v-btn>
                </div>
            </v-container>
        </v-sheet>
    </v-app>
</template>

<script>
export default {
    data:() => ({
        theme: localStorage.getItem('theme')
    }),
    methods: {
        home() {
            this.$router.push('/')
        }
    }
}
</script>

<style scoped>
.mb {
    margin-bottom: 20px;
}
.text-h1 {
    font-weight: bold;
}
</style>