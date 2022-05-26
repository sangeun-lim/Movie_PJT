<template>

    <!-- <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
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
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
      </button>
    </div> -->
    <div class="m-4">
      <div class="my-5 ms-5 me-3 d-flex justify-content-center row row-cols-6">
        <movie-card 
        class="col"
        v-for="movie in likeMovies" 
        :key="movie.id" 
        :movie='movie'>
        </movie-card>
      </div>
    </div>

</template>

<script>

import MovieCard from '../movies/MovieCard.vue'

export default {
  name: 'LikeMovies',
  components: {
    MovieCard
  },
  props: {
    likeMovies : Array
  },

}
</script>

<style scoped>
 .card {
  display: flex;
  height: 50%;
  width: 50%;
  background-color: #17141d;
  border-radius: 10px;
  box-shadow: -1rem 0 3rem #000;
  margin-left: -50px;
  transition: 0.4s ease-out;
  position: relative;
  left: 0px;
}

.card:not(:first-child) {
    margin-left: -100px;
}

.card:hover {
  transform: translateY(-140px);
  transition: 0.7s ease-out;
}

.card:hover ~ .card {
  position: relative;
  left: 100px;
  transition: 0.7s ease-out;
}

.title {
  color: white;
  font-weight: 300;
  position: absolute;
  left: 20px;
  top: 15px;
}
</style>