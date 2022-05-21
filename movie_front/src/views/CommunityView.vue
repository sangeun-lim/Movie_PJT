<template>
  <div>
    <h1>Community</h1>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'CommunityView',
  computed: {
    ...mapGetters(['review'])
  },
  methods: {
    ...mapActions(['fetchReview'])
  },
  created() {
    this.fetchReview
  }
}
</script>

<style>

</style>