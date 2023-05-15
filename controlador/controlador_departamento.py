from modelo.departamento import Departamento
from limite.limite_departamento import LimiteDepartamento

class ControladorDepartamento:
    def __init__ (self):
        self.__departamentos = []
        self.__limite_departamento = LimiteDepartamento()

    def valida_codigo(self, codigo: str):
        for departamento in self.__departamentos:
            if departamento.codigo == codigo:
                raise ValueError(f">> O codigo {codigo} ja está vinculado ao departamento {departamento.nome}! Tente com outro valor ou entre 'sair' para deixar o sistema")
        return True

    def departamento_por_codigo(self):
        codigo = self.__limite_departamento.recebe_dado("o codigo do Departamento")
        for departamento in self.__departamentos:
            if departamento.codigo == codigo:
                return departamento
        raise ValueError(f">> Valor não encontrado!")

    def inclui_departamento(self):
        while True:
            dados = {"codigo": str, "nome": str}
            try:
                dados["codigo"] = self.__limite_departamento.recebe_dado("o codigo do Departamento")
                try:
                    self.valida_codigo(dados["codigo"])
                except ValueError as e:
                    print(e)
                    continue
                dados["nome"] = self.__limite_departamento.recebe_dado("o nome do Departamento")
                self.__departamentos.append(Departamento(dados["codigo"], dados["nome"]))
                break
            except ValueError as e:
                print(e)
                break
        self.abre_tela()

    def altera_departamento(self):
            try:
                departamento = self.departamento_por_codigo()
                propriedade = self.__limite_departamento.recebe_propriedade()
                valor = self.__limite_departamento.recebe_dado("o novo valor")
                if propriedade == "codigo":
                    while True:
                        try:
                            self.valida_codigo(propriedade)
                            break
                        except ValueError as e:
                            print(e)
                            valor = self.__limite_funcionario.recebe_dado("o novo valor")    
                setattr(departamento, propriedade, valor)
            except ValueError as e:
                print(e)
                self.abre_tela()

    def deleta_departamento(self):
        try:
            departamento = self.departamento_por_codigo()
            if len(departamento.funcionarios) > 0:
                raise ValueError(f"O departamento {departamento.nome} ainda possui funcionarios! Excluir ou mover todos antes de excluir o departamento.")
            elif len(departamento.dispositivos) > 0:
                raise ValueError(f"O departamento {departamento.nome} ainda possui dispositivos! Excluir ou mover todos antes de excluir o departamento.")
            else:
                self.__departamentos.remove(departamento)
        except ValueError as e:
            print(e)
        self.abre_tela()

    def lista_departamento(self):
        self.__limite_departamento.mostra_departamentos(self.__departamentos)
        self.abre_tela()

    def lista_departamento_filtrados(self): ########### REMOVER?
        # filtra como em funcionario
        pass

    def adicionar_dispositivo(self):
        try:
            departamento = self.departamento_por_codigo()
        # controlador geral acessa controlador dispositvo e escolhe por patrimonio
        except ValueError as e:
            print(e)
            self.abre_tela()

    def adicionar_funcionario(self):
        try:
            departamento = self.departamento_por_codigo()
        # controlador geral acessa controlador funcionario e escolhe por CPF
        except ValueError as e:
            print(e)
            self.abre_tela()

    def mover_dispositivo(self, patrimonio: str, departamento: str):
        try:
            departamento = self.departamento_por_codigo()
            # Pede Patrimonio
            # Pede Departamento
        except ValueError as e:
            print(e)
            self.abre_tela()

    def mover_funcionario(self):
        try:
            departamento_origem = self.departamento_por_codigo()
            cpf = self.__limite_departamento.recebe_dado("o codigo do Departamento")
            departamento_destino = self.departamento_por_codigo()
            for funcionario in departamento_destino.funcionarios:
                if funcionario.cpf == cpf:
                    departamento_destino.append(funcionario)
                    departamento_origem.remove(funcionario)
                    self.abre_tela()
            raise ValueError(f"Funcionario de CPF {cpf} nao encontrado no departamento {departamento_origem}!")
        except ValueError as e:
            print(e)
            self.abre_tela()

    def listar_dispositivos(self):
        # Pede Departamento
        pass

    def listar_funcionarios(self):
        try:
            departamento = self.departamento_por_codigo()
            self.__limite_departamento.mostra_dispositivos_funcionarios(departamento.funcionarios)
        except ValueError as e:
            print(e)
        self.abre_tela()

    def retorna(self):
        pass

    def abre_tela(self):
        opcoes = {1: self.inclui_departamento,
                  2: self.altera_departamento,
                  3: self.deleta_departamento,
                  4: self.lista_departamento,
                  5: self.lista_departamento_filtrados,
                  6: self.adicionar_dispositivo,
                  7: self.adicionar_funcionario,
                  8: self.mover_funcionario,
                  9: self.mover_dispositivo,
                  10: self.listar_dispositivos,
                  11: self.listar_funcionarios,
                  12: self.retorna}
        opcoes[self.__limite_departamento.mostra_tela_opcoes(opcoes)]()
        pass

cd = ControladorDepartamento()
cd.abre_tela()