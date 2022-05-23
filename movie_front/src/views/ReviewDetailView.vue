<template>
  <div>
    <h1>제목 : {{ review.title }}</h1>
    <div>
      <p>내용 : {{ review.content }}</p>  
    </div>

    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button class="btn btn-outline-info">Edit</button>
      </router-link>
      |
      <button @click="deleteReview(reviewPk)" class="btn btn-outline-danger">Delete</button>
    </div>
    
    <div>
      Likeit:
      <button
        @click="likeReview(reviewPk)"
      class="btn btn-outline-dark">{{ likeCount }}</button>
    </div>

    <hr>
    <comment-list :comments="review.review_comments"></comment-list>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CommentList from '@/components/community/CommentList.vue'

export default {
  name: 'ReviewDetailView',
  components: { CommentList },
  data() {
    return {
      reviewPk: this.$route.params.reviewPk,
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'review']),
    likeCount() {
      return this.review.like_users?.length
    }
  },
  methods: {
    ...mapActions(['fetchReview', 'likeReview', 'deleteReview',])
  },
  created() {
    this.fetchReview(this.reviewPk)
  },
}
</script>

<style>

</style>