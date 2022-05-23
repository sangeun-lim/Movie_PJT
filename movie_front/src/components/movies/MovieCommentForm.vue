<template>
  <form @submit.prevent="onSubmit">
    <label for="comment">comment: </label>
    <input type="text" id="comment" v-model="content" required>
    <button>작성</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieCommentForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createMovieComment']),
    onSubmit() {
      this.createMovieComment({ moviePk: this.movie.movie_id, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>

</style>