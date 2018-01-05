==================================================
Librería para Uso de los WS del Estado Ecuatoriano
==================================================


.. image:: https://img.shields.io/pypi/v/runa.svg
        :target: https://pypi.python.org/pypi/runa

.. image:: https://img.shields.io/travis/ovnicraft/runa.svg
        :target: https://travis-ci.org/ovnicraft/runa

.. image:: https://readthedocs.org/projects/runa/badge/?version=latest
        :target: https://runa.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/ovnicraft/runa/shield.svg
     :target: https://pyup.io/repos/github/ovnicraft/runa/
     :alt: Updates


Librería para uso WS del Bus Gubernamental de Ecuador


* Free software: MIT license
* Documentation: https://runa.readthedocs.io


Installing
----------

.. code-block:: bash

    $ pip install runa


Using
-----

This library will create a configuration file .runa.json in your HOMEPATH, update this to use it.

.. code-block:: python

    >>> import runa
    >>> pr = runa.busqueda_por_nui('0102030405')
    >>> print(pr)
    <Runa [0102030405 - PUJON JUAN MANUEL]>

    >>> pr.json()
    ...
    >>> contribuyente = runa.busqueda_ruc('0102030405001')
    >>> print(contribuyente)
    <Contribuyente [0102030405001 - MI COMPANIA CIA.LTDA.]>

Features
--------

* WS Consultar_Ciudadano
* WS SRI
* Config file needed

Credits
---------

Created by Cristian Salamea
