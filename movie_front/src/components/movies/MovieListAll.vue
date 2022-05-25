<template>
  <div>
    <movie-nav-bar></movie-nav-bar>
    <h2 class="m-4">전체 영화</h2>
    <hr>
    <search-bar></search-bar>
    <div class="m-5">
      <div class="my-5 ms-5 me-3 d-flex justify-content-center row row-cols-6">
        <movie-card class="col mb-5"
        v-for="movie in movieData" :key="movie.id" :movie='movie'>
        </movie-card>
      </div>
    </div>
  </div>
</template>


<script>
  import MovieCard from '@/components/movies/MovieCard.vue'
  import MovieNavBar from '@/components/movies/MovieNavBar.vue'
  import SearchBar from '@/components/SearchBar.vue'

  import { mapGetters } from 'vuex'

  export default {
    name: 'MovieListAll',
    components: {
      MovieCard,
      MovieNavBar,
      SearchBar
    },
    computed: {
      ...mapGetters(['movieData'])
    }
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