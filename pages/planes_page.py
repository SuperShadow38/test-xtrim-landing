from playwright.sync_api import Page
from utils.config import ZAPPING_UPGRADE_URL

class PlanesPage:

    def __init__(self, page: Page):
        self.page = page
        self.planes = self.page.get_by_text("Plan Pro Zapping")
        self.boton_actualiza = self.page.locator(
            "a[href*='zappingsva.xtrim.com.ec/upgrade/login']"
        )
        self.titulo_upgrade = self.page.get_by_role(
            "heading",
            name="Accede a Tu Oferta Personalizada",
        )

    def abrir_actualizacion(self):
        self.planes.wait_for(state="visible")
        for i in range(self.boton_actualiza.count()):
            link = self.boton_actualiza.nth(i)
            if not link.is_visible():
                continue

            href = link.get_attribute("href")
            if not href or "zappingsva.xtrim.com.ec/upgrade/login" not in href.lower():
                continue

            self.page.goto(href, wait_until="domcontentloaded")
            return

        raise AssertionError("No se encontró una CTA visible de actualización en Zapping")

    def validar_landing_actualizacion(self):
        self.page.wait_for_url(f"{ZAPPING_UPGRADE_URL}**")
        self.titulo_upgrade.wait_for(state="visible")
        assert "upgrade plan internet" in self.page.title().lower()
