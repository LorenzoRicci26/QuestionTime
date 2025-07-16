<script setup>
  import { RouterView } from 'vue-router'
  import NavBarComponent from './components/NavBarComponent.vue'
</script>

<template>
  <div class="flex">
    <aside>
      <NavBarComponent />
    </aside>
    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>

<style setup>
.main-content {
  flex: 1;
  height: 100vh;
  overflow-y: auto;
  padding: 20px;
  background-color: #ffffff;
}
</style>
