<template>
  <div class="card p-0 m-4 bg-dark border-dark" style="width: 18rem;">
    <img :src="poster" class="card-img-top a" alt="movieImg" @click="moveToDetailMovie">
    <div class="card-body">
      <!-- <h3 class="fw-bold" @click="moveToDetailMovie">{{ movie.title }}</h3> -->
      <!-- <hr> -->
      <p>개봉일 : {{ movie.released_date }}</p>
      <p>평점 : {{ movie.vote_avg }}</p>
      <div class="d-flex justify-content-between">
        <p v-for="genre in movie.genres" :key="genre.pk">{{ genre.genre_name }}</p>
      </div>
      <!-- <p class="card-text txt_post">{{ movie.overview }}</p> -->
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'MovieCard',
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
    transform: scale(1.4);
    cursor: pointer;
  }
</style>