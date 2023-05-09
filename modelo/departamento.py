from modelo.funcionario import Funcionario


class Departamento:
    def __init__(self, codigo: int, nome: str):
        self.__codigo == codigo
        self.__nome == nome
        self.__dispositivos = []
        self.__funcionarios = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str):
        # Validar dados
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        # Validar dados
        self.__nome = nome

    @property
    def dispositivos(self):
        return self.__dispositivos

    @dispositivos.setter
    def dispositivos(self, dispositivos: list):
        # Validar dados
        self.__dispositivos = dispositivos

    @property
    def funcionarios(self):
        return self.__funcionarios

    @funcionarios.setter
    def funcionarios(self, funcionarios: list):
        # Validar dados
        self.__funcionarios = funcionarios

    def inclui_funcionario(self, funcionario_incluir: Funcionario):
        # Validar dados
        for funcionario_existente in self.__funcionarios:
            if funcionario_existente.cpf == funcionario_incluir.cpf:
                pass
        self.__funcionarios.append(funcionario_incluir)

    def deleta_funcionario(self, funcionario_excluir: Funcionario):
        for funcionario_existente in self.__funcionarios:
                if funcionario_existente.cpf == funcionario_excluir:
                    self.__funcionarios.remove(funcionario_excluir)
        # Else avisa que nao existe!

    def inclui_dispositivo(self, dispositivo_incluir):
        # Validar dados
        for dispositivo_existente in self.__dispositivo:
            if dispositivo_existente.patrimonio == dispositivo_incluir.patrimonio:
                pass
        self.__dispositivo.append(dispositivo_incluir)

    def deleta_dispositivo(self, dispositivo_excluir):
        for dispositivo_existente in self.__dispositivo:
                if dispositivo_existente.patrimonio == dispositivo_excluir:
                    self.__dispositivo.remove(dispositivo_excluir)
        # Else avisa que nao existe!
