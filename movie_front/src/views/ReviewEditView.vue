<template>
  <div>
    <h1 class="neon-h1">Update</h1>
    <review-form v-if="isReview" :review="review" action="update">
    </review-form>
  </div>
</template>

<script>
import ReviewForm from '@/components/community/ReviewForm.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewEditView',
  components: { 
    ReviewForm 
  },
  computed: {
    ...mapGetters(['review', 'isReview',])
  },
  methods: {
    ...mapActions(['fetchReview'])
  },
  create() {
    this.fetchReview(this.$route.params.reviewPk)
  },
}
</script>

<style>
.neon-h1 {
  color: #f1aad7;
  text-shadow: 0 0 5px #FE1DAD, 0 0 15px #FE1DAD;
}

</style>