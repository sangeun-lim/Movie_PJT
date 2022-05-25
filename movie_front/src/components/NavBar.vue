<template>
  <div>
    <!-- <nav class="navbar navbar-expand-lg navbar-light bg-dark">
      <div class="container-fluid">
        <router-link :to="{name : 'home'}" class="text-decoration-none" >Home |</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link :to="{name : 'movies'}" class=" text-decoration-none">| Movie |</router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{name : 'community'}" class=" text-decoration-none">| Community</router-link>
            </li>
          </ul>
          <span class="navbar-text" v-if="!isLoggedIn">
            <router-link :to="{name : 'login'}" class=" text-decoration-none" >Login</router-link> | 
            <router-link :to="{name : 'signup'}" class=" text-decoration-none" >Signup</router-link>
          </span>
          <span v-if="isLoggedIn">
            <router-link :to="{name : 'logout'}" class=" text-decoration-none" >logout |</router-link>
            <router-link :to="{ name : 'mypage', params: { username } }" class=" text-decoration-none"
            >| mypage</router-link>
          </span>
        </div>
      </div>
    </nav> -->
    <p class="m-3 text-start">{{ getToday() }}요일 </p>
    
    <nav class="nav sticky-top mb-5 row">
      <div class="menu-item d-flex justify-content-around">
        <div class="menu-text">
          <router-link :to="{name : 'home'}" class="text-decoration-none" >Home</router-link>
        </div>

        <div class="menu-text">
          <router-link :to="{name : 'movies'}" class=" text-decoration-none">Movie</router-link>
        </div>

        <div class="menu-text">
          <router-link :to="{name : 'community'}" class=" text-decoration-none">Community</router-link>
        </div>
          <span class="small-font align-self-end" v-if="!isLoggedIn">
            <router-link :to="{name : 'login'}" class=" text-decoration-none" >Login</router-link> | 
            <router-link :to="{name : 'signup'}" class=" text-decoration-none" >Signup</router-link>
          </span>
          <span class="small-font align-self-end" v-if="isLoggedIn">
            <router-link :to="{name : 'logout'}" class=" text-decoration-none" >logout</router-link> |
            <router-link :to="{ name : 'mypage', params: { username } }" class=" text-decoration-none">mypage</router-link>
          </span>
      </div>
        <div class="d-flex justify-content-end me-5 pe-5">
      </div>
    </nav>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods: {
      getToday () {
        const today = new Date()
        const year = today.getFullYear()
        const month = ('0' + (today.getMonth() + 1)).slice(-2)
        const day = ('0' + today.getDate()).slice(-2)

        const week = ['일', '월', '화', '수', '목', '금', '토']

        const date = year + '년 ' + month + '월 ' + day + '일 ' + week[today.getDay()]
        return date
      }
    },
  }
</script>

<style>
nav {
    width: var(--menu-width);
    display: flex;
    transform-style: preserve-3d;
    justify-content: space-evenly;
    position: relative;
    z-index: 2;
    margin: 0px auto;
    perspective: 2000px;
    flex-wrap: wrap;
    top: 3em;
}

nav .menu-item {
    color: white;
    font-weight: 600;
    transform-style: preserve-3d;
    flex-grow: 1;
    display: flex;
    flex-basis: var(--item-width);
    box-sizing: border-box;
    justify-content: center;
    perspective: 200px;
    letter-spacing: 0.5px;
    min-height: 2em;
}

nav .menu-text, nav .menu-text a {
    font-size: 1em;
    color: white;
    text-decoration: none;
    text-shadow: 0 1px 5px rgba(0,0,0,0.1);
    transition: color 0.1s ease-out;
    text-align: center;
    font-size: 140%;
}

nav .menu-text a:hover {
    color: rgba(255,255,255,0.5);
}

#sub-menu-bottom {
    background: #d4e3ea70;
    position: absolute;
    bottom: 0;
    opacity: 0;
    transition: all 0.25s ease-out, height 0.1s ease-out;
    left: 0;
    width: 100%;
    height: 5em;
}
</style>