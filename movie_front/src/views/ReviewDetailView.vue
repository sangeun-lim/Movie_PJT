<template>
  <div class="board-detail">
    <!-- <div class="board-contents">
      <h2>제목 : {{ review.title }}</h2>
      <div>
        <strong class="w3-large">{{ review.username }}</strong>
        <br>
        <span>{{ review.created_at }}</span>
      </div>
    </div>
    <div class="board-contents">
      <span>내용 : {{ review.content  }}</span>
    </div> -->

    <!-- <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button class="btn w-btn w-btn-blue">Edit</button>
      </router-link>

      <button @click="deleteReview(reviewPk)" class="btn w-btn w-btn-red">Delete</button>
    </div> -->
    <div class="review">
      <div class="d-flex justify-content-between">
        <div>
          <p class="m-0">작성 : {{ review.created_at | moment("YYYY년 MMMM Do a h:mm") }}</p>
          <p class="m-0">수정 : {{ review.updated_at | moment("YYYY년 MMMM Do a h:mm") }}</p>
        </div>
        <div>
          {{ likeCount }}
          <button
            @click="likeReview(reviewPk)"
          class="btn"><i class="fa-solid fa-heart" style="color:red;"></i></button>
        </div>
      </div>
      <hr>
      <h1>{{ review.title }}</h1>
      <div class="text-end m-0 text-secondary">{{ review.user.username }}</div>
      <hr>
      <span>{{ review.content  }}</span>
    </div>
    
    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button class="custom-btn btn-14">Edit</button>
      </router-link>
      <button @click="deleteReview(reviewPk)" class="custom-btn btn-14">Delete</button>
    </div>

    <hr>
    <div class="review">
      <h3 class="text-start">COMMENT</h3>
    </div>
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

<style scoped>
/* form */
.review {
  display: flex;
  flex-direction: column;
  width: 1000px;
  margin: 10px auto;
}
p {
  margin: 0px;
  font-size: 12px;
  color: gray;
}
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


/* button */
.custom-btn {
  color: #fff;
  width: 130px;
  height: 40px;
  padding: 10px 25px;
  margin: 20px;
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