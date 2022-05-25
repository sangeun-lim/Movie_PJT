<template>
  <form @submit.prevent="onSubmit">
    <!-- <div class="container-fluid px-1 px-md-5 px-lg-1 px-xl-5 py-5 mx-auto bg-black np">
      <div class="card border-0 bg-black">
        <div class="row d-flex justify-content-center">
          <div class="mt-5 col-6">
            <div class="card border-0 px-4 py-5">
              <div>
                <p><label for="title">제목:<input type="text" v-model="newReview.title" id="title" required placeholder="제목을 입력하세요"></label></p>
              </div>
              <div>
                <p><label for="content">내용:<input v-model="newReview.content" id="content" type="text" style="height: 200px" required placeholder="내용을 입력하세요"></label></p>
              </div>
            </div>
              <button>{{ action }}</button>
          </div>
        </div>
      </div>
    </div> -->
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
  </form>
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

<style>
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
</style>