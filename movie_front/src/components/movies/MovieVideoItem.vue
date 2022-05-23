<template>
  <div>
    <img :src="video.snippet.thumbnails.default.url" alt="thumbnail" @click="videoURL">
    <div class="youtube-container">
      <iframe :src="videoURL" frameborder="0"></iframe>
    </div>
  </div>
</template>

<script>

export default {
  name:'MovieVideoItem',
  props:{
    video: Object,
  },
  computed: {
      videoURL: function () {
        const { videoId } = this.video.id
        return `https://www.youtube.com/embed/${videoId}`
    },
  }

}
</script>

<style>

</style>