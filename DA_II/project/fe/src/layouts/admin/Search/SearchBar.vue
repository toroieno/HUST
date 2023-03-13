<template>
  <form action="#">
    <label :data-state="state">
      <input type="text" placeholder="Search" @click="state = 'open'" @blur="state='close'"/>
      <v-icon :color="light.iconColor" size="28">mdi-magnify</v-icon>
    </label>
  </form>
</template>

<script>
import { light } from '@/config';

export default {
  name: 'SearchBar',
  data(){
    return {
      light,
      state: "close"
    }
  },
}

</script>

<style src="./Search.scss" lang="scss"></style>


