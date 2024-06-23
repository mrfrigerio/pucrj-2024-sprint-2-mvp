<p align="center">
  <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png" alt="Pokemon Logo" width="150">
</p>

# Pokedex API

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
   cd pokedex-api/backend
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

## Autor

Projeto desenvolvido por [Marcelo Ragnelli Frigério](https://www.linkedin.com/in/marceloragnelli/).

## Licença

Este projeto está licenciado sob os termos da licença MIT.
