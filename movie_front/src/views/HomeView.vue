<template>
  <div>
    <h1>Movie</h1>
    <router-link to="/movies">Movies</router-link>
    <!-- Search Bar -->

    <!-- Movie Recommend -->
    <div>
      <!-- 오늘의 요일 넣기 -->
      <h3>요일 영화 추천</h3>
      <!-- card 5개 (영화 포스터 / 제목 / 평점 / 개봉날짜 / 줄거리(커서)) -->
      <div>
        <movie-card></movie-card>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import MovieCard from '@/components/movies/MovieCard.vue'

  export default {
    name: 'HomeView',
    components: {
      MovieCard,
    },
    computed: {
      ...mapGetters(['movies'])
    },
    methods: {
      ...mapActions(['fetchMovies'])
    },
    created() {
      this.fetchMovies()
    }
  }
</script>

<style>

</style>