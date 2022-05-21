const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const COMMUNITY = 'community/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 마이페이지 제공
    mypage: username => HOST + ACCOUNTS + 'mypage/' + username,
  },

  community: {
    reviews: () => HOST + COMMUNITY,
    review: reviewPk => HOST + COMMUNITY + `${reviewPk}/`,
    likeReview: reviewPk => HOST + COMMUNITY + `${reviewPk}/` + 'like/',
    comments: reviewPk => HOST + COMMUNITY + `${reviewPk}/` + 'comments/',
    comment: (reviewPk, commentPk) => HOST + COMMUNITY + `${reviewPk}/` + 'comments/' + `${commentPk}/`,
  },

  movies: {
    movies: () => HOST + MOVIES,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    likeMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',
    comments: moviePk => HOST + MOVIES + `${moviePk}/` + 'comments/',
    comment: (moviePk, commentPk) =>  HOST + MOVIES + `${moviePk}/` + 'comments/' + `${commentPk}/`,
  },

}
