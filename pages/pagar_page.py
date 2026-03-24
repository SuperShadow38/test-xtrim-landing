from playwright.sync_api import Page

class PagarPage:

    def __init__(self, page: Page):
        self.page = page
        self.titulo = self.page.get_by_text("Pagos Rápidos")
        self.identificacion = self.page.get_by_role(
            "textbox",
            name="Ingrese su número de Cédula",
        )

    def validar_carga(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.titulo.wait_for(state="visible")
        self.identificacion.wait_for(state="visible")
        assert "pagos.xtrim.com.ec" in self.page.url.lower()
        assert "landing cobros xtrim" in self.page.title().lower()
