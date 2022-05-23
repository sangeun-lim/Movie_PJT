<template>
  <div class="d-flex flex-column justify-content-between align-items-center">
    <button @click="pickRandom" class="btn btn-outline-success" style="width:300px;">Pick</button>
    <br>
    <div class="d-flex justify-content-center">
      <div class="col-12">
        <div class="row">
          <movie-card
          v-for="movie in randomMovies"
          :movie="movie"
          :key="movie.id"
          class="mx-3"
          ></movie-card>
        </div>
      </div>
    </div>
    <!-- <div>
    <div class="card" style="width: 24rem;">
      <img :src="poster" class="card-img-top" alt="movieImg">
        <div class="card-body">
          <h5 class="fw-bold">{{ randomTitle }}</h5>
          <hr>
          <p>{{ randomOverview }}</p>
        </div>
    </div>
    </div> -->

  </div>
</template>

<script>
import MovieCard from '@/components/movies/MovieCard.vue'
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name: 'RandomView',
  components: {
    MovieCard,
  },
  data () {
    return {
      randomMovies : [],
    }
  },
  computed: {
    ...mapGetters(['movieData'])
  },
  methods: {
    pickRandom () {
      const randomMovie = _.sampleSize(this.movieData, 5)
      this.randomMovies = randomMovie
    }
  },
  created() {
    this.pickRandom()
  },

}
</script>

<style>

</style>