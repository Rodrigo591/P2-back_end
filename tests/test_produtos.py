import pytest


def test_lista_vazia(client):
    response = client.get("/produtos")

    assert response.status_code == 200
    assert response.json() == []


def test_criar_produto(client):
    response = client.post(
        "/produtos",
        json={
            "nome": "Mouse",
            "preco": 10
        }
    )

    assert response.status_code == 201


def test_listagem(client, produto_existente):
    response = client.get("/produtos")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_buscar_por_id(client, produto_existente):
    response = client.get(
        f"/produtos/{produto_existente['id']}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == produto_existente["id"]


def test_buscar_inexistente(client):
    response = client.get("/produtos/999")

    assert response.status_code == 404


def test_deletar(client, produto_existente):
    response = client.delete(
        f"/produtos/{produto_existente['id']}"
    )

    assert response.status_code == 204


def test_deletar_confirmar(client, produto_existente):
    client.delete(
        f"/produtos/{produto_existente['id']}"
    )

    response = client.get(
        f"/produtos/{produto_existente['id']}"
    )

    assert response.status_code == 404


def test_deletar_inexistente(client):
    response = client.delete("/produtos/999")

    assert response.status_code == 404


@pytest.mark.parametrize(
    "payload",
    [
        {
            "nome": "",
            "preco": 10
        },
        {
            "nome": "Produto",
            "preco": 0
        }
    ]
)
def test_payload_invalido(client, payload):
    response = client.post(
        "/produtos",
        json=payload
    )

    assert response.status_code == 422


def test_isolamento(client):
    response = client.get("/produtos")

    assert isinstance(response.json(), list)


def test_atualizar_produto(
    client,
    produto_existente
):
    response = client.put(
        f"/produtos/{produto_existente['id']}",
        json={
            "nome": "Mouse Gamer",
            "preco": 300,
            "estoque": 20,
            "ativo": True
        }
    )

    assert response.status_code == 200

    dados = response.json()

    assert dados["nome"] == "Mouse Gamer"
    assert dados["preco"] == 300


def test_atualizar_produto_inexistente(client):
    response = client.put(
        "/produtos/999",
        json={
            "nome": "Teste",
            "preco": 100,
            "estoque": 1,
            "ativo": True
        }
    )

    assert response.status_code == 404