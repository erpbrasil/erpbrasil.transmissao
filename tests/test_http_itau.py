# coding=utf-8

import requests


def test_conexao_boleto_itau():
    # ENDPOINT Válido
    endpoint = 'https://oauth.itau.com.br/identity/connect/token'

    # Client fictício
    client_id = u'B0RKj1UmUV-M0'

    # Secret Fictício
    client_secret = u'8YrXLEMP0G_HIyM43RsOOez-stj50j3co_uUBq'

    params = dict(
        scope='readonly',
        grant_type='client_credentials',
        client_id=client_id,
        client_secret=client_secret
    )

    request = requests.post(
        url=endpoint,
        data=params,
    )
    assert request.status_code < 500


test_conexao_boleto_itau()
