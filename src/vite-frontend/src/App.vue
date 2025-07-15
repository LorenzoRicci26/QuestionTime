<script setup>
  import { RouterView, RouterLink } from 'vue-router'
  import NavBarComponent from './components/NavBarComponent.vue'
</script>

<template>
  <header>
    <NavBarComponent />
    <div class="wrapper">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </div>
  </header>
  <RouterView />
</template>
