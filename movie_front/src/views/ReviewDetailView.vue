<template>
  <!-- <div>
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
  </div> -->
  <div class="board-detail">
    <div class="board-contents">
      <h2>제목 : {{ review.title }}</h2>
      <div>
        <strong class="w3-large">{{ review.username }}</strong>
        <br>
        <span>{{ review.created_at }}</span>
      </div>
    </div>
    <div class="board-contents">
      <span>내용 : {{ review.content  }}</span>
    </div>

    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button class="btn w-btn w-btn-blue">Edit</button>
      </router-link>

      <button @click="deleteReview(reviewPk)" class="btn w-btn w-btn-red">Delete</button>
    </div>

    <div>
      {{ likeCount }}
      <button
        @click="likeReview(reviewPk)"
      class="btn"><i class="fa-solid fa-heart" style="color:red;"></i></button>
    </div>
    
    <hr>
<!-- #ffd5ff -->
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
.w-btn-blue {
    background-color: #6aafe6;
    color: #d4dfe6;
}
.w-btn-red {
    background-color: #ff5f2e;
    color: #e1eef6;
}
</style>