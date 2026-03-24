from pages.home_page import HomePage
from pages.contacto_page import ContactoPage
from utils.config import BASE_URL

def test_formulario_contacto_disponible(page):
    home = HomePage(page)
    contacto = ContactoPage(page)

    home.navegar(BASE_URL)
    home.cerrar_popup()
    home.ir_te_llamamos()

    contacto.validar_carga()
    contacto.validar_formulario_disponible()
