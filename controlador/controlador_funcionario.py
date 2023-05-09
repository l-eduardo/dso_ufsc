from modelo.funcionario import Funcionario
from limite.limite_funcionario import LimiteFuncionario


class ControladorFuncionario:
    def __init__ (self):
        self.__funcionarios = []
        self.__limite_funcionario = LimiteFuncionario()

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
            for funcionario in self.__funcionarios:
                if funcionario.cpf == cpf:
                    raise ValueError("CPF ja cadastrado! Informe outro CPF ou digite 'sair' para voltar ao menu")
            return True
        else:
            raise ValueError("CPF inválido! Tente novamente ou digite 'sair' para voltar ao menu")

    def inclui_funcionario(self):
        while True:
            dados = {"cargo": "", "cpf": str, "email": "", "endereco": "", "nome": "", "telefone": ""}
            dados["cpf"] = self.__limite_funcionario.recebe_dado("CPF")
            if dados["cpf"] == "sair":
                break
            else:
                # Separa apenas os digitos numericos recebidos e os concatena em uma string
                dados["cpf"] = ''.join(filter(str.isdigit, dados["cpf"]))
                try:
                    self.verif_cpf_unico_valido(dados["cpf"])
                except Exception as e:
                    print(e)
                    continue
            dados["nome"] = self.__limite_funcionario.recebe_dado("nome")
            if dados["nome"] == "sair":
                break
            dados["email"] = self.__limite_funcionario.recebe_dado("email")
            if dados["email"] == "sair":
                break
            dados["cargo"]= self.__limite_funcionario.recebe_dado("cargo")
            if dados["cargo"] == "sair":
                break
            dados["telefone"] = self.__limite_funcionario.recebe_dado("telefone")
            if dados["telefone"] == "sair":
                break
            dados["endereco"] = self.__limite_funcionario.recebe_dado("endereco")
            if dados["endereco"] == "sair":
                break
            self.__funcionarios.append(Funcionario(dados["cargo"],
                                                   dados["cpf"],
                                                   dados["email"],
                                                   dados["endereco"],
                                                   dados["nome"],
                                                   dados["telefone"]))
            break
        self.abre_tela()

    # ADD METODO EM TELA - ESTUDAR COMO ALTERAR CONFIG
    def altera_funcionario(self):
        cpf = self.__limite_funcionario.recebe_cpf()
        for funcionario in self.__funcionarios:
            if funcionario.cpf == cpf:
                pass
            else:
                raise SystemError(f"Funcionário de CPF:{cpf} não encontrado!")
        self.abre_tela()

    def deleta_funcionario(self):
            cpf = self.__limite_funcionario.recebe_cpf()
            for funcionario in self.__funcionarios:
                if funcionario.cpf == cpf:
                    self.__funcionarios.remove(funcionario)
            self.abre_tela()

    def lista_funcionarios(self):
        self.__limite_funcionario.mostra_funcionarios(self.__funcionarios)
        self.abre_tela()

    def filtra_por_propriedade(self, modelo):
        pass

    def retorna(self):
        pass

    def abre_tela(self):
        opcoes = {1: self.inclui_funcionario,
                  2: self.altera_funcionario,
                  3: self.deleta_funcionario,
                  4: self.lista_funcionarios,
                  5: self.filtra_por_propriedade,
                  6: self.retorna}
        opcoes[self.__limite_funcionario.mostra_tela_opcoes()]()


cf = ControladorFuncionario()
cf.abre_tela()