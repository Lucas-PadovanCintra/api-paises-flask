import pytest
from unittest.mock import Mock
from services.pais_service import PaisService
from exceptions import ResourceNotFoundError


def test_buscar_dados_sucesso():

    mock_client = Mock()

    mock_client.buscar_pais.return_value = [
        {
            "capital": ["Brasília"],
            "languages": {"por": "Portuguese"}
        }
    ]

    service = PaisService(mock_client)

    resultado = service.buscar_dados("brasil")

    assert resultado["capital"] == "Brasília"
    assert resultado["quantidade_idiomas"] == 1
    assert "Portuguese" in resultado["idiomas"]


def test_pais_nao_encontrado():

    mock_client = Mock()
    mock_client.buscar_pais.return_value = []

    service = PaisService(mock_client)

    with pytest.raises(ResourceNotFoundError):
        service.buscar_dados("paisfake")
