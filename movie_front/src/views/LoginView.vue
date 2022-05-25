<template>
<!-- css 꾸미기 -->
  <div>
    <account-error-list v-if="authError"></account-error-list>

    <div class="section body container">
      <form @submit.prevent="login(credentials)" class="section text-center">
        <h4 class="mb-4 pb-3">Log In</h4>
        <div class="form-group">
          <input v-model="credentials.username" type="text" class="form-style" placeholder="Your ID" id="username" autocomplete="off" required />
          <i class="input-icon uil uil-at"></i>
        </div>
        <div class="form-group mt-2">
          <input v-model="credentials.password" type="password" class="form-style" placeholder="Your Password" id="password" autocomplete="off" required />
          <i class="input-icon uil uil-lock-alt"></i>
        </div>
        <button href="#" class="btn mt-4">LOGIN</button>
        <p class="mb-0 mt-4 text-center"><router-link to="/signup" class="link">회원가입</router-link></p>
      </form>
    </div>

    <!-- <form @submit.prevent="login(credentials)">
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
      </div> -->
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
.body {
  font-family: "Poppins", sans-serif;
}
.link {
  color: #c4c3ca;
  text-decoration: None;
}
.link:hover {
  color: #ffeba7;
}
/* p {
  font-weight: 500;
  font-size: 14px;
  line-height: 1.7;
}
h4 {
  font-weight: 600;
} */
.section {
  position: relative;
  width: 100%;
  display: block;
}
.form-group {
  position: relative;
  display: block;
  margin: 0;
  padding: 0;
}
.form-style {
  padding: 13px 20px;
  padding-left: 55px;
  height: 48px;
  width: 100%;
  font-weight: 500;
  border-radius: 4px;
  font-size: 14px;
  line-height: 22px;
  letter-spacing: 0.5px;
  outline: none;
  color: #c4c3ca;
  background-color: #1f2029;
  border: none;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21, 21, 21, 0.2);
}
.form-style:focus,
.form-style:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21, 21, 21, 0.2);
}
.input-icon {
  position: absolute;
  top: 0;
  left: 18px;
  height: 48px;
  font-size: 24px;
  line-height: 48px;
  text-align: left;
  color: #ffeba7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.form-group input:-ms-input-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input::-moz-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:-moz-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input::-webkit-input-placeholder {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:focus:-ms-input-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:focus::-moz-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:focus:-moz-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}
.form-group input:focus::-webkit-input-placeholder {
  opacity: 0;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
}

.btn {
  border-radius: 4px;
  height: 44px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border: none;
  background-color: #ffeba7;
  color: #102770;
  box-shadow: 0 8px 24px 0 rgba(255, 235, 167, 0.2);
}
.btn:active,
.btn:focus {
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16, 39, 112, 0.2);
}
.btn:hover {
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16, 39, 112, 0.2);
}
</style>


