<template>
  <div>
    <!-- <form @submit.prevent="onSubmit">
      <table style="padding-top:50px" align=center width=700 border=0 cellpadding=2>
        <tr>
          <td bg-color=white>
            <table class="table2">
              <tr>
                <td>제목</td>
                <td><input type="text" name="name" size=83 v-model="newReview.title" id="title" required placeholder="제목을 입력하세요" ></td>
              </tr>

              <tr>
                <td>내용</td>
                <td><textarea name="content" cols="85" rows="15" v-model="newReview.content" id="content" type="text" required placeholder="내용을 입력하세요">
                  </textarea></td>
              </tr>
              
              <center>
                <button class="btn1">{{ action }}</button>
              </center>
            </table>
          </td>
        </tr>
      </table>
    </form> -->

    <form class="form" @submit.prevent="onSubmit">
      <div class="input">
        <input type="text" placeholder="placeholder"  v-model="newReview.title" required/>
        <label>
          <span>Title</span>
        </label>
      </div>
      <div class="input">
        <textarea type="text" placeholder="placeholder" v-model="newReview.content" style="height:300px" required></textarea>
        <label>
          <span>Content</span>
        </label>
      </div>
      <center>
        <button class="custom-btn btn-14">{{ action }}</button>
      </center>
    </form>

  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ReviewForm',
    props: {
      review: Object,
      action: String,
    },
    data() {
      return {
        newReview: {
          title: this.review.title,
          content: this.review.content,
        }
      }
    },

    methods: {
      ...mapActions(['createReview', 'updateReview']),
      onSubmit() {
        if (this.action === 'create') {
          this.createReview(this.newReview)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.review.pk,
            ...this.newReview,
          }
          this.updateReview(payload)
        }
      },
    },
  }
  
</script>

<style scoped>
  table.table2 {
    border-collapse: separate;
    border-spacing: 1px;
    text-align: left;
    line-height: 1.5;
    border-top: 1px solid #ccc;
    margin : 25px 10px;
  }

  table.table2 tr {
    width: 50px;
    padding:10px;
    font-weight: bold;
    vertical-align: top;
    border-bottom: 1px solid #ccc;
  }

  table.table2 td {
    width: 100px;
    padding: 10px;
    vertical-align: top;
    border-bottom: 1px solid #ccc;
  }

  .btn1 {
    /* margin-left:2px; */
    border: 1px solid hotpink;
    background-color: #fff;
    color: hotpink;
    padding: 5px;
  }

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
  width: 1000px;
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
  padding-bottom: 32px;
}

.input textarea:focus ~ label,
.input textarea:not(:placeholder-shown) ~ label {
  padding-bottom: 300px;
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
  font-size: 1.2rem;
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