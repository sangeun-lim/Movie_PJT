<template>
  <div>
    <div v-if="isLoggedIn">
      <div>
        <random-movie></random-movie>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import RandomMovie from '@/components/movies/RandomMovie.vue'

  // import axios from 'axios'


  export default {
    name: 'HomeView',
    components: {
      RandomMovie,
    },
    computed: {
      ...mapGetters(['movies', 'isLoggedIn'])
    },
    methods: {
      ...mapActions(['fetchMovies']),
    },
    created() {
      this.fetchMovies()
    },
  }
</script>

<style>

</style>