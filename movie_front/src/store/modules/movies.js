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
    SET_MOVIE_COMMENTS: (state, comments) => state.comments = comments
  },

  actions: {
    fetchMovies({ commit }) {
      /* 영화 목록 받아오기
      GET: movies URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.movies(),
        method: 'get',
      })
        .then(res => commit('SET_MOVIEDATA', res.data))
        .catch(err => console.error(err.response))
    },

    fetchMovie({ commit }, moviePk) {
      /* 단일 영화 받아오기
      GET: movie URL (token)
        성공하면
          응답으로 받은 게시글들을 state.movies에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    
    likeMovie({ commit, getters }, moviePk) {
      /* 좋아요
      POST: likemovie URL(token)
        성공하면
          state.movie 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

    createComment({ commit, getters }, { moviePk , content }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.movie의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.movies.comments(moviePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateComment({ commit, getters }, { moviePk, commentPk, content }) {
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.movie의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.movies.comment(moviePk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteComment({ commit, getters }, { moviePk, commentPk }) {
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.movie의 comments 갱신
          실패하면
            에러 메시지 표시
      */
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.comment(moviePk, commentPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIE_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },
  }
}