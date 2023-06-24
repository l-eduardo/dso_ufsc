

class ControlExample:
    def __init__(self):
        self.__lista = []
        self.__view = ViewExample()
        self.__cabecalho = ["ID", "Nome", "E-mail", "Telefone"]
    
    def adiciona(self):
        dicionario_atributos = {"id": '', "nome": '', "email": '', "telefone": ''}
        valores = self.__view.tela_cria_edita("Example", dicionario_atributos)
        # Cria Objeto
        self.__lista.append()

    def valores_dos_objetos(self, lista_de_objetos: list):
        valores_dos_objetos = []
        for objeto in lista_de_objetos:
            valores_dos_objetos.append(list(vars(objeto).values()))
        print(valores_dos_objetos)
        return valores_dos_objetos

    def mostra_valores(self):
        self.__view.tela_lista_seleciona(self.__cabecalho, self.valores_dos_objetos(self.__lista))
    
    def edita_valores(self):
        selecao = self.__view.tela_lista_seleciona(self.__cabecalho, 
                                                     self.valores_dos_objetos(self.__lista), 
                                                     True)
        dicionario_atributos = {"id": selecao[0], 
                                "nome": selecao[1], 
                                "email": selecao[2], 
                                "telefone": selecao[3]}
        novos_valores = self.__view.tela_cria_edita("Example", dicionario_atributos)
        for objeto in self.__lista:
            if dicionario_atributos["id"] == objeto.ident:
                objeto.nome = novos_valores["nome"]
                objeto.email = novos_valores["email"]
                objeto.telefone = novos_valores["telefone"]

    def remove(self):
        selecao = self.__view.tela_lista_seleciona(self.__cabecalho, 
                                                     self.valores_dos_objetos(self.__lista), 
                                                     True)
        for objeto in self.__lista:
                    if selecao[0] == objeto.ident:
                         self.__lista.remove(objeto)