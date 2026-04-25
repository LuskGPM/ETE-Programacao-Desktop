<script lang="ts" setup>
import { useRouter } from 'vue-router';
import { useMainStore } from '@/store/piniaStore';
import SearchEndereco from '../SearchEndereco.vue';

const store = useMainStore();
const router = useRouter()

function route_to_Home() {
    store.clearEndereco()
    router.push('/');
}

</script>

<template>
    <div class="body d-flex flex-column gap-2 justify-content-start align-items-center">
        <h1 class="text-center p-5 text-light bg-primary fs-1 rounded-1">Central de busca:
            CEP/Endereço</h1>
        <main
            class="d-flex flex-column gap-4 justify-content-center align-items-center bg-warning p-3 pt-5 pb-5 m-5 rounded-1">
            <SearchEndereco />
            <button @click="route_to_Home()" class="btn btn-primary p-3 fs-3 rounded-4">Voltar a tela
                inicial</button>
        </main>
    </div>
</template>

<style scoped>
.body {
    min-width: 100dvw;
    min-height: 100dvh;
}
</style>