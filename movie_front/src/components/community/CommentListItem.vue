<template>
  <li class="comment-list-item">
    <!-- 이부분은 필요없을지도..? -->
    <!-- <router-link :to="{ name: 'mypage', params: { username: comment.user.username } }">
      {{ comment.user.username }}
    </router-link>:  -->
    
    <!-- <p>{{ comment.content }}</p> -->

    <span v-if="!isEditing">{{ payload.content }}</span>
    <!-- "review.review_comments.0.content" -->
    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteComment(payload)">Delete</button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { 
    comment: Object 
  },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.comment-list-item {
  border: 1px solid green;

}
</style>