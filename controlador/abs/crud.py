from abc import ABC, abstractmethod, abstractproperty


class Crud(ABC):
    @abstractmethod
    def __init__(self, T, nome_cp):
        self.__lista = []
        self.__t = T
        self.__nome_cp = nome_cp

    @property
    def lista(self):
        return self.__lista

    def inclui(self, item):
        if(item in self.__lista):
            raise ValueError(f"{item} ja esta cadastrado!")

        if(not isinstance(item, self.__t)):
            raise TypeError(f"Tipo invalido! {item} nao faz parte de {self.__t}")

        self.__lista.append(item)

    def filtra_por_propriedade(self, propriedade, valor):
        listra_filtrada = list(filter(lambda item:
                                    item.__dict__[propriedade] == valor,
                                    self.__lista))
        return listra_filtrada

    def altera(self, chave_primaria, propriedade, novo_valor):
        valores_a_alterar = self.filtra_por_propriedade(self.__nome_cp, chave_primaria)

        if len(valores_a_alterar) == 0:
            raise ValueError(f"{chave_primaria} nao esta cadastrado!")
        if len(valores_a_alterar) > 1:
            raise ValueError(f"{chave_primaria} esta cadastrado mais de uma vez!")

        for item in valores_a_alterar:
            item.__dict__[propriedade] = novo_valor

    def deleta(self, chave_primaria):
        valores_a_deletar = self.filtra_por_propriedade(self.__nome_cp, chave_primaria)

        if len(valores_a_deletar) == 0:
            raise ValueError(f"{chave_primaria} nao esta cadastrado!")
        if len(valores_a_deletar) > 1:
            raise ValueError(f"{chave_primaria} esta cadastrado mais de uma vez!")

        for item in valores_a_deletar:
            self.__lista.remove(item)

    @abstractmethod
    def retorna():
        pass

    @abstractmethod
    def abre_tela():
        pass
