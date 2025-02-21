import re
from playwright.sync_api import Playwright, sync_playwright, expect, Page
import pytest

def test_access_protected_page(browser_context): #Visualizacion del dashboard nuevo usuario
    page = browser_context
    page.goto("https://app.amaia.io/dashboard")  # Ir directamente a una página que requiere login
    expect(page.get_by_text("Great job! you are now")).to_be_visible()

def test_verification(browser_context): #Mensaje de felicidades qal ingresar qal modulo de verificacion despues del KYC
    page = browser_context
    page.goto("https://app.amaia.io/dashboard")
    page.locator(".menu_btn").click()
    page.get_by_role("link", name="Profile").click()
    page.locator(".sidenavbar__header-mob__toggle > svg").click(timeout=3000)
    page.get_by_role("link", name="Verification").click(timeout=5000)
    expect(page.get_by_text("Congratulations, your account")).to_be_visible()
    page.screenshot(path="demo.png") #Toma un screenshot de la verificacion realizada 


    