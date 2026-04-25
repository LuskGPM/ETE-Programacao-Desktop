<script lang="ts" setup>
import { useMainStore } from '@/store/piniaStore';
import { computed } from 'vue';

const store = useMainStore();
const cepEnderecoList = computed(() => {
    return store.getListEndereco()
})

const showEndereco = computed<boolean>(() => {
    return cepEnderecoList.value.length > 0
})
</script>

<template>
    <p v-if="!showEndereco">Nenhum endereço encontrado.</p>
    <ul v-else v-for="cepEndereco in cepEnderecoList" class="list-group mb-3">
        <li v-for="value, key in cepEndereco" :key="key" style="list-style: none; ">
            <div v-if="key == 'cep' || key == 'logradouro' || key == 'uf' || key == 'localidade' || key == 'bairro'" class="form-floating mb-2 mt-2">
                <input type="text" class="form-control" id="valueInput" readonly :value="value">
                <label for="valueInput" class="form-label">{{ key }}</label>
            </div>
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