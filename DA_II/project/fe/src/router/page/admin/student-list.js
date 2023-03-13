export default [
  {
    path: 'students',
    name: 'StudentList',
    component: () => import('@/views/admin/students/StudentsList.vue')
  }
]