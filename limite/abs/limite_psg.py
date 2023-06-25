from abc import ABC, abstractmethod
import PySimpleGUI as sg


class LimitePSG(ABC):
    @abstractmethod
    def __init__(self, cabecalho: list, nome_objeto: str):
        self.__cabecalho = cabecalho
        self.__nome_objeto = nome_objeto

# Apresenta janela com campos de input para a criacao de um objeto
    # ARG: nome_objeto - string com o nome do Objeto a ser criado
    # ARG: dicionario_atributo_valor - dicionario com atributo
    # RETURN: Dicionario com valores "nome_atributo":"valor lido do input" 
    def tela_cria_edita(self, dicionario_atributo_valor: dict):
        layout = []
        for item in dicionario_atributo_valor:
          layout.append([[sg.Text(f'{item}')],
                         [sg.Input(key=f'-{item}-', 
                                   default_text=dicionario_atributo_valor[item])]])
        layout.append([sg.Button('Salvar'), sg.Button('Cancelar')])

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

    # Apresenta janela com uma tabela de valores dos objetos
    # ARG: self.__cabecalho - Lista dos textos para o self.__cabecalho da tabela
    # ARG: lista_valores - Matriz com as listas dos valores dos atributos dos objetos (linhas da tabela)
    # ARG: edit_mode - Bool para informar se deve haver botao de selecionar objeto e retorno de ID
    # RETURN: se edit_mode True, retorna o ID informado na linha selecionada
    def tela_lista_seleciona(self, lista_valores: list, edit_mode: bool = False):
        registros = lista_valores
        tabela = sg.Table(registros, self.__cabecalho,
                          auto_size_columns=True,
                          display_row_numbers=False,
                          justification='center', key='-TABELA-',
                          selected_row_colors='red on yellow',
                          enable_events=True,
                          expand_x=True,
                          expand_y=True,
                          enable_click_events=False,
                          select_mode=sg.TABLE_SELECT_MODE_BROWSE)
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
                window.close()
                return lista_valores[values["-TABELA-"][0]]
        window.close()

    def tela_menu(self, lista_botoes: list):
        layout = []
        for text in lista_botoes:
            layout.append([sg.Button(button_text = text,
                                     key = f'{text}',
                                     pad=(0, (10, 5)),
                                     expand_x=True)])
        layout.append([sg.Button(button_text = "Cancelar",
                                     key = 'Cancelar',
                                     pad=(0, (10, 5)),
                                     expand_x=True)])

        window = sg.Window(f"Menu {self.__nome_objeto}", layout, resizable=True)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Cancelar":
                break
            else:
                window.close()
                return event
        window.close()
