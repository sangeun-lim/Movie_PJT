<template>
  <table class="table d-flex justify-content-center">
        <thead>
          <!-- <h1>게시판(커뮤니티)</h1> -->
          <div class="wrapper">
            <div class="blackpink">CMMUNITY</div>
          </div>
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
    <!-- <div style="width:100px; height:30px; border: solid pink; margin-left:90%;"> -->
      <div class="frame">
        <router-link v-if="isLoggedIn" :to="{ name: 'reviewNew'}" class="text-decoration-none custom-btn btn-14">Create</router-link>\
      </div>
    <!-- </div> -->
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

 /* title */
.wrapper{
  width: 100%;
  grid-gap: 0.2rem;
  color:white;
  position: relative;
}

.blackpink{
  font-size: 3.5rem;
  font-weight: 700;
  letter-spacing: 8px;
  padding:0rem 2rem;
  border: 10px solid white;
  text-align: center;
  opacity:0;
  border-radius: 5px;
  animation:lightson .5s ease 3 forwards;
}
@keyframes lightson{
  0%{
    opacity:0;
    text-shadow: 0px 0px 0px #FE1DAD, 0px 0px 0px #FE1DAD, 0px 0px 0px #FE1DAD;
    box-shadow: 0px 0px 0px 0px #fe1dad, 0px 0px 0px 0px #fe1dad,0px 0px 0px 0px #fe1dad, inset 0px 0px 0px #FE1DAD;
  }
  20%{
    opacity:0.5;
    text-shadow: 0px 0px 2.5px #FE1DAD, 0px 0px 5px #FE1DAD, 1px 1px 25px #FE1DAD;
    box-shadow: 0px 0px 5px 0px #fe1dad, 0px 0px 10px 0px #fe1dad,0px 0px 50px 0px #fe1dad, inset 0px 0px 20px #FE1DAD;
  }
  40%{
    opacity:0;
    text-shadow: 0px 0px 1px #FE1DAD, 0px 0px 2px #FE1DAD, 0px 0px 10px #FE1DAD;
    box-shadow: 0px 0px 2px 0px #fe1dad, 0px 0px 5px 0px #fe1dad,0px 0px 25px 0px #fe1dad, inset 0px 0px 10px #FE1DAD;
  }
  50%{
    opacity:1;
    text-shadow: 0px 0px 5px #FE1DAD, 0px 0px 10px #FE1DAD, 1px 1px 50px #FE1DAD;
    box-shadow: 0px 0px 10px 0px #fe1dad, 0px 0px 20px 0px #fe1dad,0px 0px 100px 0px #fe1dad, inset 0px 0px 30px #FE1DAD;
  }
  100%{
    opacity:1;
    text-shadow: 0px 0px 5px #FE1DAD, 0px 0px 10px #FE1DAD, 1px 1px 50px #FE1DAD;
    box-shadow: 0px 0px 10px 0px #fe1dad, 0px 0px 30px 0px #fe1dad,0px 0px 100px 0px #fe1dad, inset 0px 0px 30px #FE1DAD;
  }
}

.blackpink span{
  transform: scaleX(-1);
  display: inline-block;
}
.blackpink__tagline{
  text-align: right;
  font-size: .8rem;
}

@media(max-width: 1150px){
  .blackpink{
    font-size: 5rem;
    padding:2rem 0;
    letter-spacing: 2px;
  }
}


@media(max-width: 789px){
  .wrapper{
     width: 100%;
     padding:2rem;
}
  .blackpink{
    font-size: 2rem;
    letter-spacing: 2px;
  }
}

/* button */
.frame {
  width: 90%;
  margin: 40px auto;
  text-align: center;
}

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