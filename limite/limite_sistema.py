import time
import sys
import limite.textos.sistema as textos


class LimiteSistema:
        def tela_opcoes(self):
            for c in textos.opt:
                print(c, end="")
                # sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.025)

            opt = input("Escolha a opcao: ")

            return self.valida_entrada(opt)

        def valida_entrada(self, opt):
            try:
                opt = int(opt)
                if opt < 0 or opt > 4:
                    raise ValueError("Opcao invalida")
                return opt
            except Exception as e:
                print(e)
                self.tela_opcoes()

