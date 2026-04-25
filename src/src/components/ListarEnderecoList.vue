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
    <ul v-show="showEndereco" v-for="cepEndereco in cepEnderecoList" class="list-group">
        <li v-for="value, key in cepEndereco" :key="key" class="list-group-item d-flex gap-3">
            <div v-if="key == 'cep' || key == 'logradouro' || key == 'uf' || key == 'localidade' || key == 'bairro'">
                <input type="text" class="input" readonly :value="key">
                <input type="text" class="form-control" readonly :value="value">
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