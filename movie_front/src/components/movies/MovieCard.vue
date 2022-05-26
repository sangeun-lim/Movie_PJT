<template>
  <div class="card p-0 bg-dark border-dark" style="width: 18rem;">
    <img :src="poster" class="card-img-top a" alt="movieImg" @click="moveToDetailMovie">
      <div class="card-body">
        <p class="text-white fw-bold">{{ movie.title }}<br>{{ movie.released_date }}</p>
        <!-- <p>평점 : {{ movie.vote_avg }}</p> -->
        <div>
          <p style="color: white">
            <i class="fa-solid fa-star fa-1x" style="color: yellow"></i>
            <strong>{{ movie.vote_avg }}</strong>
          </p>
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

  .card-body {
    margin : 10px 50px auto;
  }
  .card .card-body {
    transform: translateY(350%) translateX(-5%);
    opacity: 0;
    transition: 0.3s ease-in-out;
    position: absolute;
    width: 20rem;
    height: 7rem;
    margin: 0;
  }

  .card:hover .card-body {
    transform: translateY(305%) translateX(-5%);
    opacity: 1;
    position: absolute;
    background: rgba(0, 0, 0, 0.5);
    width: 20rem;
    height: 7rem;
    margin: 0;
  }
</style>