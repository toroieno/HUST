import StudentList from './student-list'
import LecturerList from './lecturer-list'
import ProjectList from './project-list'
import InternshipList from './internship-list'
import DashboardView from './dashboard'
import LoginForm from './login'

export default [
  {
    path: '/admin',
    name: 'AdminPage',
    component: () => import('@/layouts/admin/Layout/LayoutBar.vue'),
    children: [
      ...DashboardView,
      ...StudentList,
      ...LecturerList,
      ...ProjectList,
      ...InternshipList,
    ]
  },
  ...LoginForm,
]