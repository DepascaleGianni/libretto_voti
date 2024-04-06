import datetime

import flet as ft
class View(object):
    def __init__(self, page):
        self._page = page
        self._page.horizontal_alignment = 'CENTER'
        self._titolo=None
        self._datePicker=None

    def setController(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()

    def loadAll(self):
        self._titolo = ft.Text("il mio libretto voti ++", color="blue", size=24)

        #Row 1 info su esame
        self._txtIn = ft.TextField(label="Nome", width=200)
        self._cfu = ft.TextField(label="CFU", width=100)
        self._ddVoto = ft.Dropdown(label="Voto", width=100)
        self._fillDdVoto()

        self._datePicker = ft.DatePicker(
            first_date=datetime.datetime(2022,11,1),
            last_date=datetime.datetime(2025,10,31)
        )
        self._page.overlay.append(self._datePicker)

        self._btnCalendar = ft.ElevatedButton("Pick date",icon=ft.icons.CALENDAR_MONTH,
                                             on_click=lambda _: self._datePicker.pick_date())



        r1 = ft.Row([self._txtIn, self._cfu, self._ddVoto, self._btnCalendar],alignment=ft.MainAxisAlignment.CENTER)

        #Row 2
        self._btnAdd = ft.ElevatedButton("Add", on_click=self._controller.handleAdd)
        self._btnPrint = ft.ElevatedButton(text="Print",on_click=self._controller.handlePrint)

        r2 = ft.Row([self._btnAdd,self._btnPrint],alignment=ft.MainAxisAlignment.CENTER)

        #Row 3
        self._lvOut = ft.ListView()

        self._page.add(self._titolo, r1, r2,self._lvOut)

    def _fillDdVoto(self):
        for i in range(18,31):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append((ft.dropdown.Option("30L")))