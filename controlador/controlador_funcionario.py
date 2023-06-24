from modelo.funcionario import Funcionario
from limite.limite_funcionario import LimiteFuncionario


class ControladorFuncionario:
    def __init__ (self, controlador_sistema):
        self.__lista = []
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
            for funcionario in self.__lista:
                if funcionario.cpf == cpf:
                    raise ValueError("CPF ja cadastrado! Informe outro CPF ou digite 'sair' para voltar ao menu")
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
        print(self.__lista[-1].__dict__)

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

# Testes
c = ControladorFuncionario("")
c.adiciona()
c.adiciona()
c.edita_valores()
c.mostra_valores()
c.remove()
c.mostra_valores()