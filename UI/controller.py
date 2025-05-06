import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        try:
            anno = int(self._view._txtAnno.value)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è un numero", color="red"))
            self._view.update_page()
            return
        if not 1816 <= anno <= 2016:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è compreso tra 1816 e 2016", color="red"))
            self._view.update_page()

        self._model.buildGraph(anno)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Il grafo è stato correttamente creato!", color="lightblue"))
        self._view.update_page()

        vicini = self._model.getVicini()
        #vicini.sort()

        #self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {conn} componenti connesse"))
        for v in vicini:
            if v is not None:
                self._view._txt_result.controls.append(ft.Text(f"{v}: {vicini[v]["n"]}"))
        self._view.update_page()
