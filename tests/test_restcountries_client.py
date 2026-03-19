import pytest
from unittest.mock import patch, Mock
from clients.restcountries_client import RestCountriesClient
from exceptions import ExternalAPIError
from requests.exceptions import Timeout


def test_buscar_pais_sucesso():

    mock_response = Mock()
    mock_response.json.return_value = [{"name": "Brazil"}]
    mock_response.raise_for_status.return_value = None

    with patch("clients.restcountries_client.requests.get", return_value=mock_response):

        client = RestCountriesClient(
            base_url="https://restcountries.com/v3.1/name",
            timeout=5
        )

        resultado = client.buscar_pais("brasil")

    assert resultado == [{"name": "Brazil"}]


def test_timeout_api():

    with patch(
        "clients.restcountries_client.requests.get",
        side_effect=Timeout
    ):

        client = RestCountriesClient(
            base_url="https://restcountries.com/v3.1/name",
            timeout=5
        )

        with pytest.raises(ExternalAPIError):
            client.buscar_pais("brasil")
