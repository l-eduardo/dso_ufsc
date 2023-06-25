import os
import sys

current_dir = os.getcwd()
sys.path.append(current_dir)

from controlador.controlador_sistema import ControladorSistema
import PySimpleGUI as sg



if __name__ == "__main__":
  sg.ChangeLookAndFeel('DarkBlue12')
  ControladorSistema().abre_tela()()

