import re
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize("browser_context", ["newUser"], indirect=True)
def test_investor_dashboard(browser_context): #Verificacion KYC del inversor
    page, user = browser_context
    page.goto("https://app.amaia.io/dashboard")
    page.get_by_role("navigation").get_by_role("img").first.click()
    page.get_by_role("link", name="Profile").click(timeout=3000)
    page.locator(".sidenavbar__header-mob__toggle > svg").click(timeout=3000)
    page.get_by_role("link", name="Verification").click(timeout=3000)
    expect(page.get_by_text("Congratulations, your account")).to_be_visible(), "❌ El inversor se encuentra verificado"
    print("✅ La verificacion del usuario es exitosa")
    
    
    page.get_by_role("link", name="Security").click() #Cambio de password
    page.get_by_role("button", name="Change").click()
    expect(page.get_by_text("Change login password")).to_be_visible(), "❌ El usuario no pudo acceder a la seccion Security"
    print("✅ Modal cambio de password correcto")
    #expect(page.get_by_role("main")).to_match_aria_snapshot("- text: Change login password")
