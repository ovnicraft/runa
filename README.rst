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

* Uso del WS Consultar_Ciudadano
* Validación de NUI (usa librería stdum)
* Uso del WS SRI


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
