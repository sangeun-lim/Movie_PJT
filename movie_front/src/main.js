import Vue from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'
import '@fortawesome/fontawesome-free/js/all.js'
import vueMoment from 'vue-moment'

Vue.use(vueMoment)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
