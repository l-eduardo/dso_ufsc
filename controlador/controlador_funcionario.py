from ..modelo.funcionario import Funcionario
from ..limite.limite_funcionario import LimiteFuncionario


class ControladorFuncionario:
    def __init__ (self):
        self.__funcionarios = [Funcionario]
        self.__limite_funcionario = LimiteFuncionario()

    def inclui_funcionario(self):
        dados = self.__limite_funcionario.recebe_dados_funcionario()
        for funcionario in self.__funcionarios:
            if funcionario.cpf == dados[1]:
                raise SystemError("Ja existe um funcionario com o identificador unico: CPF!")
        self.__funcionarios.append(Funcionario(dados[0],dados[1],dados[2],dados[3],dados[4],dados[5]))

    # ADD METODO EM TELA - ESTUDAR COMO ALTERAR CONFIG
    def altera_funcionario(self):
        cpf = self.__limite_funcionario.recebe_cpf()
        for funcionario in self.__funcionarios:
            if funcionario.cpf == cpf:
                pass
            else:
                raise SystemError(f"Funcionário de CPF:{cpf} não encontrado!")

    def deleta_funcionario(self):
            for funcionario in self.__funcionarios:
                if funcionario.cpf == self.__limite_funcionario.recebe_cpf():
                    self.__funcionarios.remove(funcionario)

    def lista_funcionarios(self):
        self.__limite_funcionario.mostra_funcionarios(self.__funcionarios)

    def filtra_por_propriedade(self, modelo):
        pass

    def retorna(self):
        pass

    def abre_tela(self):
        opcoes = {0: self.inclui_funcionario, 1: self.altera_funcionario, 2: self.deleta_funcionario,
                  3: self.lista_funcionarios, 4: self.filtra_por_propriedade, 5: self.retorna}
        opcoes[self.__limite_funcionario.mostra_tela_opcoes]()