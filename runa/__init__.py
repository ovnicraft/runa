# -*- coding: utf-8 -*-

"""Top-level package for Librería para WS del Estado."""

__author__ = """Cristian Salamea"""
__email__ = 'cristian.salamea@gmail.com'
__version__ = '0.1.0'

#  _____  _    _ _   _
# |  __ \| |  | | \ | |   /\
# | |__) | |  | |  \| |  /  \
# |  _  /| |  | | . ` | / /\ \
# | | \ \| |__| | |\  |/ ____ \
# |_|  \_\\____/|_| \_/_/    \_\
#


"""
Runa Library
~~~~~~~~~~~~

Runa es una libreria para consumir los servicios web
del bus gubernamental de Ecuador de una manera *Pythonica*

   >>> import runa
   >>> r = runa.read_by_nui('0102030405')
   >>> r.Nombre
   PUJON JUAN
   >>> print(r)
   <Runa [0102030405 PUJON JUAN]>

"""

from .api import read_by_nui, busqueda_por_nui  # noqa
