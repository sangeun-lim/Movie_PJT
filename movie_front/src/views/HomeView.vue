<template>
  <div>
    <div v-if="isLoggedIn">
      <!-- Search Bar -->
      <!-- Movie Recommend -->
      <div>
        <!-- card 5개 (영화 포스터 / 제목 / 평점 / 개봉날짜 / 줄거리(커서)) -->
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