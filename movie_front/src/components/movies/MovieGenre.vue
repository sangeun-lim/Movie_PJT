<template>
  <div>
    <select v-model="genreData.selected" @change="selectGenre()" class="form-select" aria-label="Default select example">
      <option selected>Open this select genre</option>
      <option :value=28>액션</option>
      <option :value=35>코미디</option>
      <option :value=10749>로맨스</option>
    </select>
    <movie-card
    v-for="movie in genreMovies" :key="movie.id" :movie='movie'>
    </movie-card>
  </div>
</template>

<script>
  import MovieCard from '@/components/movies/MovieCard.vue'

  import { mapGetters } from 'vuex'
  import axios from 'axios'
  // import drf from '@/api/drf'


  export default {
    name: 'MovieGenre',
    components: {
      MovieCard,
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
            console.log(res.data)
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