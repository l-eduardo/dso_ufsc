from modelo.abs.dispositivo import Dispositivo


class DispositivoRede(Dispositivo):
    def __init__(self,
                 patrimonio: str,
                 marca: str,
                 modelo: str,
                 tipo: str,
                 serial_number: str,
                 especifacao: str,
                 portas: list[tuple(str, str)],
                 numero_portas: int,
                 ):
        super().__init__(patrimonio, marca, modelo, tipo, serial_number)
        self.__especifacao = especifacao
        self.__portas = portas
        self.__numero_portas = numero_portas

    @property
    def especifacao(self):
        return self.__especifacao

    @especifacao.setter
    def especifacao(self, especifacao):
        self.__especifacao = especifacao

    @property
    def portas(self):
        return self.__portas
    
    @property
    def numero_portas(self):
        return self.__numero_portas
