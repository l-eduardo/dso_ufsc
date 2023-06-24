import os
import PySimpleGUI as sg

from limite.abs.limite import Limite
from limite.components.buttons_menu import Menus
import limite.textos.computador as textos

class LimiteComputador:
    def tela_opcoes(self):
        self.setup_componentes()
        button, _ = self.__window.Read()
        return button

    def setup_componentes(self):
        buttons_text = [
            'inclui',
            'altera',
            'deleta',
            'busca',
            'lista',
            'retorna',
        ]

        buttons = Menus.buttons_menu_setup(buttons_text)

        layout = [
            [sg.Text('Menu Computadores',
                        font=("Roboto",25),
                        justification="center",
                        tooltip="Menu Computadores")],
            [sg.Column(buttons,
                        justification="center",
                        element_justification="center")],
        ]

        self.__window = sg.Window('Sistema de emprestimos').Layout(layout)

    def pega_dados(self):
        entradas = {}
        print("-------- COMPUTADOR ----------")
        for i in textos.dados_computador.keys():
            entradas[i] = input(textos.dados_computador[i])
        print()

        return entradas

    def exibe_computador(self, computador):
        for i in textos.dados_computador.keys():
            print(f"{textos.dados_computador[i]} {getattr(computador, i)}")

    def exibe_computadores(self, computadores):
        os.system('clear')
        for i in computadores:
            self.exibe_computador(computadores[i])

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

    def valida_entrada(self, opt):
        try:
            opt = int(opt)
            if opt < 0 or opt > 4:
                raise ValueError("Opcao invalida")
            return opt
        except Exception as e:
            print(e)
            self.tela_opcoes()
