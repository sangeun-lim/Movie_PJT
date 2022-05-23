<template>
  <div>

    <ul>
      <movie-comment-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </movie-comment-item>
    </ul>

    <movie-comment-form></movie-comment-form>

  </div>
</template>

<script>
  import MovieCommentForm from '@/components/movies/MovieCommentForm.vue'
  import MovieCommentItem from '@/components/movies/MovieCommentItem.vue'

  export default {
    name: 'MovieComment',
    components: {
      MovieCommentItem, MovieCommentForm
    },
    props: { 
      comments: Array
    },
  }
</script>

<style>

</style>