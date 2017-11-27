# -*- coding: utf-8 -*-

import json

CONFIG_FILE = '/var/tmp/config.json'

# Read config
with open(CONFIG_FILE) as env_file:
    VARS_ENV = json.load(env_file)

AUTHORIZED_NUI = VARS_ENV.get('AUTHORIZED_NUI', None)
WS_CIUDADANO_PRODUCTION = VARS_ENV.get('WS_CIUDADANO_PRODUCTION', None)
WS_CIUDADANO_TESTING = VARS_ENV.get('WS_CIUDADANO_TESTING', None)
WS_ACCESS = VARS_ENV.get('WS_ACCESS', None)
WS_CIUDADANO = WS_CIUDADANO_PRODUCTION
USER = VARS_ENV.get('USER', None)
PASSWORD = VARS_ENV.get('PASSWORD', None)
CODINSTITUCION = VARS_ENV.get('CODINSTITUCION', None)
CODAGENCIA = VARS_ENV.get('CODAGENCIA', None)
MODE = VARS_ENV.get('mode', 'prod')


def set_ws(mode='prod'):
    WS_CIUDADANO = mode == 'prod' and WS_CIUDADANO_PRODUCTION or WS_CIUDADANO_TESTING  # noqa
