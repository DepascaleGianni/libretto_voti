from view import View
from voto import Libretto,Voto
import flet as ft
class Controller(object):
    def __init__(self,view : View):
        self._view = view
        self._model = Libretto()
        self.startupLib()
        self._model.stampa()

    def startupLib(self):
        self._model.append(Voto("analisi 1", 10, 20, False, '2022-01-30'))
        self._model.append(Voto('Fisica 1', 10, 25, False, '2022-07-12'))

    def handleAdd(self):
        pass
    def handlePrint(self):
        outList = self._model.stampaGUI()
        for el in outList:
            self._view._lvOut.controls.append(ft.Text(el))
        self._view.update()