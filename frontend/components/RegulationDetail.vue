<template>
  <div class="detail-container">
    <h2>{{ regulation.title }}</h2>
    <p>{{ regulation.content }}</p>
    <p><strong>카테고리:</strong> {{ regulation.category.name }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getRegulation } from '@/api/regulation';

const route = useRoute();
const regulation = ref<any>(null);

onMounted(async () => {
  const id = route.params.id;
  regulation.value = await getRegulation(id);
});
</script>

<style scoped>
.detail-container {
  padding: 1rem;
}
</style>
