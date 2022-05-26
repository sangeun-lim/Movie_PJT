<template>
  <div class="card p-0 bg-dark border-dark" style="width: 18rem;">
    <img :src="poster" class="card-img-top a" alt="movieImg" @click="moveToDetailMovie">
    <div class="card-body">
        <p>개봉일 : {{ movie.released_date }}</p>
        <p>평점 : {{ movie.vote_avg }}</p>
        <div>
          <p style="color: black "><i class="fa-solid fa-star fa-2x" style="color: yellow">
            </i><strong>
            {{ movie.vote_avg }}
            </strong>
            </p>
        </div>
      <div class="d-flex justify-content-between">
        <p v-for="genre in movie.genres" :key="genre.pk">{{ genre.genre_name }}</p>
      </div>
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
    transform: scale(1.1);
    cursor: pointer;
  }

  .card .card-body {
    transform: translateY(100%);
    opacity: 0;
    transition: 0.3s ease-in-out;
  }

  .card:hover .card-body {
    transform: translateY(0);
    opacity: 1;
    position: absolute;
  }
</style>