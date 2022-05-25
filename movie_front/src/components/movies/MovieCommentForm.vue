<template>
  <div>
  <!-- <form @submit.prevent="onSubmit" class="comment-list-form">
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
    </form> -->

    <form class="form" @submit.prevent="onSubmit">
      <div class="d-flex">
        <div class="input">
          <textarea type="text" placeholder="placeholder"  v-model="content" style="height:50px" required></textarea>
          <label>
            <span>Comment</span>
          </label>
        </div>
        <div class="input" style="width:80px">
          <input type="number" placeholder="content" v-model="score" min="1" max="5" style="width:80px" required/>
          <label>
            <span>Score</span>
          </label>
        </div>
      </div>
      <center>
        <button class="custom-btn btn-14 m-3">Comment</button>
      </center>
    </form>
  </div>
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

<style scoped>
/* form */
.input:not(.invalid) input:focus ~ label::after, .input:not(.invalid) textarea:focus ~ label::after {
  background-color: #FE1DAD;
  box-shadow: 0 0 9px 3px #FE1DAD;
}

.neon-text, .input:not(.invalid) input:focus ~ label span,
.input:not(.invalid) input:not(:placeholder-shown) ~ label span, .input:not(.invalid) textarea:focus ~ label span,
.input:not(.invalid) textarea:not(:placeholder-shown) ~ label span, .neon-h1 {
  color: #FE1DAD;
  text-shadow: 0 0 5px #FE1DAD, 0 0 15px #FE1DAD;
}

.form {
  display: flex;
  padding: 40px;
  flex-direction: column;
  width: 700px;
  gap: 46px;
  margin: 10px auto;
}

.input {
  position: relative;
  width: 100%;
}
.input * {
  transition: 300ms;
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
.input label {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  padding-bottom: 10px;
  padding-left: 6px;
  color: #999;
  font-size: 1.5rem;
  pointer-events: none;
}
.input label small.message {
  opacity: 0;
}
.input label::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 1px;
  width: 100%;
  transition: ease-in 400ms;
  background-color: #FE1DAD;
}
.input input:focus ~ label,
.input input:not(:placeholder-shown) ~ label {
  padding-bottom: 50px;
}

.input textarea:focus ~ label,
.input textarea:not(:placeholder-shown) ~ label {
  padding-bottom: 50px;
}
/* .input input:focus ~ label span,
.input input:not(:placeholder-shown) ~ label span {
  font-size: 14px;
} */

/* button */
.custom-btn {
  color: #fff;
  width: 130px;
  height: 40px;
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
}

.btn-14 {
  position: relative;
  color: #FE1DAD;
  border: none;
  z-index: 2;
}
.btn-14:before,
.btn-14:after {
  position: absolute;
  content: "";
  width: 20%;
  height: 20%;
  border: 1px solid;
  
  z-index: -1;
  transition: all 0.3s ease;
}
.btn-14:before{
   top: 0;
   left: 0;
   border-bottom-color: transparent;
   border-right-color: transparent;
   border-top-color: #FE1DAD;
   border-left-color: #FE1DAD;
}
.btn-14:after{
   bottom: 0;
   right: 0;
   border-top-color: transparent;
   border-left-color: transparent;
   border-bottom-color: #FE1DAD;
   border-right-color: #FE1DAD;
}
.btn-14:hover:before,
.btn-14:hover:after {
  border-color: #FE1DAD;
  height: 100%;
  width: 100%;
  box-shadow: 0 0 5px #FE1DAD, 0 0 5px #FE1DAD inset;
}
</style>