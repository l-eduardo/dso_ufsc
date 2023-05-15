

class LimiteDepartamento:
    def __init__(self):
        self.__cabecalho = "="*50 + "Menu Departamento".center(21) + "="*50 + "\n"

    def recebe_dado(self, mensagem: str):
        dado = input(f"\n(Para sair digite 'sair')\nDigite {mensagem}: ")
        if dado == "sair":
            raise ValueError("\n>>> Operacao cancelada pelo usuario! <<<\n")
        else:
            return dado

    def valida_entrada_opcao(self):
        pass

    def move_dispositivo(self):
        pass

    def move_funcionario(self):
        print("Move funcionario entre departamentos: \n",
              "    1o - Digite o codigo de origem;\n",
              "    2o - Digite o CPF do funcionario;\n",
              "    3o - Digite o codigo de departamento de destino.")

    def mostra_dispositivos_departamento(self):
        pass

    def mostra_tela_opcoes(self, opcoes):
        return int(input(f"""{self.__cabecalho}
    Opcoes:
        1: inclui_departamento
        2: altera_departamento
        3: deleta_departamento
        4: lista_departamento
        5: lista_departamento_filtrados
        6: adicionar_dispositivo
        7: adicionar_funcionario
        8: mover_funcionario
        9: mover_dispositivo
        10: listar_dispositivos
        11: listar_funcionarios
        12: retorna
        
    Selecione a Opção desejada: """))

    def recebe_propriedade(self):
        print(f"{self.__cabecalho}",
              "\n",
              "Propriedades disponíveis: ",
              "\n\n",
              "    - Codigo\n",
              "    - Nome\n",
              "\n",
              "    - Sair para sair",
              "\n")
        propriedade = input("Digite a Propiedade desejada: ").lower()
        if propriedade in ["codigo","nome"]:
            return propriedade
        elif propriedade == "sair":
            raise ValueError("\n>>> Operacao cancelada pelo usuario! <<<\n")
        else:
            raise ValueError("Esta propriedade não existe!")

    def mostra_dispositivos_funcionarios(self, lista: list):
        atributos = vars(lista[0]).keys()
        cabecalho = " | ".join(atributos)
        print(cabecalho)
        for item in lista:
            print(item)

    def mostra_departamentos(self, departamentos: list):
        print("|", "codigo", "|", "nome", "|")
        for departamento in departamentos:
            print(departamento)
