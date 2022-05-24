<template>
  <div class="card" style="width: 18rem;">
    <img :src="poster" class="card-img-top" alt="movieImg">
    <div class="card-body">
      <h5 class="fw-bold" @click="moveToDetailMovie">{{ movie.title }}</h5>
      <hr>
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
      this.$router.push({ name: 'movieDetail' , params: { moviePk: `${this.movie.movie_id}`} })
    }
  }
}
</script>

<style>

</style>