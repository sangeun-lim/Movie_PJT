<template>
  <div>
    <!-- 여기는 다른 사용자의 프로필을 보는 것이 아닌 개인의 마이페이지를 보는프로필임 -->
    <h1>MY PAGE</h1>
    <!-- 회원정보수정을 기본값으로 주고 다른 페이지는 라우터로 -->
    <h1>{{ this.$route.params.username }}</h1>
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
      // console.log('created!')
      this.likeGenre()
    },
  }
</script>

<style>

</style>