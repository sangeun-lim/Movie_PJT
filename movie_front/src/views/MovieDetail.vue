<template>
  <div>
    <!-- {{movie.title}}
    {{movie.overview}} -->
    <ul>
      <li>
      <img :src="poster" class="card-img-top" alt="movieImg" style="width: 25vw; min-width: 140px;">

      </li>
      <br>
      <p>
        {{movie.title}}
      </p>
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
      <movie-video :title="movie.title"></movie-video>
      
      <div v-if="isLoggedIn">
        <div>
        Likeit:
          <button
            @click="likeMovie(moviePk)"
          >{{ likeCount }}</button>
        </div>
        <br>
      </div>

      <movie-comment :comments="movie.comments"></movie-comment>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieVideo from '@/components/movies/MovieVideo.vue'
import MovieComment from '@/components/movies/MovieComment.vue'

export default {
  name: 'MovieDetail',
  components: {
    MovieVideo, MovieComment
  },
  data() {
    return {
      moviePk: this.$route.params.moviePk
    }
  },
  computed: {
    ...mapGetters(['movie', 'isLoggedIn']),
    poster () {
      return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`
    },
    likeCount() {
      return this.movie.like_users?.length
    }
  },
  methods: {
    ...mapActions(['fetchMovie', 'likeMovie']),
  },
  // created() {
  //   this.fetchMovie(this.moviePk)
  // }
}
</script>

<style>

</style>