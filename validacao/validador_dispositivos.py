from typing import get_type_hints
from typing import cast


class ValidadorDispositivo:
    def validar_atributo(self, atributo, valor):
        nome_atributo = atributo.split("__")[-1]
        hint = get_type_hints(self.__class__.__init__).get(nome_atributo)

        if(isinstance(valor, hint)):
            return self, atributo, valor
        else:
            raise TypeError(f'O atributo {nome_atributo} deve ser do tipo {hint}')

        
    def __setattr__(self, nome_atributo, valor):
        self.validar_atributo(nome_atributo, valor)
        super().__setattr__(nome_atributo, valor)
