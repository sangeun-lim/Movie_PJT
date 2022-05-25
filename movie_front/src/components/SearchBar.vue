<template>
  <div>
    <div>
      <input type="text" v-model="searchData.keyword" class="mx-2">
      <button @click="searchMovie">Search</button>
    </div>

    <div class="row" >
      <div class="col-12 col-md-6 col-lg-3 my-3" v-for="movie in searchMovies" :key="movie.id">
        <div class="card shadow" style="width: 16rem;">
          <img @click="onMovieSelect(movie)" :movie="movie" :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`" class="card-img-top" alt="movie.title">
          <div class="card-body">
            <h4 class="card-title text-dark" >{{ movie.title }}</h4>
            <hr>
            <h6 class="card-text text-secondary">{{ movie.released_date }}</h6>
          </div>
        </div>
      </div>
    </div>
    <br>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
// import drf from '@/api/drf'

export default {
  name: 'searchMovies',
  data() {
    return {
      searchMovies: [],
      searchData: {
        keyword: null,
      }
    }
  },
  methods: {
    searchMovie() {
      const searchURL = 'http://localhost:8000/api/v1/movies/search/'
      axios.post(searchURL, this.searchData)
      .then(res => {
        this.searchMovies = res.data
      })
    },
    onMovieSelect(movie) {
      this.$router.push(`/movie/${movie.id}`)
    },
  },
  mounted() {
    this.searchData.keyword = this.$route.params.keyword
    // this.searchMovie()
  }
}
</script>

<style scoped>
 img:hover {
   transform: scale(1.1);
   cursor:pointer;
 }
</style>