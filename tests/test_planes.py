from pages.home_page import HomePage
from pages.planes_page import PlanesPage
from utils.config import BASE_URL

def test_planes_zapping(page):
    home = HomePage(page)
    home.navegar(BASE_URL)
    home.cerrar_popup()
    home.ir_zapping()

    planes = PlanesPage(page)
    planes.abrir_actualizacion()
    planes.validar_landing_actualizacion()
