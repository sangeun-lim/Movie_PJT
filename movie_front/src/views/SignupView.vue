<template>

  <div>
    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div class="container-fluid px-1 px-md-5 px-lg-1 px-xl-5 py-5 mx-auto bg-black">
        <div class="card card0 border-0 bg-black">
          <div class="row d-flex justify-content-center">
              <div class="mt-4 col-xl-4">
                  <div class="card1 card border-0 px-4 py-5">
                    <h1>회원가입</h1>
                    <br>
                    <div class="row px-3">
                        <label class="mb-1">
                          <h6 class="mb-0 text-sm">아이디</h6>
                        </label>
                        <input v-model="credentials.username" type="text" id="username" required />
                    </div>
                    <div class="row px-3">
                        <label class="mb-1">
                          <h6 class="mb-0 text-sm">비밀번호</h6>
                        </label>
                        <input v-model="credentials.password1" type="password" id="password1" required />

                    </div>
                    <div class="row px-3">
                       <label class="mb-1">
                          <h6 class="mb-0 text-sm">비밀번호 확인</h6>
                        </label>
                        <input v-model="credentials.password2" type="password" id="password2" required />

                    </div>
                  </div>
                  <button>가입하기</button>
              </div>
            </div>
          </div>
        </div>
    </form>
          <div class="bg-blue py-4">
            <div class="row px-3"> <small class="ml-4 ml-sm-5 mb-2">Copyright &copy; 2022. All rights reserved.</small>
            </div>
          </div>
  </div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'SingupView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials : {
        username: '',
        password1: '',
        password2: '',
      }
    }
  },
  methods: {
    ...mapActions(['signup'])
  },
  computed: {
    ...mapGetters(['authError'])
  },
}
</script>

<style>

</style>