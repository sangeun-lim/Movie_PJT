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

    <h1 class="mypage-title">My Favorite Movie</h1>
    <like-movies :likeMovies="mypage.like_movies"></like-movies>
    <hr>
    
    <!-- <h3>선호하는 장르 : </h3> -->
    <h1 class="mypage-title">Recommended Movie For {{ this.$route.params.username }}</h1>
    <like-genre :likeGenreDic="likeGenreDic"></like-genre>
    <hr>
    
    <h1 class="mypage-title">My Review</h1>
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

/* title */
@keyframes lights {
  0% {
    color: hsl(230, 40%, 80%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.2),
      0 0 0.125em hsla(320, 100%, 60%, 0.3),
      -1em -0.125em 0.5em hsla(40, 100%, 60%, 0),
      1em 0.125em 0.5em hsla(200, 100%, 60%, 0);
  }
  
  30% { 
    color: hsl(230, 80%, 90%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.5),
      0 0 0.125em hsla(320, 100%, 60%, 0.5),
      -0.5em -0.125em 0.25em hsla(40, 100%, 60%, 0.2),
      0.5em 0.125em 0.25em hsla(200, 100%, 60%, 0.4);
  }
  
  40% { 
    color: hsl(230, 100%, 95%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.5),
      0 0 0.125em hsla(320, 100%, 90%, 0.5),
      -0.25em -0.125em 0.125em hsla(40, 100%, 60%, 0.2),
      0.25em 0.125em 0.125em hsla(200, 100%, 60%, 0.4);
  }
  
  70% {
    color: hsl(230, 80%, 90%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.5),
      0 0 0.125em hsla(320, 100%, 60%, 0.5),
      0.5em -0.125em 0.25em hsla(40, 100%, 60%, 0.2),
      -0.5em 0.125em 0.25em hsla(200, 100%, 60%, 0.4);
  }
  
  100% {
    color: hsl(230, 40%, 80%);
    text-shadow:
      0 0 1em hsla(320, 100%, 50%, 0.2),
      0 0 0.125em hsla(320, 100%, 60%, 0.3),
      1em -0.125em 0.5em hsla(40, 100%, 60%, 0),
      -1em 0.125em 0.5em hsla(200, 100%, 60%, 0);
  }
  
}

.mypage-title {
  /* position: absolute; */
  top: 50%;
  left: 50%;
  /* transform: translateX(-50%) translateY(-50%); */
  font: 50px arial;
  text-align: center;
  text-shadow: 
    0px 0px 3px #fff, 
    0px 0px 7px #fff, 
    0px 0px 10px #fff, 
    0px 0px 16px #e542f4, 
    0px 0px 25px #e542f4, 
    0px 0px 40px #e542f4;
  animation: blink 1s ease-in-out infinite;
}

@keyframes blink {
  0% { text-shadow: 
    0px 0px 3px #fff, 
    0px 0px 7px #fff, 
    0px 0px 10px #fff, 
    0px 0px 16px #e542f4, 
    0px 0px 25px #e542f4, 
    0px 0px 40px #e542f4; }
  50% {
    text-shadow: 
    0px 0px 1px #fff, 
    0px 0px 3px #fff, 
    0px 0px 5px #fff, 
    0px 0px 10px #e542f4, 
    0px 0px 20px #e542f4, 
    0px 0px 30px #e542f4;
  }
  100% {
    text-shadow: 
    0px 0px 3px #fff, 
    0px 0px 7px #fff, 
    0px 0px 10px #fff, 
    0px 0px 16px #e542f4, 
    0px 0px 25px #e542f4, 
    0px 0px 40px #e542f4;
  }
}
</style>