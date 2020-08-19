from fastapi.testclient import TestClient

from canivete.routers.textos import router

client = TestClient(router)


def test_extrai_emails():
    """ Testa se extrai corretamente emails. """
    response = client.post(
        "/emails",
        json={
            "texto":
            "Esse texto contém os emails teste@teste.com e novo@novo.com.br"
        })
    assert response.status_code == 200
    assert response.json() == ['teste@teste.com', 'novo@novo.com.br']


def test_extrai_telefone():
    response = client.post(
        "/telefones",
        json={
            "texto":
            "Esse texto contém os telefones 11999999999 e 6112341234 e (21)12345-6789."
        })
    assert response.status_code == 200
    assert response.json() == ['11999999999', '6112341234', '(21)12345-6789']


def test_extrai_nomes():
    response = client.post("/nomes",
                           json={"texto": "Nome: José Francisco Souza Xavier e trabalha longe."})
    assert response.status_code == 200
    assert response.json() == ['José Francisco Souza Xavier']
