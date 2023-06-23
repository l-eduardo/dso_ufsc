from datetime import date
from modelo.funcionario import Funcionario

class Emprestimo:
    def __init__(self, id: int, dispositivos: list, funcionario: Funcionario, data_inicio: date):
        self.__dispositivos = dispositivos
        self.__funcionario = funcionario
        self.__data_inicio = data_inicio
        self.__id = id
        self.__data_devolucao = None

    @property
    def dispositivos(self):
        return self.__dispositivos

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
        return self.__data_devolucao is not None:
    
    def finalizar(self):
        self.__data_devolucao = date.today()

    def __eq__(self, value: object):
        self.__id = value.id
