<template>
  <div>
    <h1 class="neon-h1">Create Review</h1>
    <!-- <h1 class="neon" data-text="U"><span class="flicker-slow">게</span>시<span class="flicker-slow">글</span>작<span class="flicker-fast">성</span></h1> -->
    <review-form :review="review" action="create"></review-form>
  </div>
</template>

<script>
import ReviewForm from '@/components/community/ReviewForm.vue'

export default {
  name: 'ReviewNewView',
  components: { 
    ReviewForm 
  },
  data() {
    return {
      review: {
        pk: null,
        title: '',
        content: '',
      }
    }
  }
}
</script>

<style>

</style>