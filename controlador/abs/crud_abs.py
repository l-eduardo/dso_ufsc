from abc import ABC, abstractmethod
from DAO.dao import DAO


class Crud(ABC):
    @abstractmethod
    def __init__(self, T, nome_cp):
        self.__dao = DAO(T.__name__)
        self.__t = T
        self.__nome_cp = nome_cp
    @property
    def lista(self):
        return self.__dao.get_all()

    def inclui(self, item):
        if(not isinstance(item, self.__t)):
            raise TypeError(f"Tipo invalido! {item} nao faz parte de {self.__t}")

        self.__dao.add(getattr(item, self.__nome_cp), item)

    def busca(self, chave_primaria):
        return self.__dao.get(chave_primaria)

    def altera(self, chave_primaria, propriedade, novo_valor):
        valor_a_alterar = self.__dao.get(chave_primaria)

        valor_a_alterar.__setattr__(propriedade, novo_valor)

        self.__dao.update(chave_primaria, valor_a_alterar)

    def deleta(self, chave_primaria):
        self.__dao.remove(chave_primaria)

    @abstractmethod
    def retorna(self):
        pass

    @abstractmethod
    def abre_tela(self):
        pass