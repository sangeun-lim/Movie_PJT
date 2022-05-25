<template>
  <div class="m-7">
    <div class="my-5 ms-5 me-3 d-flex justify-content-center row row-cols-6">
      <movie-card
      v-for="movie in randomMovies"
      :movie="movie"
      :key="movie.id"
      class="col mb-7"
      ></movie-card>
    </div>
  </div>

</template>

<script>
  import MovieCard from '@/components/movies/MovieCard.vue'
  import _ from 'lodash'
  import axios from 'axios'

  export default {
    name: 'LikeGenre',
    components: {
      MovieCard,
    },
    props: {
      likeGenreDic : Object
    },
    data () {
      return {
        randomMovies : [],
        likeGenreMovies: [],
      }
    },
    methods: {
      pickRandom () {
        const searchURL = 'http://localhost:8000/api/v1/movies/like_recommend/'
        axios.post(searchURL, this.likeGenreDic)
          .then(res => {
            // console.log(this.likeGenreDic)
            // console.log(res.data)
            this.likeGenreMovies = res.data
            const randomMovie = _.sampleSize(this.likeGenreMovies, 7)
            this.randomMovies = randomMovie
          })
      },
    },
    created () {
      // console.log('component created!')
      this.pickRandom()
    },
  }
</script>

<style>

</style>