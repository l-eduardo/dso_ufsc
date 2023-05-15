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
                self.__funcionarios.append(Funcionario(dados["cargo"],
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

    def filtra_por_propriedade(self, propriedade: str, valor: str):
        filtro = list(filter(lambda funcionario:
                             getattr(funcionario, propriedade) == valor,
                             self.__funcionarios))
        if len(filtro) == 0:
            raise ValueError(f">> Valor não encontrado ao aplicar filtro!")
        return filtro

    def altera_funcionario(self):
        try:
            cpf = self.__limite_funcionario.recebe_dado("o CPF do funcionario a ser editado")
            funcionarios = self.filtra_por_propriedade("cpf", cpf)
            if len(funcionarios) == 1:
                funcionario = funcionarios[0]
                propriedade = self.__limite_funcionario.mostra_tela_propriedades()
                valor = self.__limite_funcionario.recebe_dado("o novo valor")
                if propriedade == "cpf":
                    while True:
                        try:
                            self.verif_cpf_unico_valido(valor)
                            break
                        except Exception as e:
                            print(e)
                            valor = self.__limite_funcionario.recebe_dado("o novo valor")
                setattr(funcionario, propriedade, valor)
        except ValueError as e:
            print(e)
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

    def lista_funcionarios_filtrados(self):
        try:
            propriedade = self.__limite_funcionario.mostra_tela_propriedades()
            valor = self.__limite_funcionario.recebe_dado("o valor para filtro: ")
            filtro = self.filtra_por_propriedade(propriedade, valor)
            self.__limite_funcionario.mostra_funcionarios(filtro)
        except Exception as e:
            print(e)
        self.abre_tela()

    def retorna(self):
        #sistema.menu_principal()
        pass

    def abre_tela(self):
        opcoes = {1: self.inclui_funcionario,
                  2: self.altera_funcionario,
                  3: self.deleta_funcionario,
                  4: self.lista_funcionarios,
                  5: self.lista_funcionarios_filtrados,
                  6: self.retorna}
        opcoes[self.__limite_funcionario.mostra_tela_opcoes()]()


cf = ControladorFuncionario()
cf.abre_tela()