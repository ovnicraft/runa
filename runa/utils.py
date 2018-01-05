# -*- coding: utf-8 -*-

import json
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

CONFIG_FILE_NAME = '.runa.json'

CONFIG_FILE = '{0}/{1}'.format(str(Path.home()), CONFIG_FILE_NAME)

if not Path(CONFIG_FILE).is_file():
    mf = open(CONFIG_FILE, 'w')
    json.dumps({}, mf)
    mf.close()


# Read config
with open(CONFIG_FILE) as env_file:
    VARS_ENV = json.load(env_file)
    if not VARS_ENV:
        logger.warning('No vars defined, please update your %s' % CONFIG_FILE)

AUTHORIZED_NUI = VARS_ENV.get('AUTHORIZED_NUI', None)
WS_CIUDADANO_PRODUCTION = VARS_ENV.get('WS_CIUDADANO_PRODUCTION', None)
WS_SRI = VARS_ENV.get('WS_SRI', None)
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
