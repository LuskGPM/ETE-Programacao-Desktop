<script setup lang="ts">
import SearchCEP from '../SearchCEP.vue';
import { useRouter } from 'vue-router';

const router = useRouter()

function route_to_Home() {
    router.push('/');
}
</script>

<template>
    <div class="body d-flex flex-column gap-2 justify-content-start align-items-center">
        <h1 class="text-center p-5 text-light bg-primary fs-1 rounded-1" style="width: 100dvw;">Central de busca:
            CEP/Endereço</h1>
        <main class="d-flex flex-column gap-4 justify-content-center bg-warning p-2 pt-5 pb-5 m-5 rounded-1"
            style="width: 100dvw;">
            <SearchCEP />
            <button @click="route_to_Home()" class="btn btn-primary p-3 fs-3 rounded-4">Voltar a tela
                inicial</button>
        </main>
    </div>
</template>