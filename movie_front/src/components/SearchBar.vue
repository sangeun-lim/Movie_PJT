<template>
  <div>
    <div>
      <input type="text" v-model="searchData.keyword" class="mx-2">
      <button @click="searchMovie">Search</button>
    </div>
    <div class="m-5">
      <div class="my-5 ms-5 me-3 d-flex justify-content-center row row-cols-6">
        <movie-card class="col mb-5"
        v-for="movie in searchMovies" :key="movie.id" :movie='movie'>
        </movie-card>
      </div>
    </div>
<!-- 
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
    </div> -->

    <br>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/movies/MovieCard.vue'
// import drf from '@/api/drf'

export default {
  name: 'searchMovies',
  components: {
    MovieCard
  },
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
 .card {
  display: flex;
  height: 280px;
  width: 200px;
  background-color: #17141d;
  border-radius: 10px;
  box-shadow: -1rem 0 3rem #000;
  margin-left: -50px;
  transition: 0.4s ease-out;
  position: relative;
  left: 0px;
}

.card:not(:first-child) {
    margin-left: -100px;
}

.card:hover {
  transform: translateY(-100px);
  transition: 0.4s ease-out;
}

.card:hover ~ .card {
  position: relative;
  left: 100px;
  transition: 0.4s ease-out;
}

.title {
  color: white;
  font-weight: 300;
  position: absolute;
  left: 20px;
  top: 15px;
}
</style>