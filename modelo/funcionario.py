

class Funcionario:
    def __init__ (self, cargo: str, cpf: str, email: str, endereco: str, nome: str, telefone: str):
        # Controladora do sistema - valida dados
        self.__cargo = cargo
        self.__cpf = cpf
        self.__email = email
        self.__endereco = endereco
        self.__nome = nome
        self.__telefone = telefone

    def __str__(self):
        return f"{self.__cpf} | {self.__nome} | {self.__email} | {self.__telefone} | {self.__cargo} | {self.__endereco}"

    def __eq__(self, __value: object):
        if isinstance(__value, Funcionario):
            return self.__cpf == __value.cpf
        return False

    @property
    def cargo(self) -> str:
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        # Validar dados
        self.__cargo = cargo

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        # Validar dados
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        # Validar dados
        self.__email = email

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        # Validar dados
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        # Validar dados
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        # Validar dados
        self.__telefone = telefone
