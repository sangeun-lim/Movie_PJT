<template>
  <table class="form">
    <div class="comment-list-item">
      <div class="d-flex justify-content-between">
        <h5 v-if="!isEditing" class="text-start fw-bold mt-3">{{ payload.content }}</h5>

        <span v-if="isEditing">
          <div class="input d-flex">
            <input class="bg-dark" style="width:760px" type="text" v-model="payload.content">
            <button class="comment-btn btn-2" @click="onUpdate">update</button>
            <button class="comment-btn btn-2" @click="switchIsEditing">cancel</button> 
          </div>
          <!-- <button class="w-btn w-btn-pink" type="button" @click="onUpdate">수정</button> |
          <button class="w-btn w-btn-gra1 w-btn-gra-anim" type="button" @click="switchIsEditing">취소</button> -->
        </span>

        <span v-if="currentUser.username === comment.user.username && !isEditing" class="mx-3">
          <div>
            <button class="comment-btn btn-2" @click="switchIsEditing">update</button>
            <button class="comment-btn btn-2" @click="deleteComment(payload)">delete</button> 
          </div>
          <!-- <button class="w-btn w-btn-gra1" type="button" @click="switchIsEditing">수정</button> |
          <button class="w-btn w-btn-gra1 w-btn-gra-anim" type="button" @click="deleteComment(payload)">삭제</button> -->
        </span>
      </div>

      <div class="text-start">{{ comment.user.username }}</div>
      <p class="fw-light text-secondary text-start">
         작성 : {{ this.comment.created_at | moment("YYYY-MMMM-Do a h:mm")  }} || 수정 : {{ this.comment.updated_at | moment("YYYY-MMMM-Do a h:mm")  }}
      </p>
    </div>
  </table>
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
.form {
  display: flex;
  flex-direction: column;
  width: 1000px;
  margin: 10px auto;
}

p {
  margin: 0px;
  font-size: 15px;
  color: gray;
}

.input input, .input textarea {
  width: 100%;
  background: transparent;
  outline: none;
  border: none;
  padding: 10px 6px;
  color: white;
}
.input input::placeholder, .input textarea::placeholder {
  color: transparent;
}

.w-btn {
    position: relative;
    border: none;
    display: inline-block;
    padding: 15px 30px;
    border-radius: 15px;
    font-family: "paybooc-Light", sans-serif;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    text-decoration: none;
    font-weight: 600;
    transition: 0.25s;
}
.w-btn-pink {
    background-color: #f199bc;
    color: #d4dfe6;
}
.w-btn-gra1 {
    background: linear-gradient(-45deg, #33ccff 0%, #ff99cc 100%);
    color: white;
}

.w-btn-gra-anim {
    background-size: 400% 400%;
    animation: gradient1 5s ease infinite;
}

 /* button */
 .container1:not(:last-child){
  margin-bottom:2rem;
}
.comment-btn{
  padding:0rem 1rem;
  margin:0.5rem;
  border-radius:5px;
  border:2px solid #bc4873;
  background:transparent;
  color:#bc4873;
  font-size:1.0rem;
  transition:.4s;
  cursor:pointer;
}
.container1:hover .btn-2{
  box-shadow:0rem 0rem .6rem rgba(188,72,115,.9),inset 0 0 .6rem rgba(188,72,115,.9);
} 

</style>