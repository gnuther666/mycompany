import Vue from 'vue'
import Router from 'vue-router'
import titlebar from '@/components/titlebar'
import taskSquare from '@/components/taskSquare'

Vue.use(Router)
const routes = [
  {
    path: '/',
    component: titlebar,
    children: [
      {
        path: 'taskSquare',
        component: taskSquare,
        name: 'taskSquare'
      },
      {
        path: '*',
        component: taskSquare,
        name: 'taskSquare'
      }
    ]
  }
]

const router = new Router({
  routes,
  base: '/',
  mode: 'hash'
})

export default router
