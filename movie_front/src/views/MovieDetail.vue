<template>
  <div>
    <!-- {{movie.title}}
    {{movie.overview}} -->
    <div>
      {{movie.title}}
      <br>
      {{movie.overview}}
      <br>
      {{movie.released_date}}
      <br>
      {{movie.vote_avg}}
      <br>
      {{movie.like_users_count}}
      <br>
      <p v-for="genre in movie.genres" :key="genre.pk">{{ genre.genre_name }}</p>
      <br>
      <p v-for="actor in movie.actors" :key="actor.name">{{actor.name}}</p>
      <br>
      <!-- <img :src="poster" class="card-img-top" alt="movieImg"> -->
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieDetail',
  data() {
    return {
      moviePk: this.$route.params.moviePk
    }
  },
  computed: {
    ...mapGetters(['movie']),
    poster () {
      return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`
    }
  },
  methods: {
    ...mapActions(['fetchMovie', 'likeMovie'])
  },
  created() {
    this.fetchMovie(this.moviePk)
  }
}
</script>

<style>

</style>