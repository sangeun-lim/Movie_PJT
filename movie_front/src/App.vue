<template>
  <div id="app">
    <nav-bar></nav-bar>

    <router-view class="slide-in"/>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'

  import { mapActions } from 'vuex'

  
  export default {
    name: 'App',
    components:{
      NavBar
    },
    methods : {
      ...mapActions(['fetchCurrentUser', 'fetchMovies'])
    },
    created() {
      this.fetchCurrentUser()
      this.fetchMovies()
    }

  }
</script>

<style>
  #app {
    /* font-family: Avenir, Helvetica, Arial, sans-serif; */
    font-family: 'IBM Plex Sans KR', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    font-family: 'IBM Plex Sans KR', sans-serif;
    color: white;
  }

</style>
