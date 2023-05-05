from abc import ABC, abstractmethod


class Dispositivo(ABC):
    @abstractmethod
    def __init__(self, patrimonio: str, marca: str, modelo: str, tipo: str, serial_number: str):
        if(isinstance(patrimonio, str)):
            self.__patrimonio = patrimonio
        if(isinstance(marca, str)):
            self.__marca = marca
        if(isinstance(modelo, str)):
            self.__modelo = modelo
        if(isinstance(tipo, str)):
            self.__tipo = tipo
        if(isinstance(serial_number, str)):
            self.__serial_number = serial_number

    @property
    @abstractmethod
    def patrimonio(self):
        return self.__patrimonio

    @property
    @abstractmethod
    def marca(self):
        return self.__marca

    @property
    @abstractmethod
    def modelo(self):
        return self.__modelo

    @property
    @abstractmethod
    def tipo(self):
        return self.__tipo

    @property
    @abstractmethod
    def serial_number(self):
        return self.__serial_number

    @patrimonio.setter
    @abstractmethod
    def patrimonio(self, patrimonio: str):
        if(isinstance(patrimonio, str)):
            self.__patrimonio = patrimonio

    @marca.setter
    @abstractmethod
    def marca(self, marca: str):
        if(isinstance(marca, str)):
            self.__marca = marca

    @modelo.setter
    @abstractmethod
    def modelo(self, modelo: str):
        if(isinstance(modelo, str)):
            self.__modelo = modelo

    @tipo.setter
    @abstractmethod
    def tipo(self, tipo: str):
        if(isinstance(tipo, str)):
            self.__tipo = tipo

    @serial_number.setter
    @abstractmethod
    def serial_number(self, serial_number: str):
        if(isinstance(serial_number, str)):
            self.__serial_number = serial_number