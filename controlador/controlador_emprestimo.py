from limite.limite_emprestimo import LimiteEmprestimo
from modelo.emprestimo import Emprestimo
from modelo.funcionario import Funcionario
from datetime import date


class ControladorEmprestimo:
    def __init__(self, controlador_sistema):
        self.__limite_emprestimo = LimiteEmprestimo()
        self.__emprestimos = []
        self.__proximo_id = 1
        self.__controlador_sistema = controlador_sistema


    def inclui(self, dispositivos: list, funcionario: Funcionario):
        atributos = {"dispositivos": dispositivos, "funcionario": funcionario, "data_inicio": date}
        # pegar dispositivos da area do funcionario
        atributos["data_inicio"] = self.__limite_emprestimo.recebe_dado("a data de início")
        self.__emprestimos.append(Emprestimo(self.__proximo_id,
                                             atributos["dispositivos"],
                                             atributos["funcionario"],
                                             atributos["data_inicio"]))
        self.__proximo_id += 1
        self.abre_tela()

    def altera(self):
        pass

    def deleta(self):
        pass

    def lista(self):
        pass

    def filtra_por_propriedade(self):
        pass

    def retorna(self):
        pass

    def abre_tela(self):
        pass

    def funcionarios_com_itens(self):
        pass

    def dispositivos_emprestados(self):
        pass

    def historico():
        pass

    def esta_emprestado(self):
        pass
