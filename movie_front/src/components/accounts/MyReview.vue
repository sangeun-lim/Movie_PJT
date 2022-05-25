<template>
  <table class="table d-flex justify-content-center" style="color:white">
    <thead>
    <tr class="table-title">
      <th scope="col">title</th>
      <th scope="col">like</th>
      <th scope="col">created time</th>
    </tr>
    <tr v-for="review in reviews" 
      :key="review.pk">
        <th>{{ review.title }}</th>
        <th>{{ review.like_users_count }}</th>
        <th>{{ review.created_at | moment("YYYY-MMMM-Do-a h:mm") }}</th>
        <router-link :to="{ name: 'review', params: {reviewPk: review.pk} }" class="text-decoration-none custom-btn btn-14 p-1 m-3" style="width: 90px">Detail</router-link>
    </tr>
    </thead>
  </table>
</template>

<script>
export default {
  name: 'MyReview',
  props: {
    reviews : Array
  }
}
</script>

<style scoped>
table {
  border-collapse: collapse;
  color: white;
  font-size: 1.2rem;
}
tr {
  border-top: 1px solid black;
  border-bottom: 1px solid black;
}
th {
  padding: 15px;
}
.table-title {
  font-size: 1.5rem;
  color: #FE1DAD
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