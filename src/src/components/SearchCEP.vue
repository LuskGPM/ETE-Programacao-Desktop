<script setup lang="ts">
import { useMainStore } from '@/store/piniaStore';
import { reactive, ref, type Ref } from 'vue';
import ListarEnderecoList from './ListarEnderecoList.vue';


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

const UF: Ref<string> = ref('AC')
const cidade: Ref<string> = ref('')
const logradouro: Ref<string> = ref('')
const loading: Ref<boolean> = ref(false)

async function buscarCEP(): Promise<void> {
    loading.value = true
    await store.setListEndereco(UF.value, cidade.value, logradouro.value)
    loading.value = false
}
</script>

<template>
    <div class="container-sm d-flex flex-column gap-4">
        <div class="bg-light p-4 rounded-4 h-25">
            <h2 class="mb-3">Digite os dados para encontrar o CEP</h2>
            <label for="UF" class="form-label">Selecione a unidade federativa</label>
            <select name="UF" id="UF" class="w-100 form-select-lg mb-3" v-model="UF">
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
            <label for="cidade" class="form-label">Nome da cidade</label>
            <input type="text" id="cidade" class="form-control mb-3" v-model="cidade">
            <label for="logradouro" class="form-label">Logradouro</label>
            <input type="text" id="logradouro" class="form-control mb-3" v-model="logradouro">
            <button @click="buscarCEP()" class="btn btn-primary">Buscar CEP</button>
        </div>
        <div class="bg-light p-4 rounded-4">
            <div class="spinner-border" role="status" v-if="loading">
                <span class="visually-hidden">Loading...</span>
            </div>
            <ListarEnderecoList v-else />
        </div>
    </div>
</template>