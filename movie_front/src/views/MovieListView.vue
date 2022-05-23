<template>
  <div>
    <h1>Movie List</h1>
    <search-bar></search-bar>
    <p>genre</p>
    <movie-genre></movie-genre>
    <hr>
    <p>popular</p>
    <movie-popular></movie-popular>
    <hr>
    <p>all</p>
    <movie-list-all></movie-list-all>
  </div>
</template>

<script>
  import SearchBar from '@/components/SearchBar.vue'
  import MovieListAll from '@/components/movies/MovieListAll.vue'
  import MoviePopular from '@/components/movies/MoviePopular.vue'
  import MovieGenre from '@/components/movies/MovieGenre.vue'
 
  export default {
    name: 'MovieListView',
    components: {
      SearchBar, MovieListAll, MoviePopular, MovieGenre
    },
    // created() {
    //   this.$store.dispatch('fetchMovies')
    // },
  }
</script>

<style>

</style>