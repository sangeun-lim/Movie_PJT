<template>
  <div class="carousel-item">
    <div class="card bg-dark border-dark" style="width: 18rem;">
      <img :src="poster" alt="movieImg" @click="moveToDetailMovie">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.vote_avg }}</p>
      </div>
    </div> 
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'MovieCardTwo',
  props: {
    movie: Object,
  },
  computed: {
    poster () {
      return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`
    }
  },
  methods: {
    ...mapActions(['fetchMovie']),
    moveToDetailMovie() {
      this.fetchMovie(this.movie.movie_id)
    }
  }
}
</script>

<style>
  .a:hover {
    transform: scale(1.1);
    cursor: pointer;
  }

</style>