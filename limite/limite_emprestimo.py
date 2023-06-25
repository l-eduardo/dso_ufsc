from limite.abs.limite_psg import LimitePSG


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
