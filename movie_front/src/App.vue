<template>
  <div id="app">
    <nav-bar></nav-bar>
    <!-- <nav> -->
      <!-- <router-link to="/">Home</router-link> | -->
      <!-- <router-link to="/about">About</router-link> -->
    <!-- </nav> -->
    <router-view/>
  </div>
</template>

<script>
  // import NavBar from '@/components/NavBar.vue'
  
  export default {
    name: 'App',
    components:{
      // NavBar
    },
    methods : {

    },
    created() {

    }

  }
</script>

<style>

</style>
