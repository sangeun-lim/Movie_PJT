<template>
  <div>
    <movie-nav-bar></movie-nav-bar>
    <h2 class="m-4">인기영화</h2>
    <hr>
    <!-- <movie-card
    v-for="movie in popularMovies" :key="movie.id" :movie='movie'>
    </movie-card> -->
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
</style>