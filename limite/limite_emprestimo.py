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
        print(dispositivos)
        layout = [[sg.Text("Dispositivo")],
                  [sg.Combo(values=[f"{dispositivo.patrimonio} - {dispositivo.modelo}" 
                                    for dispositivo in dispositivos],
                            default_value=f"{dispositivos[0].patrimonio} - {dispositivos[0].modelo}",
                            key="patrimonio",
                            expand_x=True,
                            readonly=True)],
                  [sg.Text("Funcionario")],
                  [sg.Combo(values=[f"{funcionario.cpf} - {funcionario.nome}"
                                    for funcionario in funcionarios],
                            default_value=f"{funcionarios[0].cpf} - {funcionarios[0].nome}",
                             key="cpf",
                             expand_x=True,
                             readonly=True)]]
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
