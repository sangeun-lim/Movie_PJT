<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div>
      <div class="navbar-nav">
        <router-link :to="{name : 'movieAll'}" class=" text-decoration-none" >전체영화 |<span class="sr-only">(current)</span></router-link>
        
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'MovieNavBar'
}
</script>

<style>

</style>