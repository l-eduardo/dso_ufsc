from modelo.departamento import Departamento
from limite.limite_departamento import LimiteDepartamento


class ControladorDepartamento:
    def __init__ (self):
        self.__departamentos = []
        self.__limite_departamento = LimiteDepartamento()

    def inclui_departamento(self):
        pass

    def altera_departamento(self):
        pass

    def deleta_departamento(self):
        pass

    def lista_departamento(self):
        pass

    def filtra_por_propriedade(self):
        pass

    def retorna(self):
        pass

    def abre_tela(self):
        pass

    def adicionar_dispositivo(self):
        pass

    def adicionar_funcionario(self):
        pass

    def mover_funcionario(self):
        # Pede CPF
        # Pede Departamento
        pass

    def mover_dispositivo(self, patrimonio: str, departamento: str):
        # Pede Patrimonio
        # Pede Departamento
        pass

    def listar_dispositivos(self):
        # Pede Departamento
        pass

    def listar_funcionarios(self):
        # Pede Departamento
        pass

