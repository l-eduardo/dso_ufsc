

class CPFInvalidoException(Exception):
    def __init__(self):
        super().__init__("O CPF informado é inválido")