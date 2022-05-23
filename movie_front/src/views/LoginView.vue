<template>
<!-- css 꾸미기 -->
  <div>
    <h1>로그인 페이지</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="login(credentials)">
      <div class="container-fluid px-1 px-md-5 px-lg-1 px-xl-5 py-5 mx-auto bg-black">
        <div class="card card0 border-0 bg-black">
          <div class="row d-flex justify-content-center">
            <div class="mt-5 col-4">
              <div class="card2 card border-0 px-4 py-5">
                <div class="row px-3">
                  <label class="mb-1">
                    <h6 class="mb-0 text-sm">아이디</h6>
                  </label>
                  <input v-model="credentials.username" placeholder="아이디를 입력하세요" type="text" id="username" required />
                </div>

                <div class="row px-3">
                  <label class="mb-1">
                    <h6 class="mb-0 text-sm">비밀번호</h6>
                   </label> 
                  <input v-model="credentials.password" placeholder="비밀번호를 입력하세요" type="password" id="password" required />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <button>로그인</button>
    </form>
      <div class="row mb-4 px-3">
        <small class="font-weight-bold">아이디가 없으신가요? 
          <router-link class="text-danger text-decoration-none" to="/signup">회원가입</router-link>
        </small>
      </div>
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


