<template>
  <div class="container">
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
        </div>
       <movie-card-two 
        v-for="movie in likeMovies" 
        :key="movie.id"
        :movie='movie'>
        </movie-card-two>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <!-- <span class="text-dark">Previous</span> -->
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <!-- <span class="text-dark">Next</span> -->
      </button>
    </div>
  </div>
</template>

<script>

import MovieCardTwo from '../movies/MovieCardTwo.vue'

export default {
  name: 'LikeMovies',
  components: {
    MovieCardTwo
  },
  props: {
    likeMovies : Array
  },

}
</script>

<style scoped>
 
</style>