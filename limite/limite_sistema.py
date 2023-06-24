import time
import sys
import limite.textos.sistema as textos
import PySimpleGUI as sg
from limite.components.buttons_menu import Menus

class LimiteSistema:
        def tela_opcoes(self):
            self.setup_componentes()
            button, _ = self.__window.Read()
            return button

        def setup_componentes(self):
            buttons_text = ['Dispositivos',
                            'Emprestimos',
                            'Funcionarios',
                            'Departamentos',
                            'Sair']

            buttons = Menus.buttons_menu_setup(buttons_text)
            
            layout = [
                [sg.Text('Menu princpal',
                         font=("Roboto",25),
                         justification="center",
                         tooltip="Menu principal")],
                [sg.Column(buttons,
                         justification="center",
                         element_justification="center")],
            ]
            self.__window = sg.Window('Sistema de emprestimos').Layout(layout)