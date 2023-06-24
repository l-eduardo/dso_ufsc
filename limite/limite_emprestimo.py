

class LimiteEmprestimo:
    def __init__(self):
        pass

    def pega_dados(self, mensagem: str):
        dado = input(f"\n('sair' p/ sair)\nDigite {mensagem}: ")
        if dado == "sair":
            raise ValueError("\n>>> Operacao cancelada pelo usuario! <<<\n")
        else:
            return dado

    def mostra_opcoes(self):
        pass

    def mostra_func_com_disp(self, emprestimos):
        pass

    def mostra_funcionarios(self, funcionarios):
        pass
    
    def mostra_dispositivos(self, dispositivos):
        pass

    def mostra_emprestimos(self, emprestimos):
        pass
