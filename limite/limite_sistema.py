import time
import sys
import limite.textos.sistema as textos
import PySimpleGUI as sg


class LimiteSistema:
        def tela_opcoes(self):
            self.init_components()
            button, _ = self.__window.Read()
            self.__window.close()
            return button

        def init_components(self):
            buttons = [[sg.Button('Dispositivos', key=1, pad=(0, (10, 5)), expand_x=True)],
                       [sg.Button('Emprestimos', key=2, pad=(0, 5), expand_x=True)],
                       [sg.Button('Funcionarios', key=3, pad=(0, 5), expand_x=True)],
                       [sg.Button('Departamentos', key=4, pad=(0, 5), expand_x=True)],
                       [sg.Button('Sair', key=0, pad=(0, (50, 10)), expand_x=True)],
                       ]

            layout = [
                [sg.Text('Menu principal',
                         font=("Roboto",25),
                         justification="center",
                         tooltip="Menu principal")],
                [sg.Column(buttons,
                         justification="center",
                         element_justification="center")],
            ]
            self.__window = sg.Window('Sistema de emprestimos').Layout(layout)
