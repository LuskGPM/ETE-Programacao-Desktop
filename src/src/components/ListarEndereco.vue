<script setup lang="ts">
import { computed } from 'vue';
import { useMainStore } from '@/store/piniaStore';
import type { Endereco } from '@/schemas/EnderecoSchema';

const store = useMainStore();
const cepEndereco = computed<Endereco>(() => {
    return store.getEndereco()
})
const showEndereco = computed<boolean>(() => {
    return cepEndereco.value.cep !== undefined
})
</script>

<template>
    <ul v-if="showEndereco" class="list-group">
        <li v-for="value, key in cepEndereco" :key="key" class="list-group-item d-flex gap-3">
            <input type="text" class="input" readonly :value="key">
            <input type="text" class="form-control" readonly :value="value">
        </li>
    </ul>
</template>

<style scoped>
.input {
    width: 150px;
    font-weight: bold;
    border: none;
    outline: none;
    text-align: start;
}
</style>