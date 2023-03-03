import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '@/views/HomePage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
    // beforeEnter: checkAuth,
  },

  // ADMIN

  // {
  //   path: '/admin/students',
  //   name: 'AdminStudent',
  //   component: () => import('../components/admin/students/StudentsList.vue'),
  // },
  {
    path: '/admin/students',
    // name: 'StudentsList',
    component: () => import('../components/admin/students/StudentsList.vue'),
    children: [
      // {
      //   path: 'edit',
      //   component: () => import('../components/admin/students/'),
      // },
    ]
  },
  {
    path: '/admin/projects',
    name: 'ProjectsList',
    component: () => import('../components/admin/projects/ProjectsList.vue'),
    children: [
      // {
      //   path: 'edit',
      //   component: () => import('../components/admin/students/'),
      // },
    ]
  },
  {
    path: '/admin/internships',
    name: 'InternshipsList',
    component: () => import('../components/admin/internships/InternshipsList.vue'),
    children: [
      // {
      //   path: 'edit',
      //   component: () => import('../components/admin/students/'),
      // },
    ]
  },
  {
    path: '/admin/lecturers',
    name: 'LecturersList',
    component: () => import('../components/admin/lecturers/LecturersList.vue'),
    children: [
      // {
      //   path: 'edit',
      //   component: () => import('../components/admin/students/'),
      // },
    ]
  },
  {
    path: '/admin',
    name: 'AdminPage',
    component: HomePage,
    children: [
      {
        path: 'students',
        // name: 'StudentsList',
        component: () => import('../components/admin/students/StudentsList.vue'),
        children: [
          // {
          //   path: 'edit',
          //   component: () => import('../components/admin/students/'),
          // },
        ]
      },
      {
        path: 'projects',
        name: 'ProjectsList',
        component: () => import('../components/admin/projects/ProjectsList.vue'),
        children: [
          // {
          //   path: 'edit',
          //   component: () => import('../components/admin/students/'),
          // },
        ]
      },
      {
        path: 'internships',
        name: 'InternshipsList',
        component: () => import('../components/admin/internships/InternshipsList.vue'),
        children: [
          // {
          //   path: 'edit',
          //   component: () => import('../components/admin/students/'),
          // },
        ]
      },
      {
        path: 'lecturers',
        name: 'LecturersList',
        component: () => import('../components/admin/lecturers/LecturersList.vue'),
        children: [
          // {
          //   path: 'edit',
          //   component: () => import('../components/admin/students/'),
          // },
        ]
      },
    ]
  },

  // CLIENT
  {
    path: '/student/:id',
    name: 'StudentList',
    params: {id: 2},
    component: () => import('../components/student/StudentList.vue'),
    children: [
      // {
      //   path: 'edit',
      //   component: () => import('../components/admin/students/'),
      // },
    ]
  },
  {
    path: '/cv',
    name: 'CvForm',
    component: () => import('../components/student/CvForm.vue'),
    children: [
      // {
      //   path: 'edit',
      //   component: () => import('../components/admin/students/'),
      // },
    ]
  },
  {
    path: '/project_register',
    name: 'ProjectRegister',
    component: () => import('../components/student/ProjectForm.vue'),
    children: [
      // {
      //   path: 'edit',
      //   component: () => import('../components/admin/students/'),
      // },
    ]
  },


  {path: '*', component: () => import('../views/error/NotFound.vue')}
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes,
})

export default router