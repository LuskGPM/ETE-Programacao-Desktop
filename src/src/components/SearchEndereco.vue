<script setup lang="ts">
import { ref, type Ref } from 'vue';
import { useMainStore } from '@/store/piniaStore';
import ListarEndereco from './ListarEndereco.vue';

const input_cep: Ref<string> = ref('')
const mainStore = useMainStore();

async function buscarCep(): Promise<void> {
    const cep_to_search = input_cep.value.replace('-', '');
    if (cep_to_search == undefined || cep_to_search.length != 8)
        alert('Digite um CEP válido');

    else await mainStore.setEndereco(cep_to_search);
}

function criarMascaraCep(): void {
    if (input_cep.value.length == 8) input_cep.value = input_cep.value.replace(/(\d{5})(\d{3})/, '$1-$2');
}

</script>

<template>
    <form class="container-sm row gap-4" @submit.prevent="buscarCep()">
        <div class="col-4 bg-light rounded-4 p-5 h-25">
            <label for="campoCep" class="form-label mb-3">Digite seu CEP</label>
            <input type="text" id="campoCep" v-model="input_cep" @input="criarMascaraCep()" class="form-control mb-3" placeholder="Ex: 12345-678" maxlength="9">
            <button type="submit" class="btn btn-primary">Buscar CEP</button>
        </div>
        <div class="col bg-light rounded-4 p-5">
            <ListarEndereco />
        </div>
    </form>
</template>