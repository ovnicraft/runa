# -*- coding: utf-8 -*-
"""
runa.models
~~~~~~~~~~~

RUNA Models

"""
import json


class PreparedRuna(object):

    def __init__(self):
        self.Calle = None
        self.CodigoTipoCedulado = None
        self.CondicionCedulado = None
        self.Conyuge = None
        self.Domicilio = None
        self.EstadoCivil = None
        self.FechaCedulacion = None
        self.FechaMatrimonio = None
        self.FechaNacimiento = None
        self.IndividualDactilar = None
        self.Instruccion = None
        self.LugarMatrimonio = None
        self.LugarNacimiento = None
        self.NUI = None
        self.Nacionalidad = None
        self.Nombre = None
        self.NombreMadre = None
        self.NombrePadre = None
        self.NumeroCasa = None
        self.Profesion = None
        self.Sexo = None
        self.Genero = None
        self.FechaInscripcionGenero = None
        self.ValidNUI = True

    def __repr__(self):
        return '<Runa [%s - %s]>' % (self.NUI, self.Nombre)

    def json(self):
        return json.dumps(self.__dict__)

    def nui_is_valid(self):
        """ Validate NUI """
        pass

    def prepare(self, response):
        """ Prepare given response data in object"""
        self.Calle = response.Calle
        self.NUI = response.NUI
        self.Nombre = response.Nombre
