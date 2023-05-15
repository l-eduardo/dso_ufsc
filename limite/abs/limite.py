from abc import ABC, abstractmethod


class Limite(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def exibir(self):
        pass

    @abstractmethod
    def mostra_opcoes(self):
        pass