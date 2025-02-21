from playwright.sync_api import sync_playwright

def save_auth_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Cambia a True si no necesitas ver la UI
        context = browser.new_context()  # Crea un nuevo contexto sin cookies previas
        page = context.new_page()
        
        # 🔹 1️⃣ Navega a la página de log
        page.goto("https://app.amaia.io/login")

        # 🔹 2️⃣ Ingresa credenciales y hace login
        page.get_by_role("textbox", name="JohnDoe").click()
        page.get_by_role("textbox", name="JohnDoe").fill("camila")
        page.get_by_role("textbox", name="Enter your password").click()
        page.get_by_role("textbox", name="Enter your password").fill("Test123*")
        page.get_by_role("button", name="Login").click(timeout=3000)
        page.wait_for_timeout(3000)
        #page.get_by_role("button", name="Login").click()
        
        # 🔹 3️⃣ Espera a que el login sea exitoso
        page.wait_for_selector("text=Successfully, Logged In", timeout=10000)  # Ajusta el texto según el sitio
        page.wait_for_timeout(3000)
        # 🔹 4️⃣ Guarda el estado de autenticación (cookies + local storage)
        context.storage_state(path="auth.json")

        print("✅ Estado de autenticación guardado en 'auth.json'")
        browser.close()

# Ejecuta el script para generar el archivo auth.json
if __name__ == "__main__":
    save_auth_state()
