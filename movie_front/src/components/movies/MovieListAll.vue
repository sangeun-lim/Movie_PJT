<template>
  <div>
    <movie-nav-bar></movie-nav-bar>
    <h2>전체 영화</h2>
    <search-bar></search-bar>
    <body>
    <div class="container">
      <div class="d-flex">
        <movie-card
        v-for="movie in movieData" :key="movie.id" :movie='movie'>
        </movie-card>
      </div>
    </div>
    </body>
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

.container {
  position: absolute;
  height: 300px;
  width: 600px;
  top: 60px;
  /* left: calc(50% - 300px); */
  display: flex;
}

.card {
  display: flex;
  height: 280px;
  width: 200px;
  background-color: #17141d;
  border-radius: 10px;
  box-shadow: -1rem 0 3rem #000;
/*   margin-left: -50px; */
  transition: 0.4s ease-out;
  position: relative;
  left: 0px;
}

.card:not(:first-child) {
    margin-left: -50px;
}

.card:hover {
  transform: translateY(-20px);
  transition: 0.4s ease-out;
}

.card:hover ~ .card {
  position: relative;
  left: 50px;
  transition: 0.4s ease-out;
}

.title {
  color: white;
  font-weight: 300;
  position: absolute;
  left: 20px;
  top: 15px;
}


.stroke {
  stroke: white;
  stroke-dasharray: 360;
  stroke-dashoffset: 360;
  transition: 0.6s ease-out;
}

svg {
  fill: #17141d;
  stroke-width: 2px;
}

.card:hover .stroke {
  stroke-dashoffset: 100;
  transition: 0.6s ease-out;
}
</style>