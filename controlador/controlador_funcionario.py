from modelo.funcionario import Funcionario
from limite.limite_funcionario import LimiteFuncionario
from controlador.abs.crud_abs import Crud


class ControladorFuncionario(Crud):
    def __init__ (self, controlador_sistema):
        super().__init__(T=Funcionario,  nome_cp="cpf")
        self.__limite_funcionario = LimiteFuncionario()
        self.__controlador_sistema = controlador_sistema

    def verif_cpf_unico_valido(self, cpf: str):             
        if len(cpf) != 11:
            raise ValueError("O CPF não possui o numero de digitos correto! Tente novamente ou digite 'sair' para voltar ao menu")
        digitos = [int(digito) for digito in cpf]
        # calcula o primeiro digito de verificacao
        prim_soma = sum(digito * peso for digito, peso in zip(digitos[:9], range(10, 1, -1)))
        if prim_soma % 11 < 2:
            prim_verificacao = 0
        else:
            prim_verificacao = 11 - (prim_soma % 11)
        # calcula o segundo digito de verificacao
        seg_soma = sum(digito * peso for digito, peso in zip(digitos[:10], range(11, 1, -1)))
        if seg_soma % 11 < 2:
            seg_verificacao = 0
        else:
            seg_verificacao = 11 - (seg_soma % 11)
        # condicional se digitos do cpf sao validos
        if (digitos[-2] == prim_verificacao) and (digitos[-1] == seg_verificacao):
            # for funcionario in self.__funcionarios:
            #     if funcionario.cpf == cpf:
            #         raise ValueError("CPF ja cadastrado! Informe outro CPF ou digite 'sair' para voltar ao menu")
            return True
        else:
            raise ValueError("CPF inválido! Tente novamente ou digite 'sair' para voltar ao menu")

    def inclui(self):
        while True:
            try:
                dados = {"cargo": str, "cpf": str, "email": str, "endereco": str, "nome": str, "telefone": str}
                # Separa apenas os digitos numericos recebidos e os concatena em uma string
                dados["cpf"] = ''.join(filter(str.isdigit, self.__limite_funcionario.recebe_dado("o CPF do funcionario")))
                try:
                    self.verif_cpf_unico_valido(dados["cpf"])
                except Exception as e:
                    print(e)
                    continue
                dados["nome"] = self.__limite_funcionario.recebe_dado("o nome do funcionario")
                dados["email"] = self.__limite_funcionario.recebe_dado("o email do funcionario")
                dados["cargo"]= self.__limite_funcionario.recebe_dado("o cargo do funcionario")
                dados["telefone"] = self.__limite_funcionario.recebe_dado("o telefone do funcionario")
                dados["endereco"] = self.__limite_funcionario.recebe_dado("o endereco do funcionario")
                super().inclui(Funcionario(dados["cargo"],
                                           dados["cpf"],
                                           dados["email"],
                                           dados["endereco"],
                                           dados["nome"],
                                           dados["telefone"]))
            except ValueError as e:
                print(e)
                break
            break
        self.abre_tela()

    def altera(self):
        try:
            cpf = self.__limite_funcionario.recebe_dado("o CPF do funcionario a ser editado")
            propriedade = self.__limite_funcionario.mostra_tela_propriedades()
            novo_valor = self.__limite_funcionario.recebe_dado("o novo valor para a propriedade: ") 
        
            super().altera(cpf, propriedade, novo_valor)
        except ValueError as e:
            print(repr(e))
        self.abre_tela()

    def deleta(self):
        cpf = self.__limite_funcionario.recebe_dado("o CPF do funcionario a ser DELETADO")
        super().deleta(cpf)
        self.abre_tela()


    def lista(self):
        self.__limite_funcionario.mostra_funcionarios(super().lista)
        self.abre_tela()

    def busca(self):
        cpf = self.__limite_funcionario.recebe_dado("o CPF do funcionario a ser buscado")
        self.__limite_funcionario.mostra_funcionario(super().busca(cpf))
        self.abre_tela()

    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {1: self.inclui,
                  2: self.altera,
                  3: self.deleta,
                  4: self.lista,
                  5: self.busca,
                  6: self.retorna}
        opcoes[self.__limite_funcionario.mostra_tela_opcoes()]()

