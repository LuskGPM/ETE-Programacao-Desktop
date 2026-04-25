import { createRouter, createWebHistory } from "vue-router";

import CepView from "@/components/view/CepView.vue";
import EnderecoView from "@/components/view/EnderecoView.vue";
import HomeView from "@/components/view/HomeView.vue";

const routes = [
    { path: '/', component: HomeView },
    { path: '/search-cep', component: CepView },
    { path: '/search-endereco', component: EnderecoView }
]

export const router = createRouter({
    history: createWebHistory(),
    routes,
})