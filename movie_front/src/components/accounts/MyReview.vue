<template>
  <table class="table d-flex justify-content-center" style="color:white">
    <thead>
    <tr>
      <th scope="col">제목</th>
      <th scope="col">좋아요</th>
      <th scope="col">작성시간</th>
    </tr>
    <tr v-for="review in reviews" 
      :key="review.pk">
        <th>
          <router-link :to="{ name: 'review', params: {reviewPk: review.pk} }" class="text-decoration-none">
          {{ review.title }}
          </router-link>
        </th>
        <th>{{ review.like_users_count }}</th>
        <th>{{ review.created_at | moment("YYYY-MMMM-Do-a h:mm") }}</th>
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

<style>

</style>