import requests
from exceptions import ExternalAPIError


class RestCountriesClient:

    def __init__(self, base_url: str, timeout: int):
        self.base_url = base_url
        self.timeout = timeout

    def buscar_pais(self, pais: str):

        try:
            response = requests.get(
                f"{self.base_url}/{pais}",
                timeout=self.timeout
            )

            response.raise_for_status()

        except requests.exceptions.Timeout:
            raise ExternalAPIError("Timeout na API externa")

        except requests.exceptions.RequestException:
            raise ExternalAPIError("Erro ao acessar API externa")

        return response.json()
