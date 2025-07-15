<script setup>
  import { RouterView } from 'vue-router'
  import { ref } from 'vue';
  import { Menubar, InputText, Avatar } from 'primevue';

  const items = ref([
    {
      label: 'Home',
      icon: 'pi pi-home'
    },
    {
      label: "Questions",
      icon: "pi pi-question"
    },
    {
      label: "Answers",
      icon: "pi pi-check"
    }
  ])
</script>

<template>
  <header>
    <div class="wrapper">
      <Menubar :model="items">
        <template #end>
          <div class="nav-end">
            <InputText placeholder="Search" type="text" class="w-32 sm:w-auto" />
            <Avatar image="/avatar.svg" shape="circle" size="xlarge"/>
          </div>
        </template>
      </Menubar>
    </div>
  </header>
  <RouterView />
</template>

<style scoped>
  header {
    line-height: 1;
    max-height: 100vh;
  }
  .nav-end{
    display: flex;
    align-items: center;
  }
</style>
