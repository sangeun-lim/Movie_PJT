<template>
  <div>
    <h1>게시글 작성하기</h1>
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
.neon {
  font-family: "Monoton", cursive;
  font-size: 50px;
  color: #ffd5ff;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, 30%);
  font-weight: 400;
  letter-spacing: 8px;
  text-shadow: 1px 0px 4px #ffd5ff, 2px 0px 4px #ffd5ff, 3px 0px 4px #ffd5ff, 2px 0px 3px #e01305, 2px 3px 15px #d42cca, 2px 0px 15px, 5px 0px 125px, 20px 0vw 200px #e9d418, 40px 0vw 200px #28da5e;
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