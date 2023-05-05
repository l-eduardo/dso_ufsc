

class LimiteFuncionario:
    def __init__ (self):
        self.__cabecalho = "="*50 + "Menu Funcionario".center(21) + "="*50 + "\n\n"

    # OTIMIZAR COM RECEBE DADOS
    def recebe_cpf(self):
        return input(f"{self.__cabecalho}Digite o cpf do funcionário: ")
    
    def recebe_dados_funcionario(self):
        mensagem_cargo = "Digite o cargo do funcionário: "
        mensagem_cpf = "Digite o cpf do funcionário: "
        mensagem_email = "Digite o email do funcionário: "
        mensagem_endereco = "Digite o endereco do funcionário: "
        mensagem_nome = "Digite o nome do funcionário: "
        mensagem_telefone = "Digite o telefone do funcionário: "
        return [input(mensagem_cargo),input(mensagem_cpf),input(mensagem_email),
                input(mensagem_endereco),input(mensagem_nome),input(mensagem_telefone)]
    
    def valida_entrada_opcao(self):
        pass

    def mostra_tela_opcoes(self):
        return input (self.__cabecalho,
                        "Selecione a Opção desejada: \n",
                        "    [1] Criar funcionário\n",
                        "    [2] Editar funcionário\n",
                        "    [3] Excluir funcionário\n",
                        "    [4] Listar funcionários\n",
                        "    [5] Pesquisa com filtro\n",
                        "    [6] Retornar\n")

    def mostra_funcionarios(funcionarios: list):
        print("|","CPF".center(14),"|","NOME".center(48),"|","CARGO".center(20),"|","EMAIL".center(32),"|","TELEFONE".center(13),"|","ENDERECO".center(64),"|")
        for func in funcionarios:
            print("|",func.cpf.ljust(14),"|",func.nome.ljust(48),"|",func.cargo.ljust(20),"|",func.email.ljust(32),"|",func.telefone.ljust(13),"|",func.endereco.ljust(64),"|")
