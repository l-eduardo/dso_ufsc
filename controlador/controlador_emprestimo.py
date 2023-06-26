from datetime import date
from DAO.dao import DAO
from controlador.abs.crud_abs import Crud
from limite.limite_emprestimo import LimiteEmprestimo
from modelo.emprestimo import Emprestimo
from modelo.funcionario import Funcionario
from modelo.computador import Computador


class ControladorEmprestimo(Crud):
    def __init__(self, controlador_sistema):
        super().__init__(T=Emprestimo, nome_cp="id")
        self.__controlador_sistema = controlador_sistema
        self.__limite_emprestimo = LimiteEmprestimo()
        self.__dao_funcionario = DAO(datasource=Funcionario.__name__)
        self.__dao_computador = DAO(datasource=Computador.__name__)

    def inclui(self):
        try:
            valores_tela = self.__limite_emprestimo.tela_cria_edita(
                self.__dao_funcionario.get_all().values(),
                self.__dao_computador.get_all().values()
                )
            
            computador = self.__dao_computador.get(valores_tela["patrimonio"])
            funcionario = self.__dao_funcionario.get(valores_tela["cpf"])

            return super().inclui(Emprestimo(computador, funcionario))
        except Exception as e:
            print("Erro: " + repr(e))
            self.abre_tela()

    def finalizar_emprestimo(self):
        selecao = self.__limite_emprestimo.tela_lista_seleciona( 
                                                     self.valores_dos_objetos(super().lista.values()), 
                                                     edit_mode=True)
        id = selecao[0]
        try:
            emprestimo_finalizado = super().busca(id)
            emprestimo_finalizado.finalizar()
            super().altera(id, new_object=emprestimo_finalizado)
        except ValueError as e:
            print(repr(e))
        self.abre_tela()

    def lista(self):
        self.__limite_emprestimo.tela_lista_seleciona(self.valores_dos_objetos(super().lista.values()))

    def valores_dos_objetos(self, lista_de_objetos: list):
        valores_dos_objetos = []
        for objeto in lista_de_objetos:
            aux = [
                objeto.id,
                objeto.data_inicio,
                "Nao" if objeto.esta_finalizado() else "Sim",
                objeto.funcionario.nome,
                objeto.funcionario.cpf,
                objeto.dispositivo.patrimonio,
                "Sim" if objeto.dispositivo.esta_na_garantia() else "Não",
            ]
            valores_dos_objetos.append(aux)
        return valores_dos_objetos

    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            "Novo emprestimo": self.inclui,
            "Listar eprestimos": self.lista,
            "Finalizar emprestimo": self.finalizar_emprestimo,
            "Funcionarios com itens": self.funcionarios_com_itens,
            "Dispositivos emprestados": self.dispositivos_emprestados,
            "Historico": self.historico,
            "Emprestimos em andamento": self.esta_emprestado,
        }
        botao_clicado = self.__limite_emprestimo.tela_menu(opcoes.keys())
        if botao_clicado:
            opcoes[botao_clicado]()

    def monta_colunas_tabela(self, lista_de_objetos: list):
        valores_dos_objetos = []
        for objeto in lista_de_objetos:
            valores_dos_objetos.append(list(vars(objeto).values()))
        return valores_dos_objetos

    def funcionarios_com_itens(self):
        funcionarios = []
        for emprestimo in super().lista.values():
            if emprestimo.funcionario not in funcionarios:
                funcionarios.append(emprestimo.funcionario)
        super(LimiteEmprestimo, self.__limite_emprestimo).tela_lista_seleciona(self.monta_colunas_tabela(funcionarios))

    def dispositivos_emprestados(self):
        dispositivos = []
        for emprestimo in super().lista.values():
            if emprestimo.dispositivo not in dispositivos:
                dispositivos.append(emprestimo.dispositivo)
        print(dispositivos)
        super(LimiteEmprestimo, self.__limite_emprestimo).tela_lista_seleciona(self.monta_colunas_tabela(dispositivos))

    def historico(self):
        emprestimos = [emprestimo for emprestimo in super().lista.values() if emprestimo.esta_finalizado()]
        self.__limite_emprestimo.tela_lista_seleciona(self.valores_dos_objetos(emprestimos))

        
    def esta_emprestado(self):
        emprestimos = [emprestimo for emprestimo in super().lista.values() if not emprestimo.esta_finalizado()]
        self.__limite_emprestimo.tela_lista_seleciona(self.valores_dos_objetos(emprestimos))
