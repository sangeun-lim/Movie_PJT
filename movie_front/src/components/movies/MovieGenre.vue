<template>
  <div>
    <movie-nav-bar></movie-nav-bar>
    <h2>장르 선택</h2>
    <select v-model="genreData.selected" @change="selectGenre()" class="form-select" aria-label="Default select example">
      <option :value=28>액션</option>
      <option :value=35>코미디</option>
      <option :value=10749>로맨스</option>
      <option :value=16>애니메이션</option>
      <option :value=12>모험</option>
      <option :value=80>범죄</option>
      <option :value=99>다큐멘터리</option>
      <option :value=18>드라마</option>
      <option :value=10751>가족</option>
      <option :value=14>판타지</option>
      <option :value=27>공포</option>
      <option :value=878>SF</option>
    </select>
      <movie-card
        v-for="movie in genreMovies" :key="movie.id" :movie='movie'>
      </movie-card>
  </div>
</template>

<script>
  import MovieCard from '@/components/movies/MovieCard.vue'
  import MovieNavBar from '@/components/movies/MovieNavBar.vue'
  import { mapGetters } from 'vuex'
  import axios from 'axios'
  // import drf from '@/api/drf'

  export default {
    name: 'MovieGenre',
    components: {
      MovieCard,
      MovieNavBar
    },
    data () {
      return {
        genreData: {
          selected: null,
        },
        genreMovies : [],
      }
    },
    computed: {
      ...mapGetters(['movieData'])
    },
    methods: {
      selectGenre() {
        const searchURL = 'http://localhost:8000/api/v1/movies/genres/'
        axios.post(searchURL, this.genreData)
          .then(res => {
            console.log(this.genreData)
            this.genreMovies = res.data
          })
      },
    },
    // created () {
    //   axios({
    //     url: drf.movies.movieGenre(),
    //     method: 'post',
    //   })
    //     .then(res => {
    //       console.log(res.data)
    //       this.genreMovies = res.data
    //     })
    // },
  }
</script>

<style>

</style>