import Vue from 'vue'
import Vuex from 'vuex'
import vueMoment from 'vue-moment'
import moment from "moment"

import accounts from './modules/accounts'
import movies from './modules/movies'
import community from './modules/community'

import createPersistedState from 'vuex-persistedstate'

moment.locale("ko")

Vue.use(Vuex)
Vue.use(vueMoment, { moment })

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  modules: { accounts, movies , community },
})
