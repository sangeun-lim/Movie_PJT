<template>
  <div>
  <li>
    <span v-if="!isEditing">댓글 : {{ payload.content }} | 평점 :{{payload.score}}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <input type="number" v-model="payload.score" min="1" max="5">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteMovieComment(payload)">Delete</button>
    </span>
  </li>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieCommentItem.vue',
  props: { 
    comment: Object 
  },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.comment.movie,
        commentPk: this.comment.id,
        content: this.comment.content,
        score: this.comment.score
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateMovieComment', 'deleteMovieComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateMovieComment(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style>
</style>