# coding=utf-8

import os

import requests
import vcr

AQUI = os.path.dirname(os.path.abspath(__file__))
vcr_cassettes_path = os.environ.get("vcr_cassettes_path", os.path.join(AQUI, "fixtures", "vcr_cassettes"))
# Os cassetes guardam o corpo gzip como foi recebido; com urllib3 2 o playback
# precisa descomprimir, senao o zeep recebe bytes gzip no lugar do WSDL.
gravador = vcr.VCR(decode_compressed_response=True)


@gravador.use_cassette(vcr_cassettes_path + "/test_http_itau/test_conexao_boleto_itau.yaml")
def test_conexao_boleto_itau():
    # ENDPOINT Válido
    endpoint = "https://oauth.itau.com.br/identity/connect/token"

    # Client fictício
    client_id = "B0RKj1UmUV-M0"

    # Secret Fictício
    client_secret = "8YrXLEMP0G_HIyM43RsOOez-stj50j3co_uUBq"

    params = dict(scope="readonly", grant_type="client_credentials", client_id=client_id, client_secret=client_secret)

    request = requests.post(
        url=endpoint,
        data=params,
    )
    assert request.status_code < 500
