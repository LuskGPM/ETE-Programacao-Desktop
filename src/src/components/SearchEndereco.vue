<script setup lang="ts">
import { ref, type Ref } from 'vue';
import { useMainStore } from '@/store/piniaStore';

const input_cep: Ref<string> = ref('')
const mainStore = useMainStore();

function buscarCep(): void {
    const cep_to_search = input_cep.value.replace('-', '');
    if (cep_to_search == undefined || cep_to_search.length != 8) 
        alert('Digite um CEP válido');

    else mainStore.setEndereco(cep_to_search);
}

function criarMascaraCep(): void {
    if (input_cep.value.length == 8) input_cep.value = input_cep.value.replace(/(\d{5})(\d{3})/, '$1-$2');
}

</script>

<template>
    <label for="campoCep">Digite seu CEP</label>
    <input type="text" id="campoCep" v-model="input_cep" @input="criarMascaraCep()">
    <button @click="buscarCep()">Buscar CEP</button>
</template>