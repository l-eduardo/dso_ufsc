from limite.abs.limite_psg import LimitePSG
import PySimpleGUI as sg


class LimiteEmprestimo(LimitePSG):
    def __init__ (self):
        super().__init__(cabecalho = ["ID",
                                      "Inicio",
                                      "Em andamento",
                                      "Funcionario",
                                      "CPF",
                                      "Patrimonio",
                                      "garantia"],
                        nome_objeto = "Emprestimo")

    def tela_cria_edita(self, funcionarios: list, dispositivos: list):
        layout = [[sg.Text("Dispositivo")],
                  [sg.Combo([f"{dispositivo.patrimonio} - {dispositivo.modelo}" for dispositivo in dispositivos], key="patrimonio", expand_x=True)],
                  [sg.Text("Funcionario")],
                  [sg.Combo([f"{funcionario.cpf} - {funcionario.nome}" for funcionario in funcionarios], key="cpf", expand_x=True)]]
        layout.append([sg.Button('Salvar'), sg.Button('Cancelar')])
        window = sg.Window(f'Emprestimo', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                break
            if event == 'Salvar':
                valores = {
                    "patrimonio": values["patrimonio"].split(" - ")[0],
                    "cpf": values["cpf"].split(" - ")[0]
                }
                window.close()
                return valores
        window.close()
