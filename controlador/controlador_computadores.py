from controlador.abs.crud_abs import Crud
from modelo.computador import Computador
from limite.limite_computador import LimiteComputador


class ControladorComputadores(Crud):
    def __init__(self, controlador_sistema):
        super().__init__(T=Computador, nome_cp="patrimonio")
        self.__limiteComputador = LimiteComputador()
        self.__controlador_sistema = controlador_sistema


    def valores_dos_objetos(self, lista_de_objetos: list):
        valores_dos_objetos = []
        for objeto in lista_de_objetos:
            valores_dos_objetos.append(list(vars(objeto).values()))
        return valores_dos_objetos

    def lista(self):
        self.__limiteComputador.tela_lista_seleciona(self.valores_dos_objetos(list(super().lista.values())))

    def inclui(self):
        dicionario_atributos = {"Patrimonio": '',
                                "Marca": '',
                                "Modelo": '',
                                "Tipo": '',
                                "Serial Number": '',
                                "Processador": '',
                                "Memoria RAM": '',
                                "Armazenamento": '',
                                "Sistema Operacional": '',
                                "Prazo Garantia": ''}
        valores = self.__limiteComputador.tela_cria_edita(dicionario_atributos)
        try:
            computador = Computador(patrimonio=valores["Patrimonio"],
                                     marca=valores["Marca"],
                                     modelo=valores["Modelo"],
                                     tipo=valores["Tipo"],
                                     serial_number=valores["Serial Number"],
                                     processador=valores["Processador"],
                                     memoria_ram=int(valores["Memoria RAM"]),
                                     armazenamento=float(valores["Armazenamento"]),
                                     so=valores["Sistema Operacional"],
                                     fim_garantia=valores["Prazo Garantia"])
        except Exception as e:
            print("Erro: " + e)
            self.abre_tela()

        return super().inclui(computador)
    
    def altera(self):
        selecao = self.__limiteComputador.tela_lista_seleciona( 
                                                     self.valores_dos_objetos(super().lista.values()), 
                                                     edit_mode=True)
        dicionario_atributos = {"patrimonio": selecao[0],
                                "marca": selecao[1],
                                "modelo": selecao[2],
                                "tipo": selecao[3],
                                "serial_number": selecao[4],
                                "processador": selecao[5],
                                "memoria_ram": selecao[6],
                                "armazenamento": selecao[7],
                                "so": selecao[8],
                                "fim_garantia": selecao[9]}
        novos_valores = self.__limiteComputador.tela_cria_edita(dicionario_atributos)
        try:
            novos_valores["memoria_ram"] = int(novos_valores["memoria_ram"])
            novos_valores["armazenamento"] = float(novos_valores["armazenamento"])
            patrimonio = dicionario_atributos["patrimonio"] 
            super().altera(patrimonio, novos_valores)
        except ValueError as e:
            print(repr(e))
        self.abre_tela()
        
    def deleta(self):
        lista_valores = self.valores_dos_objetos(super().lista.values())
        patrimonio = self.__limiteComputador.tela_lista_seleciona(lista_valores, 
                                                                  edit_mode=True)[0]
        super().deleta(patrimonio)
        self.abre_tela()
        
    def abre_tela(self):
        opcoes = {"Criar": self.inclui,
                  "Editar": self.altera,
                  "Listar": self.lista,
                  "Remover": self.deleta}
        botao_clicado = self.__limiteComputador.tela_menu(opcoes.keys())
        if botao_clicado:
            opcoes[botao_clicado]()

    def retorna(self):
        self.__controlador_sistema.abre_tela()
