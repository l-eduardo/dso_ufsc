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
            return True
        else:
            raise ValueError("CPF inválido! Tente novamente ou digite 'sair' para voltar ao menu")
    
    def adiciona(self):
        dicionario_atributos = {"cpf": '',
                                "nome": '',
                                "email": '',
                                "telefone": '',
                                "cargo": '',
                                "endereco": ''}
        valores = self.__limite_funcionario.tela_cria_edita("Funcionario", dicionario_atributos)
        self.__lista.append(Funcionario(valores["cpf"],
                                        valores["nome"],
                                        valores["email"],
                                        valores["telefone"],
                                        valores["cargo"],
                                        valores["endereco"]))
#telas psg
    def valores_dos_objetos(self, lista_de_objetos: list):
        valores_dos_objetos = []
        for objeto in lista_de_objetos:
            valores_dos_objetos.append(list(vars(objeto).values()))
        return valores_dos_objetos

    def mostra_valores(self):
        self.__limite_funcionario.tela_lista_seleciona(self.valores_dos_objetos(self.__lista))
    
    def edita_valores(self):
        selecao = self.__limite_funcionario.tela_lista_seleciona( 
                                                     self.valores_dos_objetos(self.__lista), 
                                                     True)
        dicionario_atributos = {"id": selecao[0], 
                                "nome": selecao[1], 
                                "email": selecao[2], 
                                "telefone": selecao[3],
                                "cargo": selecao[4],
                                "endereco": selecao[5]}
        novos_valores = self.__limite_funcionario.tela_cria_edita("Example", dicionario_atributos)
        for objeto in self.__lista:
            if dicionario_atributos["id"] == objeto.cpf:
                objeto.nome = novos_valores["nome"]
                objeto.email = novos_valores["email"]
                objeto.telefone = novos_valores["telefone"]
                objeto.cargo = novos_valores["cargo"]
                objeto.endereco = novos_valores["endereco"]

    def remove(self):
        selecao = self.__limite_funcionario.tela_lista_seleciona(self.valores_dos_objetos
                                                                 (self.__lista), 
                                                                 True)
        for objeto in self.__lista:
                    if selecao[0] == objeto.cpf:
                         self.__lista.remove(objeto)
# =======
#     def inclui(self):
#         while True:
#             try:
#                 dados = {"cargo": str, "cpf": str, "email": str, "endereco": str, "nome": str, "telefone": str}
#                 # Separa apenas os digitos numericos recebidos e os concatena em uma string
#                 dados["cpf"] = ''.join(filter(str.isdigit, self.__limite_funcionario.recebe_dado("o CPF do funcionario")))
#                 try:
#                     self.verif_cpf_unico_valido(dados["cpf"])
#                 except Exception as e:
#                     print(e)
#                     continue
#                 dados["nome"] = self.__limite_funcionario.recebe_dado("o nome do funcionario")
#                 dados["email"] = self.__limite_funcionario.recebe_dado("o email do funcionario")
#                 dados["cargo"]= self.__limite_funcionario.recebe_dado("o cargo do funcionario")
#                 dados["telefone"] = self.__limite_funcionario.recebe_dado("o telefone do funcionario")
#                 dados["endereco"] = self.__limite_funcionario.recebe_dado("o endereco do funcionario")
#                 super().inclui(Funcionario(dados["cargo"],
#                                            dados["cpf"],
#                                            dados["email"],
#                                            dados["endereco"],
#                                            dados["nome"],
#                                            dados["telefone"]))
#             except ValueError as e:
#                 print(e)
#                 break
#             break
#         self.abre_tela()

#     def altera(self):
#         try:
#             cpf = self.__limite_funcionario.recebe_dado("o CPF do funcionario a ser editado")
#             propriedade = self.__limite_funcionario.mostra_tela_propriedades()
#             novo_valor = self.__limite_funcionario.recebe_dado("o novo valor para a propriedade: ") 
        
#             super().altera(cpf, propriedade, novo_valor)
#         except ValueError as e:
#             print(repr(e))
#         self.abre_tela()

#     def deleta(self):
#         cpf = self.__limite_funcionario.recebe_dado("o CPF do funcionario a ser DELETADO")
#         super().deleta(cpf)
#         self.abre_tela()


#     def lista(self):
#         self.__limite_funcionario.mostra_funcionarios(super().lista)
#         self.abre_tela()

#     def busca(self):
#         cpf = self.__limite_funcionario.recebe_dado("o CPF do funcionario a ser buscado")
#         self.__limite_funcionario.mostra_funcionario(super().busca(cpf))
#         self.abre_tela()

#     def retorna(self):
#         self.__controlador_sistema.abre_tela()

#     def abre_tela(self):
#         opcoes = {1: self.inclui,
#                   2: self.altera,
#                   3: self.deleta,
#                   4: self.lista,
#                   5: self.busca,
#                   6: self.retorna}
#         opcoes[self.__limite_funcionario.mostra_tela_opcoes()]()
# >>>>>>> develop
