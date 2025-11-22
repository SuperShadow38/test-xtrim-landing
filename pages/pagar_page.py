from playwright.sync_api import Page

class PagarPage:

    def __init__(self, page: Page):
        self.page = page

    def validar_carga(self):
        """Valida que el landing de pagos cargó."""
        self.page.wait_for_load_state("domcontentloaded")
        assert "pagos.xtrim.com.ec" in self.page.url.lower()
