import LoginPage from '@/pages/LoginPage.vue'
import RegisterPage from '@/pages/RegisterPage.vue'
import StudentPage from '@/views/student/StudentPage.vue'

import CVForm from './cv'
import ProjectForm from './project'
import StudentInfo from './infomation'
import HomePage from './home'

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
      ...HomePage,
      ...CVForm,
      ...ProjectForm,
      ...StudentInfo,
    ]
  }
]