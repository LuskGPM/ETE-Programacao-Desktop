<script lang="ts" setup>
import { useRouter } from 'vue-router';
import SearchEndereco from '../SearchEndereco.vue';

const router = useRouter()

function route_to_Home() {
    router.push('/');
}

</script>

<template>
    <div class="body d-flex flex-column gap-2 justify-content-start align-items-center">
        <h1 class="text-center mt-5 p-5 w-75 text-light rounded-4 bg-primary fs-1">Central de busca: CEP/Endereço</h1>
        <main class="d-flex flex-column gap-4 justify-content-center align-items-center bg-warning p-5 w-75 rounded-4 m-5">
            <SearchEndereco />
            <button @click="route_to_Home()" class="btn btn-primary p-3 fs-3 rounded-4 w-25">Voltar a tela inicial</button>
        </main>
    </div>
</template>

<style scoped>
.body {
    min-width: 100dvw;
    min-height: 100dvh;
}
</style>