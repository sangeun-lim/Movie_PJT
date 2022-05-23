<template>
  <div>
    <ul>
      <li v-for="review in reviews" 
      :key="review.pk">
        <router-link :to="{ name: 'review', params: {reviewPk: review.pk} }" class="text-decoration-none">
            {{ review.title }}
        </router-link>
      </li>
    </ul>
  </div>
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