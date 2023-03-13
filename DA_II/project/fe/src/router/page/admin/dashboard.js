export default [
  {
    path: '',
    name: 'DashboardList',
    component: () => import('@/views/admin/dashboard/DashboardView.vue')
  },
  {
    path: 'dashboard',
    name: 'DashboardView',
    component: () => import('@/views/admin/dashboard/DashboardView.vue')
  },
]