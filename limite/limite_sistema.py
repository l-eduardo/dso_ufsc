import time
import sys
import limite.textos.sistema as textos
import PySimpleGUI as sg


class LimiteSistema:
        def tela_opcoes(self):
            self.init_components()
            button, _ = self.__window.Read()
            return button

        def init_components(self):
            buttons = [[sg.Button('Dispositivos', key=1, pad=(0, (10, 5)))],
                       [sg.Button('Emprestimos', key=2, pad=(0, 5))],
                       [sg.Button('Funcionarios', key=3, pad=(0, 5))],
                       [sg.Button('Departamentos', key=4, pad=(0, 5))],
                       [sg.Button('Sair', key=0, pad=(0, (50, 10)))],
                       ]

            layout = [
                [sg.Text('Menu princpal', font=("Roboto",25), justification="center", tooltip="Menu principal")],
                [sg.Column(buttons, justification="center", element_justification="center")],
            ]
            self.__window = sg.Window('Sistema de emprestimos').Layout(layout)