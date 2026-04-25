import { defineStore } from "pinia";
import { ref, type Ref } from "vue";
import { ApiCep } from "@/services/api";
import type { Endereco } from "@/schemas/EnderecoSchema";

export const useMainStore = defineStore('main', () => {
    const ObjEndereco: Ref<Endereco> = ref({} as Endereco)
    const listEndereco: Ref<Endereco[]> = ref([] as Endereco[])

    function getEndereco(): Endereco {
        return ObjEndereco.value
    }

    function getListEndereco(): Endereco[] {
        return listEndereco.value
    }

    function clearEndereco(): void {
        ObjEndereco.value = {} as Endereco
    }

    function clearListEndereco(): void {
        listEndereco.value = [] as Endereco[]
    }

    async function setEndereco(cep: string): Promise<void> {
        const response: Endereco = await ApiCep.getEndereco(cep)
        ObjEndereco.value = response
    }

    async function setListEndereco(UF: string, cidade: string, rua: string): Promise<void> {
        console.log(`setListEndereco: ${UF}, ${cidade}, ${rua}`)
        const response: Endereco[] = await ApiCep.getCep(UF, cidade, rua)
        listEndereco.value = response
    }

    return { setEndereco, getEndereco, setListEndereco, getListEndereco, clearEndereco, clearListEndereco }
})