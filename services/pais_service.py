from exceptions import ResourceNotFoundError
from clients.restcountries_client import RestCountriesClient


class PaisService:

    def __init__(self, client: RestCountriesClient):
        self.client = client

    def buscar_dados(self, pais: str) -> dict:

        data = self.client.buscar_pais(pais)

        if not data:
            raise ResourceNotFoundError("País não encontrado")

        pais_data = data[0]

        capital = pais_data.get("capital", [])
        lista_idiomas = list(pais_data.get("languages", {}).values())

        if not capital:
            raise ResourceNotFoundError("Capital não encontrada")

        if not lista_idiomas:
            raise ResourceNotFoundError("Idiomas não encontrados")

        return {
            "pais": pais,
            "capital": capital[0],
            "quantidade_idiomas": len(lista_idiomas),
            "idiomas": lista_idiomas
        }
