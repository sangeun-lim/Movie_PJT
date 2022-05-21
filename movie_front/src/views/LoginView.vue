<template>
<!-- css 꾸미기 -->
  <div>
    <h1>로그인 페이지</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">아이디: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>

      <div>
        <label for="password">비밀번호: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>

      <button>로그인</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    ...mapActions(['login'])
  },
  computed: {
    ...mapGetters(['authError'])
  },
}
</script>

<style>

</style>