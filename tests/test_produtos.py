import pytest

def test_lista_vazia(client):
    assert client.get("/produtos").status_code == 200

def test_criar_produto(client):
    r = client.post("/produtos", json={"nome":"Mouse","preco":10})
    assert r.status_code == 201

def test_listagem(client):
    client.post("/produtos", json={"nome":"Mouse","preco":10})
    assert len(client.get("/produtos").json()) == 1

def test_buscar_por_id(client):
    p = client.post("/produtos", json={"nome":"Mouse","preco":10}).json()
    assert client.get(f"/produtos/{p['id']}").status_code == 200

def test_buscar_inexistente(client):
    assert client.get("/produtos/999").status_code == 404

def test_deletar(client):
    p = client.post("/produtos", json={"nome":"Mouse","preco":10}).json()
    assert client.delete(f"/produtos/{p['id']}").status_code == 204

def test_deletar_confirmar(client):
    p = client.post("/produtos", json={"nome":"Mouse","preco":10}).json()
    client.delete(f"/produtos/{p['id']}")
    assert client.get(f"/produtos/{p['id']}").status_code == 404

def test_deletar_inexistente(client):
    assert client.delete("/produtos/999").status_code == 404

@pytest.mark.parametrize("payload",[
    {"nome":"","preco":10},
    {"nome":"x","preco":0},
])
def test_payload_invalido(client,payload):
    assert client.post("/produtos", json=payload).status_code == 422

def test_isolamento(client):
    assert isinstance(client.get("/produtos").json(), list)
