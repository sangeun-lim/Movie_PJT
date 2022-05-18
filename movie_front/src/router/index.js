import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import MovieListView from '@/views/MovieListView.vue'
import NotFound404 from '@/view/NotFound404.vue'
import SignupView from '@/views/SignupView.vue'
import UserProfile from '@/view/UserProfile.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movies',
    component: HomeView
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
    path:'/profile/:username',
    name : 'profile',
    component: UserProfile
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {

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
