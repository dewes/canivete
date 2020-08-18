from fastapi.testclient import TestClient

from app.routers.textos import router

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
