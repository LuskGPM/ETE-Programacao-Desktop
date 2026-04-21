<script setup lang="ts">
import { ref, type Ref } from 'vue';
import { useMainStore } from '@/store/piniaStore';

const input_cep: Ref<string> = ref('')
const mainStore = useMainStore();

function buscarCep(): void {
    if (input_cep.value == undefined || input_cep.value.length != 8) 
        alert('Digite um CEP válido');

    else mainStore.setJsonCep(input_cep.value);
}

function criarMascaraCep(): void {
    if (input_cep.value.length == 8) input_cep.value = input_cep.value.replace(/(\d{5})(\d{3})/, '$1-$2');
}

</script>

<template>
    <label for="campoCep">Digite seu CEP</label>
    <input type="text" id="campoCep" v-model="input_cep" @input="criarMascaraCep()">
    <button @click="buscarCep()" :disabled="input_cep.length !== 8">Buscar CEP</button>
</template>