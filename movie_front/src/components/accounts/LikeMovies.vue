<template>
  <div class="d-flex">
    <movie-card v-for="movie in likeMovies" 
    :key="movie.id"
    :movie='movie'>
    </movie-card>
  </div>
</template>

<script>
import MovieCard from '@/components/movies/MovieCard.vue'

export default {
  name: 'LikeMovies',
  components: {
    MovieCard
  },
  props: {
    likeMovies : Array
  },
  // methods: {
  //   likegenre () {
  //     console.log(this.movie)
  //   }
  // },
  // created () {
  //   this.likegenre()
  // }
}
</script>

<style>

</style>