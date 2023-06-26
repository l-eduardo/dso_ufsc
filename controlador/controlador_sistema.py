from controlador.controlador_computadores import ControladorComputadores
from controlador.controlador_departamento import ControladorDepartamento
from controlador.controlador_emprestimo import ControladorEmprestimo
from controlador.controlador_funcionario import ControladorFuncionario
from limite.limite_sistema import LimiteSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_emprestimo = ControladorEmprestimo(self)
        self.__controlador_departamento = ControladorDepartamento(self)
        self.__controlador_computadores = ControladorComputadores(self)
        self.__limite = LimiteSistema()

    def abre_tela(self):
        lista_opt = {
            0: self.sair,
            1: self.dispositivos,
            2: self.emprestimos,
            3: self.funcionarios,
            4: self.departamentos,
        }

        while True:
            lista_opt[self.__limite.tela_opcoes()]()

    def sair(self):
        exit(0);

    def dispositivos(self):
        self.__controlador_computadores.abre_tela()
    
    def emprestimos(self):
        self.__controlador_emprestimo.abre_tela()

    def funcionarios(self):
        self.__controlador_funcionario.abre_tela()

    def departamentos(self):
        self.__controlador_departamento.abre_tela()