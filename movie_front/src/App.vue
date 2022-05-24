<template>
  <div id="app">
    <nav-bar></nav-bar>

    <router-view/>
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
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    background-image: url('@/assets/background.png');
    background-size: cover;
    font-family: 'Gamja Flower', cursive;
    color: white;
    height: 100vh;
  }
</style>
