import Vue from 'vue'
import VueRouter from 'vue-router'
import AdminPage from '@/router/page/admin/admin'
import StudentPage from '@/router/page/student/student'

Vue.use(VueRouter)

const routes = [
  ...StudentPage,
  ...AdminPage,
  // CLIENT
  // { 
  //   path: '/',
  //   name: 'HomePage',
  //   component: HomePage,
  //   beforeEnter: checkAuth,
  //   children: [
  //     {
  //       path: '/student/:id',
  //       name: 'StudentList',
  //       params: {id: 2},
  //       component: () => import('../components/student/StudentList.vue'),
  //       children: [
  //         // {
  //         //   path: 'edit',
  //         //   component: () => import('../components/admin/students/'),
  //         // },
  //       ]
  //     },
  //     {
  //       path: '/cv',
  //       name: 'CvForm',
  //       component: () => import('../components/student/CvForm.vue'),
  //       children: [
  //         // {
  //         //   path: 'edit',
  //         //   component: () => import('../components/admin/students/'),
  //         // },
  //       ]
  //     },
  //     {
  //       path: '/project_register',
  //       name: 'ProjectRegister',
  //       component: () => import('../components/student/ProjectForm.vue'),
  //       children: [
  //         // {
  //         //   path: 'edit',
  //         //   component: () => import('../components/admin/students/'),
  //         // },
  //       ]
  //     },
  //   ] 
  // },

  {path: '*', component: () => import('../views/error/NotFound.vue')}
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes,
})

export default router