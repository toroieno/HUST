<template>
  <v-snackbar
    style="z-index: 999"
    v-model="snackBar"
    :timeout="timeout"
    :color="color"
    bottom
    center
    class="text-capitalize"
  >
    {{ text }}
  </v-snackbar>
</template>

<script>
import {mapState} from '@/store/ults'

export default {
  name: 'MessageNotification',
  data: () => ({
    timeout: 3000,
    snackbarColor: 'red'
  }),
  computed: {
    ...mapState('message', ['text', 'snackBar', 'color'])
  },
  mounted() {
  },
  methods: {
  }
}
</script>

<style scoped>

</style>
