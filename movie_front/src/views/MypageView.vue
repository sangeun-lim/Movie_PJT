<template>
  <div>
    <h1 class="neon" data-text="U">{{ this.$route.params.username }}'s<span class="flicker-slow"> A</span>R<span class="flicker-fast">E</span>A</h1>
    <br>
    <hr>

    <h3>좋아요 누른 영화</h3>
    <like-movies :likeMovies="mypage.like_movies"></like-movies>
    <hr>
    <!-- <h3>선호하는 장르 : </h3> -->
    <h3>{{ this.$route.params.username }}님이 좋아할 만한 영화</h3>
    <like-genre :likeGenreDic="likeGenreDic"></like-genre>
    <hr>
    
    <h3>내가 쓴 글</h3>
    <my-review :reviews="mypage.reviews"></my-review>
    <hr>
  </div>
</template>

<script>
  import LikeMovies from '@/components/accounts/LikeMovies.vue'
  import MyReview from '@/components/accounts/MyReview.vue'
  import LikeGenre from '@/components/accounts/LikeGenre.vue'

  import { mapGetters, mapActions } from 'vuex'
  // import axios from 'axios'


  export default {
    name : 'MypageView',
    components: {
      LikeMovies, MyReview, LikeGenre
    },
    data () {
      return {
        likeGenreDic: {},
      }
    },
    computed: {
      ...mapGetters(['mypage'])
    },
    methods: {
      ...mapActions(['fetchMypage']),
      likeGenre () {
        for (const movie of this.mypage.like_movies) {
          for (const genre of movie.genres) {
            if (this.likeGenreDic[genre]){
              // console.log(genre.genre_name)
              this.likeGenreDic[genre] ++
            } else {
              this.likeGenreDic[genre] = 1
            }
          }
        }
        // console.log(this.likeGenreDic)
        // const searchURL = 'http://localhost:8000/api/v1/movies/like_recommend/'
        // axios.post(searchURL, this.likeGenreDic)
        //   .then(res => {
        //     console.log(res.data)
        //     this.likeGenreMovies = res.data
        //   })
      }
    },
    created() {
      const payload = { username: this.$route.params.username}
      this.fetchMypage(payload)
      console.log('created!')
      this.likeGenre()
    },
  }
</script>

<style>
.neon {
  font-family: "Monoton", cursive;
  font-size: 50px;
  color: #ffd5ff;
  position: relative;
  top: 0%;
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