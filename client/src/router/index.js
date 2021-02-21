import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component: () => import('@/views/Index')
  },
  {
    path: '/rejected',
    name: 'Rejected',
    component: () => import('@/views/Rejected')
  },
  {
    path: '*',
    name: '404',
    component: () => import('@/views/404')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
