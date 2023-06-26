from datetime import date
from modelo.funcionario import Funcionario
from modelo.abs.dispositivo import Dispositivo

import uuid

class Emprestimo:
    def __init__(self, dispositivo: Dispositivo, funcionario: Funcionario):
        self.__dispositivo = dispositivo
        self.__funcionario = funcionario
        self.__data_inicio = date.today()
        self.__data_devolucao = None
        self.__id = uuid.uuid4()

    @property
    def dispositivo(self):
        return self.__dispositivo

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio: date):
        self.__data_inicio = data_inicio

    @property
    def id(self):
        return self.__id

    @property
    def data_devolucao(self):
        return self.__data_devolucao

    def esta_finalizado(self):
        return self.__data_devolucao is not None

    def finalizar(self):
        self.__data_devolucao = date.today()

    def __eq__(self, value: object):
        self.__id = value.id
