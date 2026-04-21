<script setup lang="ts">
import { useMainStore } from '@/store/piniaStore';
import { reactive, ref, type Ref } from 'vue';


const norteUF = reactive({
    "AC": "Acre",
    "AP": "Amapá",
    "AM": "Amazonas",
    "PA": "Pará",
    "RO": "Rondônia",
    "RR": "Roraima",
    "TO": "Tocantins"
})

const nordesteUF = reactive({
    "AL": "Alagoas",
    "BA": "Bahia",
    "CE": "Ceará",
    "MA": "Maranhão",
    "PB": "Paraíba",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RN": "Rio Grande do Norte",
    "SE": "Sergipe"
})

const centroOesteUF = reactive({
    "DF": "Distrito Federal",
    "GO": "Goiás",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul"
})

const sudesteUF = reactive({
    "ES": "Espírito Santo",
    "MG": "Minas Gerais",
    "RJ": "Rio de Janeiro",
    "SP": "São Paulo"
})

const sulUF = reactive({
    "PR": "Paraná",
    "RS": "Rio Grande do Sul",
    "SC": "Santa Catarina"
})

const store = useMainStore()

const UF: Ref<string> = ref('')
const cidade: Ref<string> = ref('')
const logradouro: Ref<string> = ref('')

async function buscarCEP(): Promise<void> {
    
}
</script>

<template>
    <h2> Digite os dados para encontrar o CEP</h2>
    <label for="UF">Selecione a unidade federativa</label>
    <select name="UF" id="UF">
        <optgroup label="Norte">
            <option v-for="(value, key) in norteUF" :key="key" :value="key">{{ value }}</option>
        </optgroup>
        <optgroup label="Nordeste">
            <option v-for="(value, key) in nordesteUF" :key="key" :value="key">{{ value }}</option>
        </optgroup>
        <optgroup label="Centro-Oeste">
            <option v-for="(value, key) in centroOesteUF" :key="key" :value="key">{{ value }}</option>
        </optgroup>
        <optgroup label="Sudeste">
            <option v-for="(value, key) in sudesteUF" :key="key" :value="key">{{ value }}</option>
        </optgroup>
        <optgroup label="Sul">
            <option v-for="(value, key) in sulUF" :key="key" :value="key">{{ value }}</option>
        </optgroup>
    </select>
    <label for="cidade">Nome da cidade</label>
    <input type="text" id="cidade">
    <label for="logradouro">Logradouro</label>
    <input type="text" id="logradouro">
    <button @click="buscarCEP()">Buscar CEP</button>
</template>