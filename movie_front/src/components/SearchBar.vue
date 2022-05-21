<template>
  <div>
    <div>
      <!-- <h4 class="mt-3 text-left">검색어 : {{ searchData.keyword }}</h4> -->
      <input type="text" v-model="searchData.keyword">
      <button @click="searchMovie">Search</button>
    </div>
     <div class="row" >
      <div class="col-12 col-md-6 col-lg-3 my-3" v-for="movie in searchMovies" :key="`movie_${movie.id}`">
        <div class="card jhyuk-img shadow" style="width: 16rem;">
          <!-- <img @click="onMovieSelect(movie)" :movie="movie" :src="movie.poster" class="card-img-top" alt="movie.title"> -->
          <div class="card-body">
            <h4 class="card-title">{{ movie.title }}</h4>
            <h6 class="card-text text-secondary">{{ movie.release_date }}</h6>
          </div>
        </div>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'

export default {
  name: 'SearchBar',
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
      // const searchURL = drf.movies.search()
      console.log(this.searchData.keyword)
      axios({
        url: drf.movies.search(),
        method: 'post',
      })
        .then(res => {
          this.searchMovies = res.data
          console.log(res.data)
        })
    },
    // onMovieSelect(movie) {
    //   this.$router.push(`/movie/${movie.id}`)
    // },
  },
  // mounted() {
  //   this.searchData.keyword = this.$route.params.keyword
  //   // this.searchMovie()
  // }
}
</script>

<style>

</style>