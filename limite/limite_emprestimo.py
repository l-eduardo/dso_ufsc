

class LimiteEmprestimo:
    def __init__(self):
        pass

    def recebe_dado(self, mensagem: str):
        dado = input(f"\n('sair' p/ sair)\nDigite {mensagem}: ")
        if dado == "sair":
            raise ValueError("\n>>> Operacao cancelada pelo usuario! <<<\n")
        else:
            return dado

    def mostra_opcoes(self):
        pass

    def mostra_func_com_disp(self):
        pass

    def mostra_itens_emprestados(self):
        pass

    def mostra_historico(self):
        pass
