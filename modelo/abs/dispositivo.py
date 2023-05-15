from abc import ABC, abstractmethod
from typing import Any, cast, get_type_hints


class Dispositivo(ABC):
    @abstractmethod
    def __init__(self, patrimonio: str, marca: str, modelo: str, tipo: str, serial_number: str):
        self.__patrimonio = patrimonio
        self.__marca = marca
        self.__modelo = modelo
        self.__tipo = tipo
        self.__serial_number = serial_number

    @property
    def patrimonio(self):
        return self.__patrimonio

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def tipo(self):
        return self.__tipo

    @property
    def serial_number(self):
        return self.__serial_number

    @patrimonio.setter
    def patrimonio(self, patrimonio: str):
        if(isinstance(patrimonio, str)):
            self.__patrimonio = patrimonio

    @marca.setter
    def marca(self, marca: str):
        if(isinstance(marca, str)):
            self.__marca = marca

    @modelo.setter
    def modelo(self, modelo: str):
        if(isinstance(modelo, str)):
            self.__modelo = modelo

    @tipo.setter
    def tipo(self, tipo: str):
        if(isinstance(tipo, str)):
            self.__tipo = tipo

    @serial_number.setter
    def serial_number(self, serial_number: str):
        if(isinstance(serial_number, str)):
            self.__serial_number = serial_number
