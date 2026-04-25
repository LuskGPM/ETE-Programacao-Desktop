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
        <h1 class="text-center p-5 text-light rounded-1 bg-primary fs-1" style="width: 100dvw;">Central de busca:
            CEP/Endereço</h1>
        <main class="d-flex flex-column gap-4 justify-content-center bg-warning p-4 rounded-1 m-5"
            style="width: 100dvw;">
            <button @click="route_to_searchCEP()" class="btn btn-primary fs-3 m-2 rounded-4">Buscar via CEP</button>
            <button @click="route_to_searchEndereco()" class="btn btn-primary p-3 m-2 fs-3 rounded-4">Buscar via
                Endereço</button>
        </main>
    </div>
</template>

<style scoped>
.body {
    min-width: 100dvw;
    min-height: 100dvh;
}
</style>