<template>
  <div>
    <movie-nav-bar></movie-nav-bar>
    <!-- <h2 class="m-4">인기영화</h2> -->
    <h1 class="neon" data-text="U">P<span class="flicker-slow">OP</span>ULA<span class="flicker-fast">R</span> MOV<span class="flicker-slow">I</span>E</h1>
    <br>
    <div class="m-5">
      <div class="my-5 ms-5 me-3 d-flex justify-content-center row row-cols-6">
        <movie-card class="col"
        v-for="movie in popularMovies" :key="movie.id" :movie='movie'>
        </movie-card>
      </div>
    </div>
  </div>
</template>

<script>
  import MovieCard from '@/components/movies/MovieCard.vue'
  import MovieNavBar from '@/components/movies/MovieNavBar.vue'
  import { mapGetters } from 'vuex'
  import axios from 'axios'
  import drf from '@/api/drf'

  export default {
    name: 'MoviePopular',
    components: {
      MovieCard,
      MovieNavBar
    },
    data () {
      return {
        popularMovies : [],
      }
    },
    computed: {
      ...mapGetters(['movieData'])
    },
    created () {
      axios({
        url: drf.movies.moviePopular(),
        method: 'get',
      })
        .then(res => {
          // console.log(res.data)
          this.popularMovies = res.data
        })
    },
  }
</script>

<style scoped>

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

.neon {
  /* font-family: "Monoton", cursive; */
  font-size: 50px;
  color: #ffd5ff;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, 30%);
  font-weight: 400;
  letter-spacing: 8px;
  text-shadow: 1px 0px 4px #ffd5ff, 2px 0px 4px #ffd5ff, 3px 0px 4px #ffd5ff, 2px 0px 3px #d42cca, 2px 3px 15px #d42cca, 2px 0px 15px, 5px 0px 125px, 20px 0vw 200px #d42cca, 40px 0vw 200px #d42cca;
}

.flicker-slow {
  animation: flicker 3s linear infinite;
}

.flicker-fast {
  animation: flicker 1s linear infinite;
}

@keyframes flicker {
    0%, 19.999%, 22%, 62.999%, 64%, 64.999%, 70%, 100% {
    opacity: 0.99;
  }
    20%, 21.999%, 63%, 63.999%, 65%, 69.999% {
    opacity: 0.4;
  }
}
</style>