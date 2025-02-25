import re
from playwright.sync_api import Page, expect
import pytest


@pytest.mark.parametrize("browser_context", ["investor", "newUser"], indirect=True)
def test_deposit_investor(browser_context): #FUncionalidad del boton de Deposito
    page, user = browser_context
    page.goto("https://app.amaia.io/dashboard")
    page.get_by_role("navigation").get_by_role("img").first.click()
    expect(page.get_by_text("Deposit").first).to_be_visible()
    page.get_by_text("Deposit").first.click(), "❌ El boton de deposito no responde"
    print(f"✅ Codigo QR funcional {user}")
    expect(page.get_by_role("heading", name="Scan the QR code below")).to_be_visible()
    page.get_by_role("img", name="Scan me!").click()