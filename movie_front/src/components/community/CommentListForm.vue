<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <!-- <div class="card mb-2">
      <div class="card-header bg-dark">
             <i class="fa fa-comment fa"></i> 댓글 작성 <i class="fa fa-comment fa"></i>
      </div>
      <div class="card-body">
        <div class="list-group list-group-flush">
            <div class="list-group-item">
                <textarea type="text" id="comment" v-model="content" required class="mx-3" cols="70" rows="3"></textarea>
                <div>
                  <button class="btn btn-dark mt-3">comment</button>
                </div>
            </div>
        </div>
      </div>
    </div> -->
    <table style="padding-top:50px;" align=center width=700 border=0 cellpadding=2>
      <tr>
        <td style="background-color:pink;">
          <table class="table2">
            <tr style="color:black">
              <td><i class="fa fa-comment fa"></i> 댓글 작성 <i class="fa fa-comment fa"></i></td>
            </tr>

            <tr>
              <td><textarea type="text" id="comment" v-model="content" required class="mx-3" cols="70" rows="4"></textarea></td>
            </tr>
            
            <div>
              <button class="btn btn-dark mt-3">comment</button>
            </div>
          </table>
        </td>
      </tr>
    </table>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['review']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ reviewPk: this.review.pk, content: this.content, })
      this.content = ''
    },
  }
}
</script>

<style>

</style>