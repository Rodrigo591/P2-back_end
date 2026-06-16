# API de Gerenciamento de Produtos

Projeto desenvolvido para a disciplina de Desenvolvimento Web utilizando FastAPI, SQLAlchemy, PostgreSQL, Docker e Pytest.

## Objetivo

Implementar uma API REST para gerenciamento de produtos, permitindo:

* Cadastro de produtos
* Consulta de produtos
* Consulta por ID
* Atualização de produtos
* Exclusão de produtos

Além disso, o projeto demonstra:

* Persistência de dados utilizando PostgreSQL
* Uso de ORM com SQLAlchemy
* Injeção de dependências com FastAPI
* Testes automatizados utilizando Pytest
* Isolamento de testes utilizando banco dedicado
* Containerização com Docker

---

## Tecnologias Utilizadas

* Python 3.13
* FastAPI
* SQLAlchemy
* PostgreSQL
* Docker
* Docker Compose
* Pytest
* HTTPX
* Python Dotenv

---

## Estrutura do Projeto

```text
.
├── main.py
├── conftest.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── .env
├── README.md
└── tests
    ├── __init__.py
    └── test_produtos.py
```

---

## Configuração do Ambiente

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
cd projeto_fastapi_produtos
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Variáveis de Ambiente

Arquivo `.env`:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/produtos
TEST_DATABASE_URL=postgresql://postgres:postgres@test_db:5432/test_db
```

---

## Executando os Containers

Subir os bancos PostgreSQL:

```bash
docker compose up -d
```

Verificar containers:

```bash
docker ps
```

Parar containers:

```bash
docker compose down
```

---

## Executando a API

```bash
uvicorn main:app --reload
```

Documentação automática:

* Swagger UI: http://localhost:8000/docs
* ReDoc: http://localhost:8000/redoc

---

## Endpoints

### Criar Produto

POST `/produtos`

Exemplo:

```json
{
  "nome": "Mouse Gamer",
  "preco": 199.90,
  "estoque": 15,
  "ativo": true
}
```

---

### Listar Produtos

GET `/produtos`

---

### Buscar Produto por ID

GET `/produtos/{id}`

---

### Atualizar Produto

PUT `/produtos/{id}`

---

### Remover Produto

DELETE `/produtos/{id}`

---

## Testes Automatizados

Executar todos os testes:

```bash
pytest
```

Executar com detalhes:

```bash
pytest -v
```

---

## Testes Automatizados

Executar todos os testes:

```bash
pytest
```

Executar com detalhes:

```bash
pytest -v
```

---

## Resultado Esperado dos Testes

Execução:

```bash
python -m pytest -v
```

Exemplo de saída:

```text
======================== test session starts ========================

collected 13 items

tests/test_produtos.py::test_lista_vazia PASSED
tests/test_produtos.py::test_criar_produto PASSED
tests/test_produtos.py::test_listagem PASSED
tests/test_produtos.py::test_buscar_por_id PASSED
tests/test_produtos.py::test_buscar_inexistente PASSED
tests/test_produtos.py::test_deletar PASSED
tests/test_produtos.py::test_deletar_confirmar PASSED
tests/test_produtos.py::test_deletar_inexistente PASSED
tests/test_produtos.py::test_payload_invalido[payload0] PASSED
tests/test_produtos.py::test_payload_invalido[payload1] PASSED
tests/test_produtos.py::test_isolamento PASSED
tests/test_produtos.py::test_atualizar_produto PASSED
tests/test_produtos.py::test_atualizar_produto_inexistente PASSED

======================== 13 passed ========================
```

---

## Estratégia de Testes

Os testes utilizam:

* Banco de testes dedicado
* Fixture `client`
* Fixture `produto_existente`
* Isolamento entre execuções
* Criação e remoção automática das tabelas

### Como o isolamento funciona

O isolamento é garantido pela fixture `client`, que cria as tabelas antes de cada teste utilizando `Base.metadata.create_all()` e remove todas as tabelas ao final utilizando `Base.metadata.drop_all()`. Dessa forma, cada teste executa em um ambiente limpo e independente dos demais.

---

## Estratégia de Testes

Os testes utilizam:

* Banco de testes dedicado
* Fixture `client`
* Fixture `produto_existente`
* Isolamento entre execuções
* Criação e remoção automática das tabelas

Cenários testados:

* Listagem de produtos
* Cadastro de produtos
* Busca por ID
* Busca de produto inexistente
* Atualização de produto
* Atualização de produto inexistente
* Exclusão de produto
* Exclusão de produto inexistente
* Validação de payload inválido
* Isolamento dos testes

---

## Docker

O projeto utiliza dois containers PostgreSQL:

### Banco de Desenvolvimento

* Porta 5432
* Persistência de dados através de volume Docker

### Banco de Testes

* Porta 5433
* Utilizado exclusivamente pelos testes automatizados

Ambos possuem healthcheck configurado para verificar disponibilidade.

---

## Autor

Projeto acadêmico desenvolvido para fins de estudo e avaliação da disciplina.
