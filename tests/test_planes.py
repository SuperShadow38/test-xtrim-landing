import pytest
from pages.home_page import HomePage
from pages.planes_page import PlanesPage
from utils.config import BASE_URL

def test_planes_zapping(page, context):
    home = HomePage(page)
    planes = PlanesPage(page)

    home.navegar(BASE_URL)
    home.cerrar_popup()

    home.ir_zapping()

    planes.click_plan_zapping_selenium()

    # Validar landing
    planes.validar_landing()
