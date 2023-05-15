from limite.abs.limite import Limite
import limite.textos.computador as textos
import os

class LimiteComputador:
    def tela_opcoes(self):
        print(textos.opt)

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados(self):
        entradas = {}
        print("-------- COMPUTADOR ----------")
        for i in textos.dados_computador.keys():
            entradas[i] = input(textos.dados_computador[i])
        print()

        return entradas.values()

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def exibe_computador(self, computador):
        for i in textos.dados_computador.keys():
            print(f"{textos.dados_computador[i]} {getattr(computador, i)}")

    def exibe_computadores(self, computadores):
        os.system('clear')
        for computador in computadores:
            self.exibe_computador(computador)

  #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_patrimonio(self):
        print("-------- COMPUTADOR ----------")
        patrimonio = input(textos.selecionar_computador)

        return patrimonio

    def pega_propriedade(self):
        print("-------- COMPUTADOR ----------")
        for i, v in enumerate(textos.propriedades_computador):
            print(f"{i} - {v}")
        prop_index = input(textos.propriedade_input)

        return textos.propriedades_computador[int(prop_index)]
    
    def novo_valor(self):
        print("-------- COMPUTADOR ----------")
        valor = input(textos.novo_valor)

        return valor

    def mostra_mensagem(self, msg):
        print(msg)
