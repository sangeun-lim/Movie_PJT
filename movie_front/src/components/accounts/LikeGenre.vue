<template>
  <div class="m-4">
    <div class="my-5 ms-5 me-3 d-flex justify-content-center row row-cols-6">
      <movie-card
      class="col"
      v-for="movie in randomMovies"
      :movie="movie"
      :key="movie.id"
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

<style scoped>
 .card {
  display: flex;
  height: 50%;
  width: 50%;
  background-color: #17141d;
  border-radius: 10px;
  /* box-shadow: -1rem 0 3rem #000; */
  margin-left: -50px;
  transition: 0.4s ease-out;
  position: relative;
  left: 0px;
}

.card:not(:first-child) {
    margin-left: -100px;
}

.card:hover {
  transform: translateY(-140px);
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