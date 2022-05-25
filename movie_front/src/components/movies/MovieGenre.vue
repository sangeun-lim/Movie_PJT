<template>
  <div>
    <movie-nav-bar></movie-nav-bar>
    <!-- <h2 class="m-4">장르별 영화</h2> -->
    <h1 class="neon" data-text="U">S<span class="flicker-slow">EL</span>EC<span class="flicker-fast">T</span> BY GEN<span class="flicker-slow">R</span>E</h1>
    <br>
    <form>
      <label for=""></label>
      <select v-model="genreData.selected" @change="selectGenre()" >
        <!-- <option disabled >-- 선택하세요 --</option> -->
        <option :value=28>액션</option>
        <option :value=35>코미디</option>
        <option :value=10749>로맨스</option>
        <option :value=16>애니메이션</option>
        <option :value=12>모험</option>
        <option :value=80>범죄</option>
        <option :value=99>다큐멘터리</option>
        <option :value=18>드라마</option>
        <option :value=10751>가족</option>
        <option :value=14>판타지</option>
        <option :value=27>공포</option>
        <option :value=878>SF</option>
      </select>
    </form>
    <hr>
    <div class="m-5">
      <div class="my-5 ms-5 me-3 d-flex justify-content-center row row-cols-6">
        <movie-card class="col"
        v-for="movie in genreMovies" :key="movie.id" :movie='movie'>
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
  // import drf from '@/api/drf'

  export default {
    name: 'MovieGenre',
    components: {
      MovieCard,
      MovieNavBar
    },
    data () {
      return {
        genreData: {
          selected: null,
        },
        genreMovies : [],
      }
    },
    computed: {
      ...mapGetters(['movieData'])
    },
    methods: {
      selectGenre() {
        const searchURL = 'http://localhost:8000/api/v1/movies/genres/'
        axios.post(searchURL, this.genreData)
          .then(res => {

            this.genreMovies = res.data
          })
      },
    },
  }
</script>

<style scoped>
/* select */
select {
  /* -moz-appearance: none;
	-webkit-appearance: none;
	appearance: none; */

  color: white;
  background-color: black;

  padding: 0.6em 1.4em 0.5em 0.8em;
  margin: 0;
  width: 200px;

  border: 2px solid #f7b5f2;
  border-radius: 1em;
  box-shadow: 0 0 7px 4px #f7b5f2, 0 0 7px 4px #f7b5f2 inset;
}

select:hover {
  border-color: #d42cca;
}

select:focus {
  border-color: #d42cca;
  box-shadow: 0 0 1px 3px rgba(0, 0, 0, 0.7);
  box-shadow: 0 0 7px 4px #d42cca, 0 0 7px 4px #d42cca inset;
  color: white;
  outline: none;
}

select:disabled {
  opacity: 0.5;
}

option {
  color: white;
  font-size: 17px;
}


/* card */
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
  transform: translateY(-130px);
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