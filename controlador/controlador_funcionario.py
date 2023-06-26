from modelo.funcionario import Funcionario
from limite.limite_funcionario import LimiteFuncionario
from exceptions.selecao_nula import SelecaoNulaException
from controlador.abs.crud_abs import Crud
import re


class ControladorFuncionario(Crud):
    def __init__ (self, controlador_sistema):
        super().__init__(T=Funcionario,  nome_cp="cpf")
        self.__limite_funcionario = LimiteFuncionario()
        self.__controlador_sistema = controlador_sistema

    def inclui(self):
        dicionario_atributos = {"cpf": '',
                                "nome": '',
                                "email": '',
                                "telefone": '',
                                "cargo": '',
                                "endereco": ''}
        valores = self.__limite_funcionario.tela_cria_edita(dicionario_atributos)
        if not valores:
            return self.abre_tela()
        try:
            funcionario = Funcionario(re.sub(r"[^\d]", "", valores["cpf"]),
                                      valores["nome"],
                                      valores["email"],
                                      valores["telefone"],
                                      valores["cargo"],
                                      valores["endereco"])
            super().inclui(funcionario)
        except Exception as e:
            self.__limite_funcionario.popup(repr(e))
        self.abre_tela()

    def altera(self):
        try:
            selecao = self.__limite_funcionario.tela_lista_seleciona(
                                                         self.valores_dos_objetos(super().lista.values()),
                                                         edit_mode=True)
            if not selecao:
                return self.abre_tela()
            dicionario_atributos = {"cpf": selecao[0],
                                    "nome": selecao[1],
                                    "email": selecao[2],
                                    "telefone": selecao[3],
                                    "cargo": selecao[4],
                                    "endereco": selecao[5]}
            novos_valores = self.__limite_funcionario.tela_cria_edita(dicionario_atributos,
                                                                      edit_mode=True)
            cpf = dicionario_atributos["cpf"]
            super().altera(cpf, novos_valores)
        except ValueError as e:
            self.__limite_funcionario.popup(repr(e))
        except SelecaoNulaException as e:
            self.__limite_funcionario.popup(repr(e))
        self.abre_tela()

    def deleta(self):
        try:
            cpf = self.__limite_funcionario.tela_lista_seleciona(self.valores_dos_objetos
                                                                     (super().lista.values()),
                                                                     edit_mode=True)
            if cpf:
                super().deleta(cpf[0])
        except SelecaoNulaException as e:
            self.__limite_funcionario.popup(repr(e))
        self.abre_tela()

    def valores_dos_objetos(self, lista_de_objetos: list):
        valores_dos_objetos = []
        for objeto in lista_de_objetos:
            valores_dos_objetos.append(list(vars(objeto).values()))
        return valores_dos_objetos

    def lista(self):
        self.__limite_funcionario.tela_lista_seleciona(
            self.valores_dos_objetos(list(super().lista.values()))
            )
        self.abre_tela()

    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {"Criar": self.inclui,
                  "Editar": self.altera,
                  "Listar": self.lista,
                  "Remover": self.deleta}
        botao_clicado = self.__limite_funcionario.tela_menu(opcoes.keys())
        if botao_clicado:
            opcoes[botao_clicado]()
