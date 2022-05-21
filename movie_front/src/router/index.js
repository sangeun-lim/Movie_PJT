import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

// movies
import HomeView from '@/views/HomeView.vue'
import MovieListView from '@/views/MovieListView.vue'

// community
import CommunityView from '@/views/CommunityView.vue'

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
    path: '/community',
    name: 'community',
    component: CommunityView
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
  routes
})

export default router
