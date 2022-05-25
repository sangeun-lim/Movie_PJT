<template>
  <div>
    <!-- {{movie.title}}
    {{movie.overview}} -->
    <ul>
      <li>
      <img :src="poster" class="card-img-top" alt="movieImg" style="width: 25vw; min-width: 140px;">

      </li>
      <br>
      <p>
        {{movie.title}}
      </p>
      <br>
      {{movie.overview}}
      <br>
      {{movie.released_date}}
      <br>
      {{movie.vote_avg}}
      <br>
      {{movie.like_users_count}}
      <br>
      <p v-for="genre in movie.genres" :key="genre.pk">{{ genre.genre_name }}</p>
      <br>
      <p v-for="actor in movie.actors" :key="actor.name">{{actor.name}}
        <!-- <img src="https://www.themoviedb.org/t/p/original{{actor.profile_path}}">{{actor.profile_path}}</p> -->
      <br>
      <!-- <movie-video :title="movie.title"></movie-video> -->
      
      <div class="movie-card">
        <div class="poster-wrapper">
          <div class="poster">
            <img :src="poster" alt="poster" />
          </div>
        </div>
        <!-- end poster-wrapper -->
        <div class="movie-info text-start">
          <div class="header-section">
            <h2 class="fw-bold">{{movie.title}}</h2>
            <div class="d-flex">
              <p v-for="genre in movie.genres" :key="genre.pk">| {{ genre.genre_name }} |</p>
            </div>
            <div class="extra">
              <div class="ratings"><p>평점 : {{movie.vote_avg}}</p></div>
            </div>
          </div>
          <div class="cast-section">
            <h3 class="fw-bold">THE CAST</h3>
            <div class="casts">
              <!-- <p v-for="actor in movie.actors" :key="actor.name">
                <img src="https://www.themoviedb.org/t/p/original{{actor.profile_path}}" alt="avatar" />
              </p> -->
              <img src="https://m.media-amazon.com/images/M/MV5BNDg4OTczODE5Nl5BMl5BanBnXkFtZTcwMjgwMjA0Mg@@._V1_UY44_CR3,0,32,44_AL_.jpg" alt="avatar" />
              <img src="https://m.media-amazon.com/images/M/MV5BOTkyNDE4NTA4NF5BMl5BanBnXkFtZTgwOTY3ODQ1MDI@._V1_UY44_CR3,0,32,44_AL_.jpg" alt="avatar" />
              <img src="https://m.media-amazon.com/images/M/MV5BNzYwMTQ1ODY1MV5BMl5BanBnXkFtZTgwMTU5NDc5OTE@._V1_UY44_CR17,0,32,44_AL_.jpg" alt="avatar" />
              <img src="https://m.media-amazon.com/images/M/MV5BMTEyMDA1MzE0NjdeQTJeQWpwZ15BbWU3MDM0NzA4MDQ@._V1_UY44_CR1,0,32,44_AL_.jpg" alt="avatar" />
            </div>
            <div class="casts">
              <p v-for="actor in movie.actors" :key="actor.name">{{actor.name}}</p>
            </div>
          </div>
          <div class="synopsis-section">
            <h3>SYNOPSIS</h3>
            <p class="fw-bold">{{movie.overview}}</p>
          </div>
          <div class="gallery-section">
            <h3>VIDEO / PICTURE</h3>
            <div class="gallery">
              <div class="small"><img src="https://m.media-amazon.com/images/M/MV5BYzkyNGViZDItYzFkMy00OGM0LTg3NzktZGVkZjM2Mzk1OGEzXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg" alt="media" /></div>
              <div class="medium"><img src="https://m.media-amazon.com/images/M/MV5BNTkxOGIwYzUtNzc0ZS00MTBkLWFkODItYzEzNGRkN2E3MTAxXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg" alt="media" /></div>
              <div class="small"><img src="https://m.media-amazon.com/images/M/MV5BMzg2OTY3MjE3OF5BMl5BanBnXkFtZTgwNTkxMDU0MDI@._V1_SX1777_CR0,0,1777,745_AL_.jpg" alt="media" /></div>
            </div>
          </div>
        </div>
      </div>
      <!-- end movie-card -->

      <div v-if="isLoggedIn">
        <div>
        Likeit:
          <button
            @click="likeMovie(moviePk)"
          >{{ likeCount }}</button>
        </div>
        <br>
      </div>

      <movie-comment :comments="movie.comments"></movie-comment>
    </ul>
  
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
// import MovieVideo from '@/components/movies/MovieVideo.vue'
import MovieComment from '@/components/movies/MovieComment.vue'

export default {
  name: 'MovieDetail',
  components: {
    // MovieVideo, 
    MovieComment
  },
  data() {
    return {
      moviePk: this.$route.params.moviePk
    }
  },
  computed: {
    ...mapGetters(['movie', 'isLoggedIn']),
    poster () {
      return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`
    },
    actorPoster () {
      return `https://www.themoviedb.org/t/p/original${this.actor.profile_path}`
    },
    likeCount() {
      return this.movie.like_users?.length
    }
  },
  methods: {
    ...mapActions(['likeMovie']),
  },
  // created() {
  //   this.fetchMovie(this.moviePk)
  // }
}
</script>

<style scoped>
p {
  font-size: 14px;
  line-height: 20px;
}

img {
  width: 100%;
}

h2 {
  font-size: 30px;
}

h3 {
  font-size: 14px;
  margin-bottom: 15px;
}

/*movie-card*/
.movie-card {
  display: grid;
  grid-template-columns: 2fr 400px 0.5fr 400px 2fr;
  grid-template-areas: ". p . m .";
}
@media screen and (max-width: 1024px) {
  .movie-card {
    grid-template-columns: 1fr 4fr 1fr 4fr 1fr;
  }
}
@media screen and (max-width: 780px) {
  .movie-card {
    grid-template-columns: 1fr 4fr 1fr;
    grid-template-areas: ". p ." ". m .";
  }
}
@media screen and (max-width: 500px) {
  .movie-card {
    grid-template-columns: 0.5fr 4fr 0.5fr;
    grid-template-areas: ". p ." ". m .";
  }
}
.movie-card .poster-wrapper {
  grid-area: p;
}
.movie-card .poster-wrapper .poster {
  position: relative;
  color: #fff;
}
@media screen and (max-width: 500px) {
  .movie-card .poster-wrapper .poster {
    margin-bottom: 30px;
  }
}
.movie-card .poster-wrapper .poster .release-date {
  position: absolute;
  top: 30px;
  left: -30px;
  background-color: #3686ff;
  padding: 10px;
  text-align: center;
}
.movie-card .poster-wrapper .poster .release-date h2 {
  font-size: 42px;
  color: #fff;
}
.movie-card .poster-wrapper .poster .release-date .divider {
  background-color: #fff;
  height: 2px;
  width: 20px;
  margin: 10px auto;
}
.movie-card .poster-wrapper .poster .btn-play {
  position: absolute;
  bottom: 30px;
  right: -30px;
  background-color: #3686ff;
  padding: 15px;
  font-size: 24px;
  cursor: pointer;
  transition: all 0.4s;
}
.movie-card .poster-wrapper .poster .btn-play:hover {
  background-color: #fdba2e;
}
.movie-card .movie-info {
  grid-area: m;
}
.movie-card .movie-info > div {
  margin-bottom: 30px;
}
.movie-card .movie-info .header-section p {
  margin: 5px 0;
}
.movie-card .movie-info .header-section .extra {
  display: flex;
  align-items: center;
}
@media screen and (max-width: 500px) {
  .movie-card .movie-info .header-section .extra {
    display: block;
  }
}
.movie-card .movie-info .header-section .extra .ratings {
  margin-right: 50px;
  color: #fdba2e;
}
.movie-card .movie-info .header-section .extra .ratings p {
  font-size: 18px;
}
.movie-card .movie-info .header-section .extra .channels > span {
  margin-right: 5px;
}
.movie-card .movie-info .cast-section .casts {
  display: flex;
}
.movie-card .movie-info .cast-section .casts img {
  width: 40px;
  height: 40px;
  object-fit: cover;
  border-radius: 50%;
  margin-right: 15px;
}
.movie-card .movie-info .gallery-section .gallery {
  display: grid;
  grid-template-columns: repeat(autofit, minmax(50px, 1fr));
  grid-auto-rows: 75px;
  grid-row-gap: 10px;
  grid-column-gap: 10px;
  grid-auto-flow: dense;
}
.movie-card .movie-info .gallery-section .gallery .small {
  grid-column: span 1;
}
.movie-card .movie-info .gallery-section .gallery .medium {
  grid-column: span 3;
}
.movie-card .movie-info .gallery-section .gallery img {
  object-fit: cover;
  width: 100%;
  height: 100%;
}
</style>