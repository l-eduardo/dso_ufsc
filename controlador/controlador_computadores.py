from abs.crud import Crud
from modelo.computador import Computador
from limite.limite_computador import LimiteComputador


class ControladorComputadores(Crud):
    def __init__(self):
        super().__init__(T=Computador, nome_cp="patrimonio")
        self.__limiteComputador = LimiteComputador() 
    
    def lista(self):
        self.__limiteComputador.exibe_computadores(super().lista)

    def inclui(self):
        computador = Computador(*self.__limiteComputador.pega_dados())
        return super().inclui(computador)
    
    def altera(self):
        patrimonio = self.__limiteComputador.pega_patrimonio()
        propriedade = self.__limiteComputador.pega_propriedade()
        novo_valor = self.__limiteComputador.novo_valor()

        super().altera(
            chave_primaria=patrimonio,
            propriedade=propriedade,
            novo_valor=novo_valor
            )
        
    def deleta(self):
        patrimonio = self.__limiteComputador.pega_patrimonio()
        super().deleta(patrimonio)

    def filtra(self):
        propriedade = self.__limiteComputador.pega_propriedade()
        valor = self.__limiteComputador.novo_valor()

        resultado = super().filtra_por_propriedade(propriedade, valor)

        self.__limiteComputador.exibe_computadores(resultado)
        
    def abre_tela(self):
        lista_opt = {
            0: self.retorna,
            1: self.inclui,
            2: self.altera,
            3: self.deleta,
            4: self.filtra_por_propriedade,
            5: self.lista
        }

        while True:
            lista_opt[self.__limiteComputador.tela_opcoes()]()

    def retorna(self):
        pass

c = ControladorComputadores()

c.abre_tela()