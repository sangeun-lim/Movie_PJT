import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default{
  // namespaced: true,

  // state는 직접 접근하지 않고
  state: {
    token: localStorage.getItem('token') || '',  // 값이 있으면 기본 token 넣어주고 없으면 '' 넣어주기
    currentUser: {},
    mypage: {},
    authError: null
  },
  
  // 모든 state는 getters를 통해서 접근
  getters: {
    isLoggedIn: state => !!state.token, 
    currentUser: state => state.currentUser,
    mypage: state => state.mypage,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`})
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_MYPAGE: (state, mypage) => state.mypage = mypage,
    SET_AUTH_ERROR: (state, error) => state.authError = error
  },

  actions: {
    saveToken({ commit }, token){
      // state.token 추가
      // localStorage에 token 추가
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },
    
    removeToken({ commit }){
      // state.token 삭제
      // localStorage에 token 삭제
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    signup({ commit, dispatch }, credentials) {
      // POST: 사용자 입력정보를 signup URL로 보내기
      // 성공하면:
      //  응답 토큰 저장
      //  현재 사용자 정보 받기
      //  메인 페이지로 이동
      // 실패하면:
      //  에러메시지
      axios({
        url: drf.accounts.signup(),
        method:'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'movies' })
        })
        .catch(err => {
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    // signup 끝나고, login 끝나고 쓰임
    fetchCurrentUser({ commit, getters, dispatch }) {
      /*
      get: 사용자가 로그인 했다면 (토큰을 가지고 있다면)
        currentUserInfo url로 요청보내기
          성공하면
            state.currentUser에 저장
          실패하면( 토큰이 요상하다면 )
            기존 토큰 삭제
            LoginView로 이동
      */
     if (getters.isLoggedIn){
       axios({
         url: drf.accounts.currentUserInfo(),
         method: 'get',
         headers: getters.authHeader,
       })
        .then(res => commit('SET_CURRENT_USER', res.data))
        .catch(err => {
          if (err.response.status === 401){
            dispatch('removeToken')
            router.push({ name: 'login' })
          }
        })
     }
    },

    login( {commit, dispatch }, credentials ){
      // POST: 사용자 입력정보를 signup URL로 보내기
      // 성공하면:
      //  응답 토큰 저장
      //  현재 사용자 정보 받기
      //  메인 페이지로 이동
      // 실패하면:
      //  에러메시지
      axios({
        url: drf.accounts.login(),
        method:'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'movies' })
        })
        .catch(err => {
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    
    logout({ getters, dispatch }){
      /*
      POSt : token을 logout url로 보내기
        성공하면
          토큰 삭제
          사용자 알람
          LoginView로 이동
        실패하면
          에러메시지   
       */
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(() => {
        dispatch('removeToken')
        alert('로그아웃 되었습니다.')
        router.push({ name: 'login' })
      })
      // 약간의 수정 필요할수도 
      .catch(err => {
        console.error(err.response)
      })
    },
    fetchMypage({ commit, getters }, {username}){
      // GET: mypage url로 요청보내기
      //  성공하면
      //    state.mypage에 저장
      axios({
        url: drf.accounts.mypage(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MYPAGE', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    }
  }
}