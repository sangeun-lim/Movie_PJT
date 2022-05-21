<template>
  <div>
    <h1>로그아웃</h1>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'LogoutView',
    methods: {
      ...mapActions(['logout'])
    },
    computed: {
      ...mapGetters(['isLoggedIn'])
    },
    created() {
      if (this.isLoggedIn){
        this.logout()
      } else {
        alert('접근 불가')
        this.$router.back() // 이전페이지로 보내는 명령어 
      }
    },
  }
</script>

<style>

</style>