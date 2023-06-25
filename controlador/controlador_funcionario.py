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

# =======
    def inclui(self):
        dicionario_atributos = {"cpf": '',
                                "nome": '',
                                "email": '',
                                "telefone": '',
                                "cargo": '',
                                "endereco": ''}
        valores = self.__limite_funcionario.tela_cria_edita(dicionario_atributos)
        try:
            funcionario = Funcionario(valores["cpf"],
                                      valores["nome"],
                                      valores["email"],
                                      valores["telefone"],
                                      valores["cargo"],
                                      valores["endereco"])
        except Exception as e:
            print("Erro: " + e)
            self.abre_tela()

        return super().inclui(funcionario)

    def altera(self):
        selecao = self.__limite_funcionario.tela_lista_seleciona( 
                                                     self.valores_dos_objetos(super().lista.values()), 
                                                     True)
        dicionario_atributos = {"cpf": selecao[0], 
                                "nome": selecao[1], 
                                "email": selecao[2], 
                                "telefone": selecao[3],
                                "cargo": selecao[4],
                                "endereco": selecao[5]}
        novos_valores = self.__limite_funcionario.tela_cria_edita(dicionario_atributos)
        try:
            cpf = dicionario_atributos["cpf"] 
            super().altera(cpf, novos_valores)
        except ValueError as e:
            print(repr(e))
        self.abre_tela()

    def deleta(self):
        cpf = self.__limite_funcionario.tela_lista_seleciona(self.valores_dos_objetos
                                                                 (super().lista.values()), 
                                                                 True)[0]
        super().deleta(cpf)
        self.abre_tela()

    def valores_dos_objetos(self, lista_de_objetos: list):
        valores_dos_objetos = []
        for objeto in lista_de_objetos:
            valores_dos_objetos.append(list(vars(objeto).values()))
        return valores_dos_objetos

    def lista(self):
        self.__limite_funcionario.tela_lista_seleciona(self.valores_dos_objetos(list(super().lista.values())))

    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {"Criar": self.inclui,
                  "Editar": self.altera,
                  "Listar": self.lista,
                  "Remover": self.deleta}
        opcoes[self.__limite_funcionario.tela_menu(opcoes.keys())]()
        

