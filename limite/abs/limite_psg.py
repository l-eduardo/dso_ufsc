from abc import ABC, abstractmethod
from exceptions.selecao_nula import SelecaoNulaException
import PySimpleGUI as sg


class LimitePSG(ABC):
    @abstractmethod
    def __init__(self, cabecalho: list, nome_objeto: str):
        self.__cabecalho = cabecalho
        self.__nome_objeto = nome_objeto

    def tela_cria_edita(self, dicionario_atributo_valor: dict, edit_mode: bool = False):
        layout = []
        for item in dicionario_atributo_valor:
          layout.append([[sg.Text(f'{item}')],
                         [sg.Input(key=f'-{item}-', 
                                   default_text=dicionario_atributo_valor[item],
                                   disabled_readonly_background_color="#4682b4")]])
        layout.append([sg.Button('Salvar'), sg.Button('Cancelar')])
        if edit_mode:
            layout[0][1][0].__setattr__("ReadOnly", True)
            layout[0][1][0].__setattr__("disabled_readonly_text_color", "#303030")
        window = sg.Window(f'Dados {self.__nome_objeto}', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                break
            if event == 'Salvar':
                valores = {}
                for item in dicionario_atributo_valor:
                    valores[item] = values[f'-{item}-']
                window.close()
                return valores
        window.close()

    def tela_lista_seleciona(self, lista_valores: list, headers: list = [], edit_mode: bool = False):
        registros = lista_valores
        tabela = sg.Table(registros, headings=headers or self.__cabecalho,
                          auto_size_columns=True,
                          display_row_numbers=False,
                          justification='center', key='-TABELA-',
                          selected_row_colors='#191970 on #add8e6',
                          enable_events=True,
                          expand_x=True,
                          expand_y=True,
                          enable_click_events=False,
                          select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                          vertical_scroll_only = False)
        layout = [[tabela],
                  [sg.Button("Cancelar")]]
        if edit_mode:
            layout[-1].insert(0, sg.Button("Selecionar"))
        window = sg.Window(f"Lista {self.__nome_objeto}", layout, size=(900, 300), resizable=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Cancelar":
                break
            if event == "Selecionar":
                if values["-TABELA-"]:
                    window.close()
                    return lista_valores[values["-TABELA-"][0]]
                else:
                    window.close()
                    raise SelecaoNulaException()
        window.close()

    def tela_menu(self, lista_botoes: list):
        buttons = []
        for text in lista_botoes:
            buttons.append([sg.Button(button_text = text,
                                     key = f'{text}',
                                     pad=(0, (10, 5)),
                                     expand_x=True)]
                                     )
        buttons.append([sg.Button(button_text = "    Cancelar    ",
                                     key = 'Cancelar',
                                     pad=(0, (50, 10)),
                                     expand_x=True)])
        layout = [[sg.Text(f'Menu {self.__nome_objeto}',
                 font=("Roboto",25),
                 justification="center",
                 tooltip="Menu principal")],
                 [sg.Column(buttons,
                            justification="center",
                            element_justification="center")]]
        window = sg.Window(f"Menu {self.__nome_objeto}", layout, resizable=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Cancelar":
                break
            else:
                window.close()
                return event
        window.close()

    def popup(self, texto: str):
        sg.popup(texto,title="Erro")
