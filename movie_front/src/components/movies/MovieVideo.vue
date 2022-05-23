<template>
  <di>
    <movie-video-item
    v-for="(video, idx) in youtubeVideos"
    :key="idx"
    :video="video"
    ></movie-video-item>
  </di>
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
  created() {
    this.$store.dispatch('searchYoutube', this.title)
  }
}
</script>

<style>

</style>