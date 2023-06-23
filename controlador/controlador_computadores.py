from controlador.abs.crud_abs import Crud
from modelo.computador import Computador
from limite.limite_computador import LimiteComputador


class ControladorComputadores(Crud):
    def __init__(self, controlador_sistema):
        super().__init__(T=Computador, nome_cp="patrimonio")
        self.__limiteComputador = LimiteComputador()
        self.__controlador_sistema = controlador_sistema

    def lista(self):
        self.__limiteComputador.exibe_computadores(super().lista)

    def inclui(self):
        dados_computador = self.__limiteComputador.pega_dados()
        try:
            dados_computador['memoria_ram'] =  int(dados_computador['memoria_ram'])
            dados_computador['armazenamento'] =  float(dados_computador['armazenamento'])
            
            computador = Computador(*dados_computador.values())
        except Exception as e:
            print("Erro: " + e)
            self.abre_tela()
            
        return super().inclui(computador)
    
    def altera(self):
        try:
            patrimonio = self.__limiteComputador.pega_patrimonio()
            propriedade = self.__limiteComputador.pega_propriedade()
            novo_valor = self.__limiteComputador.novo_valor()

            super().altera(
                chave_primaria=patrimonio,
                propriedade=propriedade,
                novo_valor=novo_valor
                )
        except Exception as e:
            print("Erro: " + repr(e))
            self.abre_tela()
        
    def deleta(self):
        try:
            patrimonio = self.__limiteComputador.pega_patrimonio()
            super().deleta(patrimonio)
        except Exception as e:
            print("Erro: " + e)
            self.abre_tela()

    def busca(self):
        propriedade = self.__limiteComputador.pega_patrimonio()

        resultado = super().busca(propriedade)

        self.__limiteComputador.exibe_computador(resultado)
        
    def abre_tela(self):
        lista_opt = {
            0: self.retorna,
            1: self.inclui,
            2: self.altera,
            3: self.deleta,
            4: self.busca,
            5: self.lista
        }

        while True:
            lista_opt[self.__limiteComputador.tela_opcoes()]()

    def retorna(self):
        self.__controlador_sistema.abre_tela()
