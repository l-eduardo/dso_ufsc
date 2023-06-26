

class ChaveUnicaException(Exception):
    def __init__(self):
        super().__init__("A chave única (CPF ou Patrimonio) informada já está registrada!")