import pytest

@pytest.fixture(scope="function")
def context(browser):
    ctx = browser.new_context(viewport={"width": 1400, "height": 800})
    yield ctx
    ctx.close()

@pytest.fixture(scope="function")
def page(context):
    p = context.new_page()
    yield p
    p.close()
