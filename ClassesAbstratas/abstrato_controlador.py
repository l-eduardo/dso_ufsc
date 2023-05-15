from abc import ABC
from abc import abstractmethod

class AbstratoControlador(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inclui(self):
        pass

    @abstractmethod
    def altera(self):
        pass

    @abstractmethod
    def deleta(self):
        pass

    @abstractmethod
    def lista(self):
        pass

    @abstractmethod
    def filtra_por_propriedade(self):
        pass

    @abstractmethod
    def retorna(self):
        pass

    @abstractmethod
    def abre_tela(self):
        pass