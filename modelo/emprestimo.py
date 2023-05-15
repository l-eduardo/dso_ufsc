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

    @dispositivos.setter
    def dispositivos(self, dispositivos: list):
        self.__dispositivos = dispositivos

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario: Funcionario):
        self.__funcionario = funcionario

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio: date):
        self.__data_inicio = data_inicio

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def data_devolucao(self):
        return self.__data_devolucao

    @data_devolucao.setter
    def data_devolucao(self, data_devolucao: date):
        self.__data_devolucao = data_devolucao
