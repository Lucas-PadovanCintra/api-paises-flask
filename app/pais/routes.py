import logging
from flask import Blueprint, current_app
from services.pais_service import PaisService
from clients.restcountries_client import RestCountriesClient

logger = logging.getLogger(__name__)

pais_bp = Blueprint(
    "pais",
    __name__,
    url_prefix="/api/v1/pais"
)


def init_service():

    client = RestCountriesClient(
        base_url=current_app.config["RESTCOUNTRIES_URL"],
        timeout=current_app.config["API_TIMEOUT"]
    )

    return PaisService(client)


@pais_bp.route("/dados/<pais>")
def dados_pais(pais):

    logger.info(
        "Requisição recebida",
        extra={
            "event": "pais_request_started",
            "pais": pais
        }
    )

    service = init_service()

    dados = service.buscar_dados(pais)

    logger.info(
        "Dados encontrados",
        extra={
            "event": "pais_request_finished",
            "pais": pais
        }
    )

    return dados, 200
