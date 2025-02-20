import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Cambia a False para ver la UI
        context = browser.new_context(storage_state="auth.json")  # Carga la sesión guardada
        page = context.new_page()  # Crea una nueva página
        yield page  # Devuelve la página para ser usada en los tests
        browser.close()  # Cierra el navegador después de los tests


