<template>
  <div>
    <h1>Regulation Search</h1>
    <input v-model="keyword" placeholder="Search keyword" />
    <select v-model="category">
      <option value="">All Categories</option>
      <option v-for="c in categories" :key="c.id" :value="c.id">{{ c.name }}</option>
    </select>
    <button @click="search">Search</button>
    <ul>
      <li v-for="reg in regulations" :key="reg.id">
        <router-link :to="{ name: 'RegulationDetail', params: { id: reg.id } }">{{ reg.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getRegulations } from '../api/regulation'

const keyword = ref('')
const category = ref('')
const categories = ref([])
const regulations = ref([])

const search = async () => {
  const res = await getRegulations({ keyword: keyword.value, category: category.value })
  regulations.value = res.data
}

onMounted(async () => {
  // fetch categories
})
</script>
