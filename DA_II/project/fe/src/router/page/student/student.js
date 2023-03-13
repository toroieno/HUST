import LoginPage from '@/pages/LoginPage.vue'
import RegisterPage from '@/pages/RegisterPage.vue'
import StudentPage from '@/views/student/HomePage.vue'

import CVForm from './cv'
import ProjectForm from './project'
import StudentInfo from './infomation'

import checkAuth from './auth.js'

export default [
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/register', name: 'RegisterPage', component: RegisterPage },
  {
    path: '/',
    name: 'StudentPage',
    component: StudentPage,
    beforeEnter: checkAuth,
    children: [
      ...CVForm,
      ...ProjectForm,
      ...StudentInfo,
    ]
  }
]