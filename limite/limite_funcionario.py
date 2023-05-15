

class LimiteFuncionario:
    def __init__ (self):
        self.__cabecalho = "="*50 + "Menu Funcionario".center(21) + "="*50 + "\n"

    def recebe_dado(self, mensagem: str):
        dado = input(f"\n(Para sair digite 'sair')\nDigite {mensagem}: ")
        if dado == "sair":
            raise ValueError("\n>>> Operacao cancelada pelo usuario! <<<\n")
        else:
            return dado

    def valida_entrada_opcao(self):
        pass

    def mostra_tela_opcoes(self):
        return int(input (f"""{self.__cabecalho}
    Opcoes:
        [1] Criar funcionário
        [2] Editar funcionário
        [3] Excluir funcionário
        [4] Listar funcionários
        [5] Pesquisa com filtro
        [6] Retornar
        
    Selecione a Opção desejada: """))

    def mostra_tela_propriedades(self):
        propriedade = input (f"""{self.__cabecalho}
    Digite a Propiedade desejada:

        - CPF
        - Nome
        - Email
        - Telefone
        - Cargo
        - Endereco\n\n""").lower()
        if propriedade in ["cpf","nome","email","telefone", "cargo", "endereco"]:
            return propriedade
        else:
            raise ValueError("Esta propriedade não existe!")

    def mostra_funcionarios(self, funcionarios: list):
        print("\n\n|","CPF","|","NOME","|","CARGO","|","EMAIL","|","TELEFONE","|","ENDERECO","|")
        for func in funcionarios:
            print("|",func.cpf,"|",func.nome,"|",func.cargo,"|",func.email,"|",func.telefone,"|",func.endereco,"|")
        input("\n\nPressione qualquer tecla para continuar...")
