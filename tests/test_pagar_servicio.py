from pages.home_page import HomePage
from pages.pagar_page import PagarPage
from utils.config import BASE_URL

def test_pagar_servicio(page):
    home = HomePage(page)
    pagar_page = PagarPage(page)

    home.navegar(BASE_URL)
    home.cerrar_popup()
    home.ir_pagar_servicio()
    pagar_page.validar_carga()
