import PySimpleGUI as sg


class Menus:
    @staticmethod
    def buttons_menu_setup(texts: list):
        buttons = []
        for index, text in enumerate(texts, start=1):
            buttons.append([sg.Button(text, key=index, pad=(0, (10, 5)), expand_x=True)])     
        return buttons