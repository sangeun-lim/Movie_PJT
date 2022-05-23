<template>
  <div class="d-flex flex-column justify-content-between align-items-center">
    <h3>{{ getToday() }}요일 </h3>
    <button @click="pickRandom" class="btn btn-outline-success" style="width:300px;">
      <h3>영화 추천!</h3></button>
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
    },
    getToday () {
      const today = new Date()
      const year = today.getFullYear()
      const month = ('0' + (today.getMonth() + 1)).slice(-2)
      const day = ('0' + today.getDate()).slice(-2)

      const week = ['일', '월', '화', '수', '목', '금', '토']

      const date = year + '-' + month + '-' + day + ' ' + week[today.getDay()]
      return date
    }
  },
  created() {
    this.pickRandom()
  },

}
</script>

<style>

</style>