<template>
  <div class="search-container">
    <input v-model="keyword" placeholder="검색어를 입력하세요" />
    <button @click="search">검색</button>
  </div>
  <ul>
    <li v-for="reg in regulations" :key="reg.id" @click="selectRegulation(reg)">
      {{ reg.title }}
    </li>
  </ul>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { getRegulations } from '@/api/regulation';

const keyword = ref('');
const regulations = ref([] as any[]);

async function search() {
  regulations.value = await getRegulations({ keyword: keyword.value });
}

function selectRegulation(reg: any) {
  // navigate to detail page (simple alert for demo)
  alert(`선택된 규정: ${reg.title}`);
}
</script>

<style scoped>
.search-container {
  margin-bottom: 1rem;
}
</style>
