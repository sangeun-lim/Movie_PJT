<template>
  <div>
    <movie-card
    v-for="movie in movieData" :key="movie.id" :movie='movie'>
    </movie-card>
  </div>
</template>

<script>
  import MovieCard from '@/components/movies/MovieCard.vue'

  import { mapGetters } from 'vuex'

  export default {
    name: 'MovieListAll',
    components: {
      MovieCard,
    },
    computed: {
      ...mapGetters(['movieData'])
    }
  }
</script>

<style>

</style>