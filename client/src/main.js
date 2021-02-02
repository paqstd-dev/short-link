import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// axios http requests
import axios from 'axios'
Vue.prototype.$axios = axios.create({
  baseURL: `${ document.location.protocol }//${ document.location.hostname }/`
})

// validate form data
import Vuelidate from 'vuelidate'
Vue.use(Vuelidate)

// copy links
import VueClipboard from 'vue-clipboard2'
Vue.use(VueClipboard)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
