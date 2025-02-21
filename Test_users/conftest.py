import pytest
from playwright.sync_api import sync_playwright

# 📌 Diccionario de usuarios con sus archivos de autenticación
USERS = {
    "investor": "auth_investor.json",
    "newUser": "auth_newUser.json"
}
@pytest.fixture
def browser_context(request):
    user_type = request.param  # Obtiene el usuario del parámetro del test

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Cambia a True para modo sin UI
        context = browser.new_context(storage_state=USERS[user_type])  # Carga la sesión guardada
        page = context.new_page()
        page.goto("https://app.amaia.io")
        yield page, user_type  # Devuelve la página y el usuario actual
        browser.close()
