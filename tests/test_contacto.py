import pytest
from pages.home_page import HomePage
from pages.contacto_page import ContactoPage
from utils.config import BASE_URL, TEST_DATA

def test_te_llamamos(page):

    home = HomePage(page)
    contacto = ContactoPage(page)

    home.navegar(BASE_URL)
    home.cerrar_popup()

    home.ir_te_llamamos()

    contacto.completar_formulario(TEST_DATA)
    contacto.enviar()

    assert page.url.startswith("https://www.xtrim.com.ec/contactanos")
