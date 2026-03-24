from playwright.sync_api import Page
from utils.config import CONTACTO_URL, PAGAR_URL, ZAPPING_URL

class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.popup_close = ".close"
        self.onesignal_cancel = "#onesignal-slidedown-cancel-button"
        self.link_pagos = self.page.locator("a[href*='pagos.xtrim.com.ec']")
        self.link_actualizar_plan = self.page.get_by_role("link", name="Actualizar Plan").first

    # -------------------------
    # Métodos base
    # -------------------------
    def navegar(self, url):
        self.page.goto(url, wait_until="domcontentloaded")
        self.page.wait_for_load_state("domcontentloaded")

    def cerrar_popup(self):
        try:
            c = self.page.locator(self.popup_close)
            if c.first.is_visible():
                c.first.click()
        except:
            pass

        try:
            o = self.page.locator(self.onesignal_cancel)
            if o.is_visible():
                o.click()
        except:
            pass

    # -------------------------
    # SECCIÓN: Contacto
    # -------------------------
    def ir_te_llamamos(self):
        self.page.goto(CONTACTO_URL, wait_until="domcontentloaded")
        self.page.wait_for_url("**/contactanos/")

    # -------------------------
    # SECCIÓN: Pagos
    # -------------------------
    def ir_pagar_servicio(self):
        for i in range(self.link_pagos.count()):
            link = self.link_pagos.nth(i)
            if not link.is_visible():
                continue

            href = link.get_attribute("href")
            if not href or "pagos.xtrim.com.ec" not in href.lower():
                continue

            self.page.goto(href, wait_until="domcontentloaded")
            self.page.wait_for_url(f"{PAGAR_URL}**")
            return

        raise AssertionError("No se encontró un acceso visible a pagos en la home")

    def ir_zapping(self):
        self.link_actualizar_plan.wait_for(state="visible")
        href = self.link_actualizar_plan.get_attribute("href")
        assert href and ZAPPING_URL in href
        self.page.goto(href, wait_until="domcontentloaded")
        self.page.wait_for_url("**/zapping*")
