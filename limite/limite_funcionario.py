

class LimiteFuncionario:
    def __init__ (self):
        self.__cabecalho = "="*50 + "Menu Funcionario".center(21) + "="*50 + "\n"

    # OTIMIZAR COM RECEBE DADOS
    def recebe_cpf(self):
        return input(f"{self.__cabecalho}Digite o cpf do funcionário: ")

    def recebe_dado(self, dado):
        return input(f"Digite o {dado} do funcionário: ")
    
    def valida_entrada_opcao(self):
        pass

    def mostra_tela_opcoes(self):
        return int(input (f"""{self.__cabecalho}
    Selecione a Opção desejada:

        [1] Criar funcionário
        [2] Editar funcionário
        [3] Excluir funcionário
        [4] Listar funcionários
        [5] Pesquisa com filtro
        [6] Retornar\n\n"""))

    def mostra_funcionarios(self, funcionarios: list):
        print("|","CPF","|","NOME","|","CARGO","|","EMAIL","|","TELEFONE","|","ENDERECO","|")
        for func in funcionarios:
            print("|",func.cpf,"|",func.nome,"|",func.cargo,"|",func.email,"|",func.telefone,"|",func.endereco,"|")
