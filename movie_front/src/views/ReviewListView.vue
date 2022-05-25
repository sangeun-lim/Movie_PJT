<template>
  <table class="table d-flex justify-content-center">
        <thead>
          <!-- <h1>게시판(커뮤니티)</h1> -->
          <h1 class="neon" data-text="U">WEL<span class="flicker-slow">COM </span>COM<span class="flicker-fast">MUN</span>ITY</h1>
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
            <th>{{review.created_at | moment("YYYY년 MMMM Do a h:mm") }}</th>
            <th>{{review.updated_at | moment("YYYY년 MMMM Do a h:mm")  }}</th>
          </tr>
    <br>
    <br>
    <div style="width:100px; height:30px; border: solid pink; margin-left:90%;">
      <router-link v-if="isLoggedIn" :to="{ name: 'reviewNew'}" class="text-decoration-none" style="color: #f3c6e4 ">새 글 작성</router-link>
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

<style scoped>
table {
  border-collapse: collapse;
  
}
tr {
  border-top: 1px solid black;
  border-bottom: 1px solid black;
}
tr:nth-child(odd) {
  background-color: #f3c6e4;
}
tr:nth-child(even) {
  background-color: #f4c7fa;
}
tr:hover {
  background-color : #ffc5c2;
  cursor: pointer;
}
td {
  padding: 5px;
}

.neon {
  font-family: "Monoton", cursive;
  font-size: 50px;
  color: #ffd5ff;
  position: relative;
  top: 0%;
  left: 50%;
  transform: translate(-50%, 30%);
  font-weight: 400;
  letter-spacing: 8px;
  text-shadow: 1px 0px 4px #ffd5ff, 2px 0px 4px #ffd5ff, 3px 0px 4px #ffd5ff, 2px 0px 3px #d42cca, 2px 3px 15px #d42cca, 2px 0px 15px, 5px 0px 125px, 20px 0vw 200px #d42cca, 40px 0vw 200px #d42cca;
}

.flicker-slow {
  animation: flicker 3s linear infinite;
}

.flicker-fast {
  animation: flicker 1s linear infinite;
}

@keyframes flicker {
    0%, 19.999%, 22%, 62.999%, 64%, 64.999%, 70%, 100% {
    opacity: 0.99;
  }
    20%, 21.999%, 63%, 63.999%, 65%, 69.999% {
    opacity: 0.4;
  }
}
</style>