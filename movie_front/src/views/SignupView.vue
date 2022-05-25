<template>

  <div>
    <account-error-list v-if="authError"></account-error-list>
    
    <div class="section body container">
      <form @submit.prevent="signup(credentials)" class="section text-center">
        <h1 class="mb-4 pb-3">Sign Up</h1>
        <div class="form-group">
          <input v-model="credentials.username" type="text" id="username" class="form-style" placeholder="ID" autocomplete="off" required />
          <i class="input-icon uil uil-user"></i>
        </div>
        <div class="form-group mt-2">
          <input v-model="credentials.password1" type="password" id="password1" class="form-style" placeholder="Password" autocomplete="off" required />
          <i class="input-icon uil uil-at"></i>
        </div>
        <div class="form-group mt-2">
          <input v-model="credentials.password2" type="password" id="password2" class="form-style" placeholder="Password Check Up" autocomplete="off"  required />
          <i class="input-icon uil uil-lock-alt"></i>
        </div>
        <button href="#" class="custom-btn btn-14 mt-5">submit</button>
      </form>
    </div>

    <!-- <form @submit.prevent="signup(credentials)">
      <div class="container-fluid px-1 px-md-5 px-lg-1 px-xl-5 py-5 mx-auto bg-black text-black">
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
    </form> -->
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

<style scoped>
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

h1 {
  margin: auto;
  font-size: 4rem;
  font-weight: 300;
  animation: lights 5s 750ms linear infinite;
}

/* form */
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

  /* button */
.frame {
  width: 90%;
  margin: 40px auto;
  text-align: center;
}

.custom-btn {
  color: #fff;
  width: 130px;
  height: 40px;
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
}

.btn-14 {
  position: relative;
  color: #FE1DAD;
  border: none;
  z-index: 2;
}
.btn-14:before,
.btn-14:after {
  position: absolute;
  content: "";
  width: 20%;
  height: 20%;
  border: 1px solid;
  
  z-index: -1;
  transition: all 0.3s ease;
}
.btn-14:before{
   top: 0;
   left: 0;
   border-bottom-color: transparent;
   border-right-color: transparent;
   border-top-color: #FE1DAD;
   border-left-color: #FE1DAD;
}
.btn-14:after{
   bottom: 0;
   right: 0;
   border-top-color: transparent;
   border-left-color: transparent;
   border-bottom-color: #FE1DAD;
   border-right-color: #FE1DAD;
}
.btn-14:hover:before,
.btn-14:hover:after {
  border-color: #FE1DAD;
  height: 100%;
  width: 100%;
  box-shadow: 0 0 5px #FE1DAD, 0 0 5px #FE1DAD inset;
}
</style>