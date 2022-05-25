<template>
  <table>

  <div class="comment-list-item">
    <span v-if="!isEditing">{{ payload.content }} || 작성 시간 : {{ this.comment.created_at | moment("YYYY-MMMM-Do a h:mm")  }} || 수정 시간 : {{ this.comment.updated_at | moment("YYYY-MMMM-Do a h:mm")  }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button class="w-btn w-btn-pink" type="button" @click="onUpdate">수정</button> |
      <button class="w-btn w-btn-gra1 w-btn-gra-anim" type="button" @click="switchIsEditing">취소</button>
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing" class="mx-3">
      <button class="w-btn w-btn-gra1" type="button" @click="switchIsEditing">수정</button> |
      <button class="w-btn w-btn-gra1 w-btn-gra-anim" type="button" @click="deleteComment(payload)">삭제</button>
    </span>
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

</style>