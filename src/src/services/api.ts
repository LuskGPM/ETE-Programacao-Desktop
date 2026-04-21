import axios from "axios";
import { type Endereco } from "@/schemas/EnderecoSchema";

class Api {
    private api = axios.create({
        baseURL: "https://viacep.com.br/ws/"
    })

    public async getEndereco(cep: string): Promise<Endereco> {
        const response = await this.api.get(`${cep}/json/`)
        return response.data
    }

    public async getCep(UF: string, cidade: string, rua: string): Promise<Endereco[]> {
        const response = await this.api.get(`${UF}/${cidade}/${rua}/json/`)
        return response.data
    }
}

export const ApiCep = new Api()