<script setup lang="ts">
import { computed, ref, type Ref } from 'vue';
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
    <ul v-if="showEndereco">
        <li v-for="value, key in cepEndereco" :key="key">
            <input type="text" readonly :value="key">
            <input type="text" readonly :value="value">
        </li>
    </ul>
</template>