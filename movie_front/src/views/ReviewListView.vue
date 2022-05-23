<template>
  <div>
    <h1>Community</h1>
    <div>
      <router-link v-if="isLoggedIn" :to="{ name: 'reviewNew'}">새 글 작성</router-link>
    </div>
    <div>
      <div v-for="review in reviews" :key="review.pk">
        {{ review.user.username }}

        <router-link :to="{ name: 'review', params: {reviewPk: review.pk} }">
          {{ review.title }}
        </router-link>

        => {{ review.comment_count }} | {{ review.like_count }}
      </div>
    </div>
  </div>
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