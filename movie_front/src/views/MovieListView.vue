<template>
  <div>
    <h1>Movie List</h1>
    <div>
      <movie-card
      v-for="movie in movieData" :key="movie.id" :movie='movie'>
      </movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/movies/MovieCard.vue'

export default {
  name: 'MovieListView',
  components: {
    MovieCard
  },
  created() {
    this.$store.dispatch('fetchMovies')
  },
  computed: {
    movieData() {
      return this.$store.state.movieData
    }
  }
}
</script>

<style>

</style>