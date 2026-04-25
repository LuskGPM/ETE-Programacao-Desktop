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
    <p v-if="!showEndereco">Nenhum endereço encontrado.</p>
    <ul v-else class="list-group">
        <li v-for="value, key in cepEndereco" :key="key" class="form-floating mb-3" style="list-style: none;">
            <input type="text" id="valueInput" class="form-control" readonly :value="value">
            <label for="valueInput">{{key}}</label>
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