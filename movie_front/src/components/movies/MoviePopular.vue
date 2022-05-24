<template>
  <div>
    <movie-nav-bar></movie-nav-bar>
    <h2>인기영화</h2>
    <movie-card
    v-for="movie in popularMovies" :key="movie.id" :movie='movie'>
    </movie-card>
  </div>
</template>

<script>
  import MovieCard from '@/components/movies/MovieCard.vue'
  import MovieNavBar from '@/components/movies/MovieNavBar.vue'
  import { mapGetters } from 'vuex'
  import axios from 'axios'
  import drf from '@/api/drf'

  export default {
    name: 'MoviePopular',
    components: {
      MovieCard,
      MovieNavBar
    },
    data () {
      return {
        popularMovies : [],
      }
    },
    computed: {
      ...mapGetters(['movieData'])
    },
    created () {
      axios({
        url: drf.movies.moviePopular(),
        method: 'get',
      })
        .then(res => {
          // console.log(res.data)
          this.popularMovies = res.data
        })
    },
  }
</script>

<style>

</style>