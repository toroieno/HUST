<template>
    <v-app :theme="theme">
        <v-sheet class="pa-12" rounded height="840">
            <v-container>
                <div class="d-flex justify-center mb">
                    <p class="text-h1"><b>403</b></p>
                </div>
                <div class="d-flex justify-center">
                    <p class="text-h3"><span class="text-red">Error !</span> Forbidden</p>
                </div>
                <div class="d-flex justify-center mb">
                    <p class="text-h6 text-center">A web server may return a 403 Forbidden HTTP status code in response to a request from a client for a web page or resource to indicate that the server can be reached and understood the request, but refuses to take any further action. Status code 403 responses are the result of the web server being configured to deny access, for some reason, to the requested resource by the client.</p>
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
    data() {
        return {
            theme: localStorage.getItem('theme')
        }
    },
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