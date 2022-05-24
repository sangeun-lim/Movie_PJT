<template>
  <div class="container">
    <div class="row">
      <div class="col">
      <iframe :src="videoURL" frameborder="0"></iframe>
      </div>
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
      videoURL() {
        const {videoId} = this.video.id
        return `https://www.youtube.com/embed/${videoId}`
    },
  },

}
</script>

<style>

</style>