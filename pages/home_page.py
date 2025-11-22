from playwright.sync_api import Page
from utils.config import PAGAR_URL, PLANES_URL, ZAPPING_URL

class HomePage:

    def __init__(self, page: Page):
        self.page = page

        # Selectores
        self.popup_close = ".close"
        self.onesignal_cancel = "#onesignal-slidedown-cancel-button"
        self.menu_movil = "#menu-movil"

        # Menú
        self.link_te_llamamos = "text=Te llamamos"
        self.link_pagar_servicio = "a[title='Pagar Servicio']"
        self.link_planes = "a[title='Planes']"
        self.link_zapping = "text=Zapping"   # ✅ nuevo selector

    # -------------------------
    # Métodos base
    # -------------------------
    def navegar(self, url):
        self.page.goto(url, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")

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

    def abrir_menu_movil(self):
        try:
            mm = self.page.locator(self.menu_movil)
            if mm.is_visible():
                mm.click()
        except:
            pass

    # -------------------------
    # SECCIÓN: Te Llamamos
    # -------------------------
    def ir_te_llamamos(self):
        link = self.page.locator(self.link_te_llamamos).first
        if link.is_visible():
            link.click()
        else:
            self.abrir_menu_movil()
            link = self.page.locator(self.link_te_llamamos).first
            link.click()

    # -------------------------
    # SECCIÓN: Pagar Servicio
    # -------------------------
    def ir_pagar_servicio(self):
        link = self.page.locator(self.link_pagar_servicio).first

        if link.is_visible():
            link.click()
            return

        self.abrir_menu_movil()
        link = self.page.locator(self.link_pagar_servicio).first
        if link.is_visible():
            link.click()
            return

        # fallback
        self.page.goto(PAGAR_URL, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")

    # -------------------------
    # SECCIÓN: Planes / Zapping
    # -------------------------
    def ir_planes(self):
        link = self.page.locator(self.link_planes).first

        if link.is_visible():
            link.click()
            self.page.wait_for_load_state("networkidle")
            return

        self.abrir_menu_movil()
        link = self.page.locator(self.link_planes).first
        if link.is_visible():
            link.click()
            self.page.wait_for_load_state("networkidle")
            return

        # fallback
        self.page.goto(PLANES_URL, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")


    def ir_zapping(self):
        """
        Replica el Selenium:
        - click directo en 'Zapping' del menú
        - si no está visible, abre menú móvil
        - si igual falla, va directo a /zapping/
        """
        link = self.page.locator(self.link_zapping).first

        if link.is_visible():
            link.click()
            self.page.wait_for_load_state("networkidle")
            return

        self.abrir_menu_movil()
        link = self.page.locator(self.link_zapping).first
        if link.is_visible():
            link.click()
            self.page.wait_for_load_state("networkidle")
            return

        # fallback directo
        self.page.goto(ZAPPING_URL, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")
