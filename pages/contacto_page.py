from playwright.sync_api import Page

class ContactoPage:

    def __init__(self, page: Page):
        self.page = page
        self.nombre = "#wpforms-11208-field_1"
        self.celular = "#wpforms-11208-field_5"
        self.cedula = "#wpforms-11208-field_2"
        self.email = "#wpforms-11208-field_3"
        self.terminos = "#wpforms-11208-field_4_1"
        self.boton_enviar = "#wpforms-submit-11208"

    def completar_formulario(self, datos):
        self.page.fill(self.nombre, datos["nombre"])
        self.page.fill(self.celular, datos["celular"])
        self.page.fill(self.cedula, datos["cedula"])
        self.page.fill(self.email, datos["email"])
        self.page.click(self.terminos)

    def enviar(self):
        self.page.click(self.boton_enviar)
