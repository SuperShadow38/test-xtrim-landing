from playwright.sync_api import Page

class ContactoPage:

    def __init__(self, page: Page):
        self.page = page
        self.nombre = self.page.locator("#wpforms-11208-field_1")
        self.cedula = self.page.locator("#wpforms-11208-field_2")
        self.celular = self.page.locator("#wpforms-11208-field_5")
        self.email = self.page.locator("#wpforms-11208-field_3")
        self.terminos = self.page.locator("#wpforms-11208-field_4_1")
        self.boton_enviar = self.page.locator("#wpforms-submit-11208")

    def validar_carga(self):
        self.nombre.wait_for(state="visible")
        assert "/contactanos" in self.page.url.lower()

    def validar_formulario_disponible(self):
        self.nombre.wait_for(state="visible")
        self.cedula.wait_for(state="visible")
        self.celular.wait_for(state="visible")
        self.email.wait_for(state="visible")
        self.terminos.wait_for(state="visible")
        self.boton_enviar.wait_for(state="visible")
