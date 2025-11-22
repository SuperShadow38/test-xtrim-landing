from playwright.sync_api import Page

class PlanesPage:

    def __init__(self, page: Page):
        self.page = page

    def click_plan_zapping_selenium(self):
        css_selector = ".vc_row:nth-child(5) .card-rectangulo:nth-child(4) .vc_general:nth-child(1)"
        plan = self.page.locator(css_selector).first

        plan.wait_for(state="visible")
        plan.scroll_into_view_if_needed()
        plan.click()

    def validar_landing(self):
        self.page.wait_for_load_state("networkidle")
        assert (
            "zapping" in self.page.url.lower()
            or "plan" in self.page.url.lower()
            or "premium" in self.page.url.lower()
        )
