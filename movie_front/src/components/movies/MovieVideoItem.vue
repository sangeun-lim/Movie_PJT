<template>
  <div class="container">
    <iframe :src="videoURL" frameborder="0"></iframe>
  </div>
</template>

<script>

export default {
  name:'MovieVideoItem',
  props:{
    video: Object,
  },
  computed: {
      videoURL() {
        const {videoId} = this.video.id
        return `https://www.youtube.com/embed/${videoId}`
    },
  },

}
</script>

<style scoped>
iframe {
  width: 100%;
  height: 300px;
}
</style>