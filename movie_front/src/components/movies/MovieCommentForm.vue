<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <!-- <div class="card mb-2">
      <div class="card-header bg-light">
              <i class="fa fa-comment fa"></i> REPLY
      </div>
      <div class="card-body">
        <ul class="list-group list-group-flush">
            <li class="list-group-item">
                <textarea type="text" id="comment" v-model="content" required class="mx-3" cols="70" rows="3"></textarea>
                평점 :<input type="number" v-model="score" required min="1" max="5" >
                <div>
                  <button class="btn btn-dark mt-3">post reply</button>
                </div>
            </li>
        </ul>
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
              <td>평점 :<input type="number" v-model="score" required min="1" max="5" ></td>
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
  name: 'MovieCommentForm',
  data() {
    return {
      content: '',
      score: null,
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createMovieComment']),
    onSubmit() {
      this.createMovieComment({ moviePk: this.movie.movie_id, content: this.content, score: this.score })
      this.content = ''
      this.score = ''
    }
  }
}
</script>

<style>

</style>