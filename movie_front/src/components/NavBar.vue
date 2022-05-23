<template>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #e3f2fd;">
      <div class="container-fluid">
        <router-link :to="{name : 'home'}" class="text-decoration-none" >Home |</router-link>
        <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button> -->
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
            <router-link :to="{name : 'mypage'}" class=" text-decoration-none"
            >| mypage</router-link>
          </span>
        </div>
      </div>
    </nav>
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
  }
</script>

<style>

</style>