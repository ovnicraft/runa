# -*- coding: utf-8 -*-

import os
import json

CONFIG_FILE = '/var/tmp/config.json'

# Read config
with open(CONFIG_FILE) as env_file:
    VARS_ENV = json.load(env_file)

AUTHORIZED_NUI = os.environ.get('AUTHORIZED_NUI', None)
WS_CIUDADANO_PRODUCTION = VARS_ENV.get('WS_CIUDADANO_PRODUCTION', None)
WS_CIUDADANO_TESTING = VARS_ENV.get('WS_CIUDADANO_TESTING', None)
WS_ACCESS = VARS_ENV.get('WS_ACCESS', None)
WS_CIUDADANO = None


def set_ws(mode='prod'):
    WS_CIUDADANO = mode == 'prod' and WS_CIUDADANO_PRODUCTION or WS_CIUDADANO_TESTING  # noqa
