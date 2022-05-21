<template>
  <div>
    <!-- 여기는 다른 사용자의 프로필을 보는 것이 아닌 개인의 마이페이지를 보는프로필임 -->
    <h1>MY PAGE</h1>
    <h1>{{ mypage.username }}</h1>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name : 'MypageView',
  computed: {
    ...mapGetters(['mypage'])
  },
  methods: {
    ...mapActions(['fetchMypage'])
  },
  created() {
    const payload = { username: this.$route.params.username}
    this.fetchMypage(payload)
  }
}
</script>

<style>

</style>