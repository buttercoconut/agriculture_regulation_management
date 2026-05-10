import { createRouter, createWebHistory } from 'vue-router';
import RegulationSearch from '@/components/RegulationSearch.vue';
import RegulationDetail from '@/components/RegulationDetail.vue';

const routes = [
  { path: '/', component: RegulationSearch },
  { path: '/regulations/:id', component: RegulationDetail, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
