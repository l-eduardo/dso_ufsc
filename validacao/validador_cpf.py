from exceptions.cpf_invalido import CPFInvalidoException


class ValidadorCPF:
    def __init__ (self, cpf: str):
         self.__cpf = cpf
         self.__digitos = [int(digito) for digito in cpf]

    def valida_cpf(self):             
            if len(self.__cpf) != 11:
                raise CPFInvalidoException()
            if (self.__digitos[-2] == self.__primeiro_digito()) and\
                (self.__digitos[-1] == self.__segundo_digito()):
                return 0
            else:
                raise CPFInvalidoException()

    def __primeiro_digito(self):
            prim_soma = sum(digito * peso for digito, peso in zip(self.__digitos[:9], range(10, 1, -1)))
            if prim_soma % 11 < 2:
                return 0
            else:
                return 11 - (prim_soma % 11)

    def __segundo_digito(self):
            seg_soma = sum(self.__digito * peso for self.__digito, peso in zip(self.__digitos[:10], range(11, 1, -1)))
            if seg_soma % 11 < 2:
                return 0
            else:
                return 11 - (seg_soma % 11)
