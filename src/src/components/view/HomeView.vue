<script lang="ts" setup>
import { useRouter } from 'vue-router';

const router = useRouter()

function route_to_searchCEP() {
    router.push('/search-cep');
}

function route_to_searchEndereco() {
    router.push('/search-endereco');
}
</script>

<template>
    <div class="body d-flex flex-column gap-2 justify-content-start align-items-center">
        <h1 class="text-center mt-5 p-5 w-75 text-light rounded-4 bg-primary fs-1">Central de busca: CEP/Endereço</h1>
        <main class="d-flex flex-row gap-4 justify-content-center bg-warning p-5 w-75 rounded-4 m-5">
            <button @click="route_to_searchCEP()" class="btn btn-primary p-3 fs-3 rounded-4">Buscar via CEP</button>
            <button @click="route_to_searchEndereco()" class="btn btn-primary p-3 fs-3 rounded-4">Buscar via Endereço</button>
        </main>
    </div>
</template>

<style scoped>
.body {
    min-width: 100dvw;
    min-height: 100dvh;
}
</style>