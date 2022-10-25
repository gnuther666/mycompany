import Vue from 'vue'
import Router from 'vue-router'
import titlebar from '@/components/titlebar'
import taskSquare from '@/components/taskSquare'
import UserManager from '@/components/Manager/UserManager'

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
        path: 'UserManager',
        component: UserManager,
        name: 'UserManager'
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
