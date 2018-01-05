# -*- coding: utf-8 -*-
"""
runa.api
~~~~~~~~

RUNA API

"""
import logging
from urllib.error import URLError

from suds.client import Client
from suds.wsse import Security, UsernameToken, Timestamp

from .utils import (
    WS_CIUDADANO,
    WS_SRI,
    WS_ACCESS,
    AUTHORIZED_NUI,
    USER,
    PASSWORD,
    CODAGENCIA,
    CODINSTITUCION
)
from .models import PreparedRuna, PreparedContribuyente

logger = logging.getLogger('runa')


def login(WSDL):
    try:
        client = Client(WSDL)
    except URLError:
        logger.error("Error en WS")
        return False

    cl_auth = Client(WS_ACCESS)
    factory = cl_auth.factory.create("validarPermisoPeticion")
    factory.Cedula = AUTHORIZED_NUI
    factory.Urlsw = WSDL
    response = cl_auth.service.ValidarPermiso(factory)

    if response.TienePermiso == 'N':
        logger.error('%s %s' % (response.Mensaje.CodError, response.Mensaje.DesError))  # noqa
        return False, False
    return response, client


def _has_error(response):
    if not response.CodigoError == '000':
        return '{0} {1}'.format(response.CodigoError, response.Error)


def create_tokens(response):
    security = Security()
    token = UsernameToken(AUTHORIZED_NUI)
    token.setcreated(response.Fecha)
    token.nonce_has_encoding = True
    token.setnonce(response.Nonce)
    token.setpassworddigest(response.Digest)
    security.tokens.append(token)

    token_ts = Timestamp()
    token_ts.created = response.Fecha
    token_ts.expires = response.FechaF
    security.tokens.append(token_ts)
    return security


def read_by_nui(nui, mode='prod', authorized_nui=AUTHORIZED_NUI):
    response, client = login(WS_CIUDADANO)
    if not response:
        return False
    security = create_tokens(response)
    client.set_options(wsse=security)

    consulta_response = client.service.BusquedaPorNui(
        NUI=nui,
        Usuario=USER,
        Contrasenia=PASSWORD,
        CodigoInstitucion=CODINSTITUCION,
        CodigoAgencia=CODAGENCIA
    )
    error = _has_error(consulta_response)
    if error:
        raise Exception(error)
    runa = PreparedRuna()
    runa.prepare(consulta_response)
    return runa


def busqueda_por_nui(nui, mode='prod', authorized_nui=AUTHORIZED_NUI):
    return read_by_nui(nui, mode=mode, authorized_nui=authorized_nui)


def busqueda_ruc(ruc, AUTHORIZED_NUI=AUTHORIZED_NUI, bulk=False):
    response, cliente = login(WS_SRI)
    if not response:
        return False
    security = create_tokens(response)
    cliente.set_options(wsse=security)
    consulta_response = cliente.service.obtenerDatos(numeroRuc=ruc)
    if not consulta_response:
        return False
    contribuyente = PreparedContribuyente()
    contribuyente.prepare(consulta_response)
    return contribuyente
