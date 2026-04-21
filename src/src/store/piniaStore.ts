import { defineStore } from "pinia";
import { ref } from "vue";
import { ApiCep } from "@/services/api";

export const useMainStore = defineStore('main', () => {
    const jsonCep = ref({})

    function getJsonCep(): any {
        return jsonCep.value
    }

    async function setJsonCep(cep: string) {
        jsonCep.value = await ApiCep.getCep(cep)
    }

    return { jsonCep, setJsonCep }
})