import pytest
from pages.home_page import HomePage
from pages.pagar_page import PagarPage
from utils.config import BASE_URL

def test_pagar_servicio(page, context):
    home = HomePage(page)

    home.navegar(BASE_URL)
    home.cerrar_popup()

    # Igual que Selenium:
    home.ir_pagar_servicio()

    # Puede abrir nueva pestaña o no
    try:
        new_tab = context.wait_for_event("page", timeout=4000)
        new_tab.wait_for_load_state("domcontentloaded")
        pagar_page = PagarPage(new_tab)
    except:
        pagar_page = PagarPage(page)

    pagar_page.validar_carga()
