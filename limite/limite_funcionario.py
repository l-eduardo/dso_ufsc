from limite.abs.limite_psg import LimitePSG


class LimiteFuncionario(LimitePSG):
    def __init__ (self):
        super().__init__(cabecalho = ["CPF",
                                      "Nome",
                                      "E-mail",
                                      "Telefone",
                                      "Cargo",
                                      "Endereço"],
                        nome_objeto = "Funcionário")
        self.__botoes_menu = ["Criar", "Editar", "Listar", "Remover"]

    def tela_menu(self):
        return super().tela_menu(self.__botoes_menu)
