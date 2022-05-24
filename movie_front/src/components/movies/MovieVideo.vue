<template>
  <div>
    <movie-video-item
    v-for="(video, idx) in youtubeVideos"
    :key="idx"
    :video="video"
    ></movie-video-item>
  </div>
</template>

<script>
import MovieVideoItem from '@/components/movies/MovieVideoItem.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieVideo',
  components: {
    MovieVideoItem,
  },
  props:{
    title : String,
  },
  computed: {
    ...mapGetters(['youtubeVideos'])
  },
  // created() {
  //   console.log(this.title)
  //   this.$store.dispatch('searchYoutube', this.title)
  // },
  mounted(){
    console.log(this.title)
    this.$store.dispatch('searchYoutube', this.title)
  }
}
</script>

<style>

</style>