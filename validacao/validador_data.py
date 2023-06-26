import re

class ValidadorData:
    @staticmethod
    def verificar_data(data):
        padrao = r"^(0[1-9]|1\d|2\d|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        if re.match(padrao, data):
            return True
        else:
            raise ValueError("A data não está no formato correto (dd/mm/aaaa).")