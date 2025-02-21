import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.parametrize("browser_context", ["investor"], indirect=True)
def test_investor_dashboard(browser_context):
    page, user = browser_context
    page.goto("https://app.amaia.io/dashboard")
    page.get_by_role("navigation").get_by_role("img").first.click()
    page.get_by_role("link", name="Algorithms").click()
    expect(page.get_by_label("2 /").get_by_role("button", name="Invest now")).to_be_visible()
    page.get_by_role("link", name="Dashboard").click()
    expect(page.get_by_role("link", name="Subscription")).to_be_visible()
    page.get_by_role("link", name="Subscription").click()
    page.locator(".sidenavbar__header-mob__toggle > svg").click()
    
    expect(page.get_by_role("button", name="Cancel subscription")).to_be_visible(), "❌ El inversor no pudo acceder al Dashboard"
    print(f"✅ Acceso exitoso al Dashboard como {user}")

@pytest.mark.parametrize("browser_context", ["newUser"], indirect=True)
def test_new_user_profile(browser_context):
    page, user = browser_context
    page.goto("https://app.amaia.io/dashboard")

    page.locator(".menu_btn").click()
    page.get_by_role("link", name="Profile").click()

    assert page.locator("text=Profile").is_visible(), "❌ El nuevo usuario no pudo acceder al perfil"
    print(f"✅ Acceso exitoso al perfil como {user}")
