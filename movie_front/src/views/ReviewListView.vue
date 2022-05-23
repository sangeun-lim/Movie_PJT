<template>
  <table class="table d-flex justify-content-center">
        <thead>
          <h1>게시판(커뮤니티)</h1>
          <br>
         <tr>
            <th scope="col">#</th>
            <th scope="col">작성자</th>
            <th scope="col">제목</th>
            <th scope="col">댓글 수</th>
            <th scope="col">좋아요 수</th>
            <th scope="col">작성 시간</th>
            <th scope="col">수정 시간</th>
          </tr>
          <tr v-for="review in reviews" :key="review.pk">
            <th >{{review.pk}}</th>
            <th> {{review.user.username}} </th>
            <th> <router-link :to="{ name: 'review', params: {reviewPk: review.pk} }" class="text-decoration-none">
            {{ review.title }}
          </router-link></th>
            <th>{{review.comment_count}}</th>
            <th>{{review.like_count}}</th>
            <th>{{review.created_at | moment("dddd, MMMM Do YYYY, h:mm:ss a") }}</th>
            <th>{{review.updated_at | moment("dddd, MMMM Do YYYY, h:mm:ss a")  }}</th>
          </tr>
    <br>
    <br>
    <div style="width:100px; height:30px; border: solid red; margin-left:90%;">
      <router-link v-if="isLoggedIn" :to="{ name: 'reviewNew'}" class="text-decoration-none" style="color: #141619 ">새 글 작성</router-link>
    </div>
        </thead>

  </table>

</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ReviewListView',
  computed: {
    ...mapGetters(['reviews'])
  },
  methods: {
    ...mapActions(['fetchReviews','isLoggedIn'])
  },
  created() {
    this.fetchReviews()
  },
}
</script>

<style>

</style>