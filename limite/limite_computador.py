from limite.abs.limite_psg import LimitePSG


class LimiteComputador(LimitePSG):
    def __init__ (self):
        super().__init__(cabecalho = ["Patrimonio",
                                      "Marca",
                                      "Modelo",
                                      "Tipo",
                                      "Serial Number",
                                      "Processador",
                                      "Memoria RAM",
                                      "Armazenamento",
                                      "Sist. Operacional",
                                      "Prazo Garantia"],
                        nome_objeto = "Computador")
