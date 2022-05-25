<template>
  <table class="d-flex form">
    <div class="comment-list-item">
      <div class="d-flex justify-content-between">
        <h5 v-if="!isEditing" class="text-start fw-bold mt-3">{{ payload.content }}</h5>

        <span v-if="isEditing">
          <div class="input d-flex m-0">
            <div class="m-0">              
              <input class="bg-dark" style="width:750px" type="text" v-model="payload.content">
              <input class="bg-dark" style="width:750px" type="number" v-model="payload.score" min="1" max="5">
            </div>
            <button class="comment-btn btn-2" @click="onUpdate">update</button>
            <button class="comment-btn btn-2" @click="switchIsEditing">cancel</button> 
          </div>
        </span>

        <span v-if="currentUser.username === comment.user.username && !isEditing" class="mx-3">
          <div>
            <button class="comment-btn btn-2" @click="switchIsEditing">update</button>
            <button class="comment-btn btn-2" @click="deleteMovieComment(payload)">delete</button> 
          </div>
        </span>
      </div>
      <p v-if="!isEditing" class="text-start fw-bold text-white">평점 : {{payload.score}}</p>

      <p class="text-start m-0">{{ comment.user.username }}</p>
      <p class="fw-light text-secondary text-start">
        created time : {{ this.comment.created_at | moment("YYYY-MMMM-Do a h:mm")  }} || updated time : {{ this.comment.updated_at | moment("YYYY-MMMM-Do a h:mm")  }}
      </p>
    </div>
  </table>
  <!-- <div>
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
  </div> -->
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
.form {
  display: flex;
  padding: 20px;
  flex-direction: column;
  width: 1000px;
  gap: 46px;
  margin: 10px auto;
}
</style>