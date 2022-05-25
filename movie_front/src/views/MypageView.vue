<template>
  <div>
    <div class="wrapper">
      <div class="neon-wrapper">
        <span class="txt">MY AREA</span>
        <span class="gradient"></span>
        <span class="dodge"></span>
      </div>
    </div>
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
.navbar{
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top:20px;
  color: #ffffff;
  background:#000000;
  font-size:20px;
  font-weight: bold;
  font-family: Arial;
  text-transform: uppercase;
  
}
.wrapper {
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #000000; 
}
.txt {
    color: #ffffff;
    background:#000000;
    font-size:100px;
    font-weight: bold;
    font-family: Arial;
    text-transform: uppercase;
}

.txt::before {
    content: 'MY AREA';
    position: absolute;
    mix-blend-mode: difference;
    filter: blur(3px);
}
.neon-wrapper {
    display:inline-flex;
    filter: brightness(200%);
    overflow: hidden;
}
.gradient{
  /*   
  use gradpad to generate code :
  http://ourownthing.co.uk/gradpad.html#
  */
    background: linear-gradient(90deg, rgba(243, 72, 104,1) 20.5625%,rgba(242, 71, 104,1) 20.5625%,rgba(158, 0, 236,1) 80.5625%);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    mix-blend-mode: multiply;
}
.dodge {
    background: radial-gradient(circle,white,black 35%) center / 25% 25%;
    position: absolute;
    top:-100%;
    left:-100%;
    right:0;
    bottom:0;
    mix-blend-mode: color-dodge;
    animation: dodge-area 5s linear infinite;
}
@keyframes dodge-area {
    to {
        transform: translate(50%,50%);
    }
}
</style>