import pytest

STEALTH_INIT_SCRIPT = """
Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
window.chrome = { runtime: {} };
Object.defineProperty(navigator, 'languages', { get: () => ['es-EC', 'es', 'en-US', 'en'] });
Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
"""

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "args": ["--disable-blink-features=AutomationControlled"]
    }

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": {"width": 1400, "height": 800},
        "locale": "es-EC",
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/141.0.0.0 Safari/537.36"
        ),
    }

@pytest.fixture(scope="function")
def context(browser, browser_context_args):
    ctx = browser.new_context(**browser_context_args)
    yield ctx
    ctx.close()

@pytest.fixture(scope="function")
def page(context):
    p = context.new_page()
    p.add_init_script(STEALTH_INIT_SCRIPT)
    yield p
    p.close()
