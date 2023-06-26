

class SelecaoNulaException(Exception):
    def __init__(self):
        super().__init__("Nenhum objeto selecionado, nenhuma alteraçao realizada!")