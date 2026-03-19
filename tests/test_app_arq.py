import pytest
from unittest.mock import patch
from app import create_app
from exceptions import ResourceNotFoundError


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_rota_dados_sucesso(client):
    mock_retorno = {
        "pais": "brasil",
        "capital": "Brasília",
        "quantidade_idiomas": 1,
        "idiomas": ["Portuguese"]
    }

    with patch(
        "services.pais_service.PaisService.buscar_dados",
        return_value=mock_retorno
    ):
        response = client.get("/api/v1/pais/dados/brasil")


    assert response.status_code == 200
    assert response.get_json()["capital"] == "Brasília"

def test_rota_dados_nao_encontrado(client):
    with patch(
        "services.pais_service.PaisService.buscar_dados",
        side_effect=ResourceNotFoundError("País não encontrado")
    ):
        response = client.get("/api/v1/pais/dados/paisfake")

    assert response.status_code == 404
    assert response.get_json()["error"]["type"] == "RESOURCE_NOT_FOUND"
    assert response.get_json()["error"]["message"] == "País não encontrado"
