import axios from "axios";

class Api {
    private api = axios.create({
        baseURL: "https://viacep.com.br/ws/"
    })

    public async getCep(cep: string): Promise<JSON> {
        const response = await this.api.get(`${cep}/json/`)
        return response.data
    }
}

export const ApiCep = new Api()