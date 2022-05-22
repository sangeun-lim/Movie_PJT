import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

import SearchBar from '@/components/SearchBar.vue'

// movies
import HomeView from '@/views/HomeView.vue'
import MovieListView from '@/views/MovieListView.vue'

// community
import ReviewListView from '@/views/ReviewListView.vue'
import ReviewNewView from '@/views/ReviewNewView.vue'
import ReviewEditView from '@/views/ReviewEditView.vue'
import ReviewDetailView from '@/views/ReviewDetailView.vue'

// accounts
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import SignupView from '@/views/SignupView.vue'
import MyPageView from '@/views/MypageView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movies',
    name: 'movies',
    component: MovieListView
  },
  {
    path: '/movies/search/:keyword',
    name: 'SearchMovies',
    component: SearchBar
  },
  {
    path: '/community',
    name: 'community',
    component: ReviewListView
  },
  {
    path: '/community/new',
    name: 'reviewNew',
    component: ReviewNewView
  },
  {
    path: '/community/:reviewPk',
    name: 'review',
    component: ReviewDetailView
  },
  {
    path: '/community/:reviewPk/edit',
    name: 'reviewEdit',
    component: ReviewEditView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path:'/mypage/:username',
    name : 'mypage',
    component: MyPageView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

// router.beforeEach((to, from, next) => {
//   // 이전 페이지에서 발생한 에러메시지 삭제
//   store.commit('SET_AUTH_ERROR', null)

//   const { isLoggedIn } = store.getters

//   const noAuthPages = ['login', 'signup']

//   const isAuthRequired = !noAuthPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     alert('Require Login. Redirecting..')
//     next({ name: 'login' })
//   } else {
//     next()
//   }

//   if (!isAuthRequired && isLoggedIn) {
//     next({ name: 'movies' })
//   }
// })

export default router
