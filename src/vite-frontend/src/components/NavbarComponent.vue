<script setup>
import { Menu, Badge, Avatar } from 'primevue';
import { ref } from "vue";
import { useRouter } from 'vue-router';
    
const router = useRouter();

const items = ref([
    {
        separator: true
    },
    {
        label: 'Questions',
        items: [
            {
                label: 'New',
                icon: 'pi pi-plus',
                shortcut: '⌘+N'
            },
            {
                label: 'List',
                icon: 'pi pi-search',
                shortcut: '⌘+S',
                command: () => {
                    router.push('/home');
                }
            }
        ]
    },
    {
        label: 'Profile',
        items: [
            {
                label: 'Settings',
                icon: 'pi pi-cog',
                shortcut: '⌘+O'
            },
            {
                label: 'Messages',
                icon: 'pi pi-inbox',
                badge: 2
            },
            {
                label: 'Logout',
                icon: 'pi pi-sign-out',
                shortcut: '⌘+Q'
            }
        ]
    },
    {
        separator: true
    }
]);

</script>

<template>
    <main>
        <div class="card flex min-h-screen">
            <Menu :model="items" class="w-full md:w-60">
                <template #start>
                    <span class="inline-flex items-center gap-1 px-2 py-2">
                        <i class="pi pi-question" />
                        <span class="text-xl font-semibold">QUESTION<span class="text-primary">TIME</span></span>
                    </span>
                </template>
                <template #submenulabel="{ item }">
                    <span class="text-primary font-bold">{{ item.label }}</span>
                </template>
                <template #item="{ item, props }">
                    <a class="flex items-center" v-bind="props.action">
                        <span :class="item.icon" />
                        <span>{{ item.label }}</span>
                        <Badge v-if="item.badge" class="ml-auto" :value="item.badge" />
                        <span v-if="item.shortcut" class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1">{{ item.shortcut }}</span>
                    </a>
                </template>
                <template #end>
                    <button class="relative overflow-hidden w-full border-0 bg-transparent flex items-start p-1 pl-4 hover:bg-surface-100 rounded cursor-pointer transition-colors duration-200">
                        <Avatar image="/avatar.svg" class="mr-2" shape="circle" size="xlarge"/>
                        <span class="inline-flex flex-col items-start">
                            <span class="font-bold">Lorenzo Ricci</span>
                            <span class="text-sm">Admin</span>
                        </span>
                    </button>
                </template>
            </Menu>
        </div>
    </main>
</template>

