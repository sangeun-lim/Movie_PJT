<template>
  <div class="d-flex flex-column justify-content-center align-items-center">
    <button @click="pickRandom" class="btn btn-outline-success" style="width:300px;">Pick</button>
    <br>
    <div>{{ randomMovies }}</div>
    <!-- <div class="card" style="width: 24rem;" v-if="!!randomTitle">
      <img :src="poster" class="card-img-top" alt="movieImg">
        <div class="card-body">
          <h5 class="fw-bold">{{ randomTitle }}</h5>
          <hr>
          <p>{{ randomOverview }}</p>
        </div>
    </div>
    <div v-else>
      <div>
        <img src=""  alt="Pick">

      </div>
    </div> -->
  </div>
</template>

<script>
// import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name: 'RandomView',
  data () {
    return {
      // randomTitle : null,
      // randomOverview : null,
      // randomPosterPath : null,
      randomMovies : [],
    }
  },
  methods: {
    pickRandom () {
      const randomMovie = _.sampleSize(this.$store.state.movieData, 5)
      // this.randomTitle = randomMovie.title
      // this.randomOverview = randomMovie.overview
      // this.randomPosterPath = randomMovie.poster_path
      this.randomMovies = randomMovie
    }
  },
  // computed: {
  //     poster () {
  //       return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.randomPosterPath}`
  //   }
    // ...mapGetters(['randomMovie'])
    // randomMovie () {
    //   return _.sampleSize(this.$store.state.movieData, 1).join('')
  // }
}
</script>

<style>

</style>