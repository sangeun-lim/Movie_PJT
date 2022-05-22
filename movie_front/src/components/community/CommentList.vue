<template>
  <div class="comment-list">
    
    <ul>
      <comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </comment-list-item>

      <!-- <p v-for="comment in comments"
      :comment="comment"
      :key="comment.pk">
      내용 : {{comment.content}} |
      작성시간 : {{comment.created_at}} |
      수정시간 : {{comment.updated_at}}
      </p>         -->
    </ul>

    <comment-list-form></comment-list-form>
  </div>
</template>

<script>
import CommentListItem from '@/components/community/CommentListItem.vue'
import CommentListForm from '@/components/community/CommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { 
    CommentListForm,
    CommentListItem 
  },
  props: { 
    comments: Array
  },
}
</script>

<style>
.comment-list {
  border: 1px solid blue;
}
</style>