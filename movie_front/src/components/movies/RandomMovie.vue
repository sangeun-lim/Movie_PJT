<template>
  <div class="d-flex flex-column justify-content-between">
    <!-- <h4 class="m-3 text-start">{{ getToday() }}요일 </h4> -->
    <h1 class="mt-5 title-font">🎬</h1>
    <!-- <button @click="pickRandom" class="btn btn-outline-success" style="width:300px;"> -->
      <!-- <h3>영화 추천!</h3></button> -->
    <!-- <div class="d-flex justify-content-center">
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
    </div> -->

    <div class="container">
      <div class="carousel">
        <movie-card
          v-for="movie in randomMovies"
          :movie="movie"
          :key="movie.id"
          class="mx-3 carousel__face text-dark"
        ></movie-card>
      </div>
    </div>
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
        const randomMovie = _.sampleSize(this.movieData, 9)
        this.randomMovies = randomMovie
      },
      getToday () {
        const today = new Date()
        const year = today.getFullYear()
        const month = ('0' + (today.getMonth() + 1)).slice(-2)
        const day = ('0' + today.getDate()).slice(-2)

        const week = ['일', '월', '화', '수', '목', '금', '토']

        const date = year + '년 ' + month + '월 ' + day + '일 ' + week[today.getDay()]
        return date
      }
    },
    created() {
      this.pickRandom()
    },
  }
</script>

<style scoped>
  .a:hover {
    transform: scale(1.4);
    cursor: pointer;
  }

  .title-font {
    font-size: 100px;
    font-family: 'Hahmlet', serif;
    font-weight: 900;
  }
  .container {
    position: relative;
    width: 320px;
    margin: 100px auto 0 auto;
    perspective: 3000px;
  }

  .carousel {
    position: absolute;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d; 
    animation: rotate360 50s infinite forwards linear;
  }
  .carousel__face { 
    position: absolute;
    width: 300x;
    height: 187px;
    top: 20px;
    left: 10px;
    right: 10px;
    background-size: cover;
    box-shadow:inset 0 0 0 2000px rgba(0,0,0,0.5);
    display: flex;
  }

  .carousel__face:nth-child(1) {
    transform: rotateY(  0deg) translateZ(430px); }
  .carousel__face:nth-child(2) { 
    transform: rotateY( 40deg) translateZ(430px); }
  .carousel__face:nth-child(3) {
    transform: rotateY( 80deg) translateZ(430px); }
  .carousel__face:nth-child(4) {
    transform: rotateY(120deg) translateZ(430px); }
  .carousel__face:nth-child(5) { 
    transform: rotateY(160deg) translateZ(430px); }
  .carousel__face:nth-child(6) { 
    transform: rotateY(200deg) translateZ(430px); }
  .carousel__face:nth-child(7) { 
    transform: rotateY(240deg) translateZ(430px); }
  .carousel__face:nth-child(8) {
    transform: rotateY(280deg) translateZ(430px); }
  .carousel__face:nth-child(9) {
    transform: rotateY(320deg) translateZ(430px); }

  @keyframes rotate360 {
    from {
      transform: rotateY(0deg);
    }
    to {
      transform: rotateY(-360deg);
    }
  }

</style>