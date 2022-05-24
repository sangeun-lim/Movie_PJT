<template>
  <div>
    <movie-nav-bar></movie-nav-bar>
    <h2>전체 영화</h2>
    <search-bar></search-bar>
    <movie-card
    v-for="movie in movieData" :key="movie.id" :movie='movie'>
    </movie-card>
  </div>
</template>

<script>
  import MovieCard from '@/components/movies/MovieCard.vue'
  import MovieNavBar from '@/components/movies/MovieNavBar.vue'
  import SearchBar from '@/components/SearchBar.vue'

  import { mapGetters } from 'vuex'

  export default {
    name: 'MovieListAll',
    components: {
      MovieCard,
      MovieNavBar,
      SearchBar
    },
    computed: {
      ...mapGetters(['movieData'])
    }
  }
</script>

<style>

</style>