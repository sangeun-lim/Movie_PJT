import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  // namespaced : true,

  state: {
    movieData: [],
    movie: [],
    comments : [],

  },
  getters: {
    movieData: state => state.movieData,
    movie: state => state.movie,
    comments: state => state.comments,
    
  },
  mutations: {
    SET_MOVIEDATA: (state, movieData) => state.movieData = movieData,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_COMMENTS: (state, comments) => state.comments = comments
  },

  actions: {

  }
}