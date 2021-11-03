import Vue from 'vue'
import App from './App.vue'
import titleMixin from './mixins/titleMixin'
import Vue2Filters from 'vue2-filters'

Vue.config.productionTip = false
Vue.mixin(titleMixin)
Vue.use(Vue2Filters)

// Import Bootstrap
import 'bootstrap/dist/css/bootstrap.css'

new Vue({
  render: h => h(App),
}).$mount('#app')
