<template>
  <form @submit.prevent="onSubmit">
    <div class="container-fluid px-1 px-md-5 px-lg-1 px-xl-5 py-5 mx-auto bg-black np">
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
    </div>
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

</style>