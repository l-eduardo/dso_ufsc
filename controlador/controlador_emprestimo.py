from datetime import date
from DAO.dao import DAO
from controlador.abs.crud_abs import Crud
from limite.limite_emprestimo import LimiteEmprestimo
from modelo.emprestimo import Emprestimo
from modelo.funcionario import Funcionario
from modelo.computador import Computador


class ControladorEmprestimo(Crud):
    def __init__(self, controlador_sistema):
        super().__init__(T=Emprestimo, nome_cp="id")
        self.__controlador_sistema = controlador_sistema
        self.__limite_emprestimo = LimiteEmprestimo()
        self.__dao_funcionario = DAO(datasource=Funcionario.__name__)
        self.__dao_computador = DAO(datasource=Computador.__name__)

    def inclui(self):
        chave_computador = self.__limite_emprestimo.pega_dados("computador")
        chave_funcionario = self.__limite_emprestimo.pega_dados("funcionario")
        computador = self.__dao_computador.get(chave_computador)
        funcionario = self.__dao_funcionario.get(chave_funcionario)
        try:
            emprestimo = Emprestimo(dispositivo=computador,
                                    funcionario=funcionario,
                                    data_inicio=date.today())
        except ValueError as e:
            print("Erro ao criar emprestimo: " + repr(e))
            self.abre_tela()

        return super().inclui(emprestimo)    

    def lista(self):
        print(super().lista)

    # def altera(self):
    #     pass

    # def deleta(self):
    #     pass

    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        pass

    def funcionarios_com_itens(self):
        funcionarios = []
        for emprestimo in super().lista.values():
            if emprestimo.funcionario not in funcionarios:
                funcionarios.append(emprestimo.funcionario)
        self.__limite_emprestimo.mostra_funcionarios(funcionarios)

    def dispositivos_emprestados(self):
        dispositivos = []
        for emprestimo in super().lista.values():
            if emprestimo.dispositivo not in dispositivos:
                dispositivos.append(emprestimo.dispositivo)
        print(dispositivos)
        self.__limite_emprestimo.mostra_dispositivos(dispositivos)

    def historico(self):
        emprestimos = [emprestimo for emprestimo in super().lista.values() if emprestimo.esta_finalizado()]
        self.__limite_emprestimo.mostra_emprestimos(emprestimos)
        
    def esta_emprestado(self):
        emprestimos = [emprestimo for emprestimo in super().lista.values() if not emprestimo.esta_finalizado()]
        self.__limite_emprestimo.mostra_emprestimos(emprestimos)



ce = ControladorEmprestimo(controlador_sistema=None)

# ce.inclui()

# ce.lista()
# ce.funcionarios_com_itens()
# ce.dispositivos_emprestados()
ce.esta_emprestado()