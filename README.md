<p align="center">
  <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png" alt="Pokemon Logo" width="150">
</p>

<h1 align="center">
 Pokedex Web
</h1>

# Backend

Este é o backend para a aplicação Pokedex, desenvolvido com Python, Flask, SQLAlchemy e SQLite. A API fornece endpoints para gerenciar capturas de Pokémon, incluindo adição, listagem e exclusão de capturas.

## Funcionalidades

- Listar Pokémons disponíveis
- Adicionar uma nova captura
- Listar capturas existentes
- Excluir uma captura

## Requisitos

- Python 3.8+
- Flask
- SQLAlchemy
- Flask-CORS
- Pydantic

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/mrfrigerio/pokedex.git
   cd pokedex/backend
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

1. Execute a aplicação:

   ```bash
   flask run --host 0.0.0.0 --port 5050 --reload
   ```

2. A documentaçõa da API estará disponível em `http://localhost:5050/openapi`.

# Frontend

Este é o frontend para a aplicação Pokedex, desenvolvido com HTML, CSS e JavaScript. Ele consome a API fornecida pelo backend para gerenciar capturas de Pokémons.

## Funcionalidades

- Formulário para adicionar uma nova captura
- Listagem de capturas existentes
- Exclusão de capturas

## Execução

1. Abra o arquivo `index.html` em um navegador web.

## Como Usar

1. Abra o formulário na página principal.
2. Preencha o nome do treinador e a data de captura.
3. Selecione um Pokémon da lista.
4. Clique no botão "Adicionar Captura".
5. A captura será exibida na tabela abaixo do formulário.
6. Para excluir uma captura, clique no botão "Delete" ao lado da captura na tabela.

## Autor

Projeto desenvolvido por [Marcelo Ragnelli Frigério](https://www.linkedin.com/in/marceloragnelli/).

## Licença

Este projeto está licenciado sob os termos da licença MIT.
