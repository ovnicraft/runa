# -*- coding: utf-8 -*-
"""
runa.api
~~~~~~~~

RUNA API

"""
import logging
from urllib.error import URLError

# from suds.client import Client
from zeep import Client
from suds.wsse import Security, UsernameToken, Timestamp

from .utils import WS_CIUDADANO, WS_ACCESS, AUTHORIZED_NUI
from .models import PreparedRuna

logger = logging.getLogger('suds')


def login(WSDL):
    try:
        client = Client(WSDL)
    except URLError:
        logger.error("Error en WS")
        return False, False

    cl_auth = Client(WS_ACCESS)
    logger.info("***********\n Leyendo types en servicios...")
    req_auth = cl_auth.factory.create("validarPermisoPeticion")
    logger.info("***********\n Autentificacion...")
    req_auth.Cedula = AUTHORIZED_NUI
    req_auth.Urlsw = WS_CIUDADANO
    logger.info("***********\nResultado de auth...")

    response = cl_auth.service.ValidarPermiso(req_auth)

    if response.TienePermiso == 'N':
        logger.error("No tiene permisos, respuesta de WS: %s" % response.TienePermiso)
        return False
    return response, client


def read_by_nui(nui, mode='prod', authorized_nui=None):
    response, client = login(WS_CIUDADANO)
    if not response:
        return False
    logger.info("Digest: %s" % response.Digest)
    logger.info("Fecha: %s" % response.Fecha)
    logger.info("FechaF: %s " % response.FechaF)
    logger.info("Nonce: %s " % response.Nonce)
    logger.info("TienePermiso: %s " % response.TienePermiso)
    security = Security()
    token = UsernameToken(authorized_nui)
    token.setcreated(response.Fecha)
    token.nonce_has_encoding = True
    token.setnonce(response.Nonce)
    token.setpassworddigest(response.Digest)
    security.tokens.append(token)
    token_ts = Timestamp()
    token_ts.created = response.Fecha
    token_ts.expires = response.FechaF
    security.tokens.append(token_ts)
    client.set_options(wsse=security)
    consulta_response = False
    try:
        consulta_response = client.service.BusquedadPorNui(NUI=nui, Usuario="testroot", Contrasenia="Sti1DigS21")
    except WebFault:
        logger.info("error en la consulta")
    runa = PreparedRuna()
    runa.prepare(consulta_response)
    return runa
