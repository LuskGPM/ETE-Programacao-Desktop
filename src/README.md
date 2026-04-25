# Projeto de Busca de CEP e Endereço

Este projeto é uma aplicação web construída com **Vue 3**, **TypeScript**, **Vite**, **Pinia**, **Vue Router** e **Bootstrap 5**. O sistema utiliza a API pública **ViaCEP** para localizar informações de endereço a partir de um CEP ou para buscar CEPs a partir de estado, cidade e logradouro.

![Imagem da interface do aplicativo](../img/aplicativo-desktop.png)

## Funcionalidades

- Página inicial com opções para buscar por:
  - CEP
  - Endereço (UF, cidade e logradouro)
- Busca por CEP:
  - Entrada de CEP com máscara no formato `00000-000`
  - Consulta direta à API ViaCEP
  - Exibição dos dados retornados: CEP, logradouro, bairro, localidade, UF
- Busca por endereço:
  - Seleção de Unidade Federativa (UF) dividida por regiões do Brasil
  - Entrada de cidade e logradouro
  - Consulta à API ViaCEP para listar resultados associados
  - Exibição de lista de endereços com campos principais

## Estrutura do projeto

- `src/main.ts`
  - Inicializa a aplicação Vue
  - Registra o roteador (`vue-router`)
  - Registra o estado global com `pinia`
  - Importa estilos do Bootstrap
- `src/App.vue`
  - Contém o componente de rota principal (`<router-view />`)
- `src/router/index.ts`
  - Define as rotas da aplicação:
    - `/` → `HomeView`
    - `/search-cep` → `CepView`
    - `/search-endereco` → `EnderecoView`
- `src/store/piniaStore.ts`
  - Armazena dados de endereço e lista de endereços
  - Define ações para buscar dados pela API
  - Exporta funções reativas consumidas pelos componentes
- `src/services/api.ts`
  - Faz requisições HTTP com `axios`
  - Conecta à API `https://viacep.com.br/ws/`
  - Métodos:
    - `getEndereco(cep)`
    - `getCep(UF, cidade, rua)`
- `src/schemas/EnderecoSchema.ts`
  - Modelo TypeScript para os dados de endereço retornados pela API

## Componentes principais

- `src/components/view/HomeView.vue`
  - Tela inicial com botões para navegar para cada modo de busca
- `src/components/view/CepView.vue`
  - Tela para buscar endereço a partir de CEP
- `src/components/view/EnderecoView.vue`
  - Tela para buscar CEPs a partir de endereço
- `src/components/SearchEndereco.vue`
  - Formulário de busca por CEP e exibição de resultado
- `src/components/SearchCEP.vue`
  - Formulário de busca por UF, cidade e logradouro
  - Mostra lista de resultados com base na pesquisa
- `src/components/ListarEndereco.vue`
  - Exibe os dados de endereço retornados para o CEP informado
- `src/components/ListarEnderecoList.vue`
  - Exibe a lista de endereços retornados pela busca por endereço

## Como o sistema foi construído

1. **Roteamento**
   - A aplicação utiliza `vue-router` para navegação entre telas sem recarregar a página.
2. **Estado global**
   - `pinia` armazena os resultados da consulta e permite que múltiplos componentes acessem os dados.
3. **Requisições HTTP**
   - `axios` faz chamadas à API ViaCEP para obter dados de endereço e CEP.
4. **Base de dados externa**
   - A API ViaCEP retorna JSON com informações de endereço para consultas por CEP ou busca por cidade/rua.
5. **Interface**
   - Bootstrap é usado para a aparência e componentes visuais básicos.
   - Os formulários usam `v-model` para sincronizar os campos de entrada com o estado reativo do Vue.

## Dependências principais

- `vue`
- `vue-router`
- `pinia`
- `axios`
- `bootstrap`
- `vite`
- `typescript`

## Como rodar

No diretório `src`:

```sh
npm install
npm run dev
```

A aplicação ficará disponível no endereço mostrado pelo Vite, geralmente `http://localhost:5173`.

## Observações

- A busca por endereço depende dos dados disponíveis na API ViaCEP e pode retornar vários resultados.
- A busca por CEP exige um valor válido de 8 dígitos.
- O projeto está organizado para ser facilmente estendido com novas formas de busca ou melhorias de interface.
