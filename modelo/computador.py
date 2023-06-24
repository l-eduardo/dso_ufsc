import datetime
from modelo.abs.dispositivo import Dispositivo
from validacao.validador_dispositivos import ValidadorDispositivo


class Computador(Dispositivo, ValidadorDispositivo):
    def __init__(self,
                 patrimonio: str,
                 marca: str,
                 modelo: str,
                 tipo: str,
                 serial_number: str,
                 processador: str,
                 memoria_ram: int,
                 armazenamento: float,
                 so: str,
                 fim_garantia: str
                 ):
        super().__init__(patrimonio, marca, modelo, tipo, serial_number)
        self.__processador = processador
        self.__memoria_ram = memoria_ram
        self.__armazenamento = armazenamento
        self.__so = so
        self.__fim_garantia = fim_garantia
    
    def __eq__(self, __value: object):
        if isinstance(__value, Computador):
            return super().patrimonio == __value.patrimonio
        return False

    @property
    def processador(self):
        return self.__processador

    @processador.setter
    def processador(self, novo_processador):
        self.__processador = novo_processador

    @property
    def memoria_ram(self):
        return self.__memoria_ram

    @memoria_ram.setter
    def memoria_ram(self, nova_memoria_ram):
        self.__memoria_ram = nova_memoria_ram

    @property
    def armazenamento(self):
        return self.__armazenamento
    
    @armazenamento.setter
    def armazenamento(self, novo_armazenamento):
        self.__armazenamento = novo_armazenamento

    @property
    def so(self):
        return self.__so

    @so.setter
    def so(self, novo_so):
        self.__so = novo_so

    @property
    def fim_garantia(self):
        return self.__fim_garantia

    @fim_garantia.setter
    def fim_garantia(self, nova_fim_garantia):
        self.__fim_garantia = nova_fim_garantia

    def esta_na_garantia(self):
        hoje = datetime.datetime.today()
        garantia = datetime.datetime.strptime(self.__fim_garantia, '%d/%m/%Y')

        return hoje <= garantia
