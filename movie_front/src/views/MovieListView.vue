<template>
  <div>
    <router-link to="/">Home</router-link>
    <h1>Movie List</h1>
    <search-bar></search-bar>
    <div>
      <movie-card
      v-for="movie in movieData" :key="movie.id" :movie='movie'>
      </movie-card>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import MovieCard from '@/components/movies/MovieCard.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieListView',
  components: {
    MovieCard, SearchBar
  },
  created() {
    this.$store.dispatch('fetchMovies')
  },
  computed: {
    ...mapGetters(['movieData'])
  }
}
</script>

<style>

</style>