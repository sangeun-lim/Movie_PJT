<template>
  <div>
    <!-- <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div>
        <div class="navbar-nav">
          <router-link :to="{name : 'movieAll'}" class=" text-decoration-none" >전체영화  |<span class="sr-only">(current)</span></router-link>
          <router-link :to="{name : 'moviePopular'}" class=" text-decoration-none" >인기영화  |</router-link>
          <router-link :to="{name : 'movieGenre'}" class=" text-decoration-none" >장르별 영화</router-link>
        </div>
      </div>
    </nav> -->
    

    <div class="d-flex justify-content-evenly">
      <div class="small-font">
        <router-link :to="{name : 'movieAll'}" class="text-decoration-none" >| 전체영화 |<span class="sr-only">(current)</span></router-link>
      </div>
      <div class="small-font">
        <router-link :to="{name : 'moviePopular'}" class="text-decoration-none" >| 인기영화 |</router-link>
      </div>
      <div class="small-font">
        <router-link :to="{name : 'movieGenre'}" class="text-decoration-none" >| 장르별 영화 |</router-link>
      </div>
    </div>
  </div>


</template>

<script>
export default {
  name: 'MovieNavBar'
}
</script>

<style>
.small-font, .small-font a {
    font-size: 1em;
    color: white;
    text-decoration: none;
    text-shadow: 0 1px 5px rgba(0,0,0,0.1);
    transition: color 0.1s ease-out;
    text-align: center;
    font-size: 110%;
    font-weight: 600;
}

.small-font a:hover {
    color: rgba(255,255,255,0.5);
}
</style>