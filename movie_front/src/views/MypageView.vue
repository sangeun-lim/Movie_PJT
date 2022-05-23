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
    <h3>선호하는 장르 : </h3>
    <hr>
    <h3>내가 쓴 글</h3>
    <my-review :reviews="mypage.reviews"></my-review>
    <hr>
  </div>
</template>

<script>
import LikeMovies from '@/components/accounts/LikeMovies.vue'
import MyReview from '@/components/accounts/MyReview.vue'

import { mapGetters, mapActions } from 'vuex'

export default {
  name : 'MypageView',
  components: {
    LikeMovies, MyReview
  },
  data () {
    return {
      likeGenreDic: {}
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
          console.log(genre.genre_name)
          this.likeGenreDicgenre[genre.genre_name] = 1
        }
      }
    }
  },
  created() {
    const payload = { username: this.$route.params.username}
    this.fetchMypage(payload)
    this.likeGenre()
  }
}
</script>

<style>

</style>